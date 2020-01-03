import sys

import click
from umcnad.core import UMCNPerson

from yeahyeah.decorators import pass_yeahyeah_context
from yeahyeah.context import YeahYeahContext
from yeahyeah.persistence import JSONSettingsFile
from yeahyeah_ad_plugin.context import (
    default_settings_file_name,
    default_context,
    ADPluginContext,
    pass_ad_context,
)
from yeahyeah_ad_plugin.decorators import handle_umcnad_exceptions
from yeahyeah_ad_plugin.translator import find_z_numbers, Translator


@click.group(name="ad")
@click.pass_context
@pass_yeahyeah_context
def main(context: YeahYeahContext, ctx):
    """query active directory"""
    settings_file = JSONSettingsFile(
        path=context.settings_path / default_settings_file_name
    )
    if not settings_file.exists():
        click.echo(
            f"settings file not found. writing default context to {settings_file.path}"
        )
        settings_file.save(dict_in=default_context.to_dict())
    ctx.obj = ADPluginContext.init_from_dict(settings_file.load())


@click.command()
@pass_ad_context
def status(context: ADPluginContext):
    """show server and api key"""
    click.echo(f"hello {context}")


@click.command()
@handle_umcnad_exceptions
@pass_ad_context
@click.argument("z_numbers", nargs=-1)
def find_z_number(context: ADPluginContext, z_numbers):
    """print name and info for z-number if possible"""
    if not z_numbers:
        raise click.badparameter("no z-numbers given")
    people = context.search_people(list(z_numbers))
    for person in people:
        click.echo(f"{person} - {person.department}")


@click.command()
@handle_umcnad_exceptions
@pass_ad_context
@click.argument("last_name_first_name",
                nargs=-1)
def find_name(context: ADPluginContext, last_name_first_name):
    """print name and info for z-number if possible"""
    if not last_name_first_name:
        raise click.BadParameter("last_name is required")
    last_name = last_name_first_name[0]
    if last_name_first_name[1:]:
        first_name_or_initial = last_name_first_name[1:]
    else:
        first_name_or_initial = None

    people = context.search_person_by_name(
        last_name=last_name, first_name_or_initial=first_name_or_initial)
    for person in people:
        click.echo(f"{person} - {person.department}")


def read_stdin():
    """

    Returns
    -------
    str
        All input from stdin. Might contain newlines
    """
    return ''.join(sys.stdin.readlines())


@click.command()
@handle_umcnad_exceptions
@pass_ad_context
@click.argument("input_string", nargs=-1)
@click.option(
    "--department/--no-department", default=False, help="Print department after name"
)
@click.option(
    "--email/--no-email", default=False, help="Print email after name"
)
@click.option(
    "--stdin/--no-stdin", default=False, help="Read from standard in"
)
def translate(context: ADPluginContext, input_string, department, email, stdin):
    """replace any z-number in input text with name"""
    if stdin:
        input_string = read_stdin()
    else:
        input_string = " ".join(input_string)
    if not input_string:
        return
    people = context.search_people(list(find_z_numbers(input_string)))

    def person_to_string(person: UMCNPerson):
        person_string = str(person)
        if department:
            person_string += f"({person.department})"
        if email:
            person_string += f"({person.email})"
        return person_string

    glossary = {x.z_number: person_to_string(x) for x in people}
    click.echo(Translator(glossary).process(input_string))


@click.command()
@handle_umcnad_exceptions
@pass_yeahyeah_context
def edit_settings(context: YeahYeahContext):
    """open context file for editing"""
    click.launch(str(context.settings_path / default_settings_file_name))


for func in [status, find_z_number, translate, find_name]:
    main.add_command(func)
