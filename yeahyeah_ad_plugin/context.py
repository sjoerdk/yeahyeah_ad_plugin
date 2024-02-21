"""Context that gets passed around to this yeahyeah_plugins' functions

"""


import click
from umcnad.core import ADConnection
from typing import List

from yeahyeah_ad_plugin.persistence import KeyRingStorage, KeyringError


class ADPluginContext:
    """Context that gets passed to each ad_plugins function

    """
    def __init__(self, server_url, bind_dn):
        self.server_url = server_url
        self.bind_dn = bind_dn

    def search_people(self, z_numbers: List[str]):
        """
        Parameters
        ----------
        z_numbers: List[str]
            List of z-numbers to search for
        """
        with ADConnection(url=self.server_url, bind_dn=self.bind_dn,
                          password=self.get_pass()) as connection:
            return connection.search_z_numbers(z_numbers)

    def search_person_by_name(self, last_name, first_name_or_initial=None):
        with ADConnection(url=self.server_url, bind_dn=self.bind_dn,
                          password=self.get_pass()) as connection:
            filter_string = ""
            if first_name_or_initial:
                filter_string = f"first_name={first_name_or_initial} and"
            filter_string = filter_string +  f"last_name={last_name}"
            return connection.search_people(filter_string)

    @staticmethod
    def get_pass():
        """Get password for binding to AD. To be replaced with something more
        convenient later """
        keyring = KeyRingStorage()
        try:
            return keyring.load_password()
        except KeyringError as e:
            click.echo(f"Could not find AD password in keyring (error: {e})")
            return click.prompt('password for umcn AD', hide_input=True)

    @classmethod
    def init_from_dict(cls, dict_in):
        return cls(server_url=dict_in["server_url"], bind_dn=dict_in["bind_dn"])

    def to_dict(self):
        return {"server_url": self.server_url, "bind_dn": self.bind_dn}


pass_ad_context = click.make_pass_decorator(ADPluginContext)
default_context = ADPluginContext(
    server_url="<ldap://adserver:port>",
    bind_dn="<ldap dn to access AD. Something looking like 'cn=bla,ou=blab,dc=thing'>"
)
default_settings_file_name = "ad_umcn.json"