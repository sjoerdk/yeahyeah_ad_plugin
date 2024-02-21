# YeahYeah AD Plugin

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/yeahyeah_ad_plugin)](https://pypi.org/project/yeahyeah_ad_plugin/)

Adds Active Directory interfacing to [YeahYeah launch manager](https://github.com/sjoerdk/yeahyeah)

* Free software: MIT license

## Features

AD connection fully based on [umcnad](https://github.com/DIAGNijmegen/umcnad) library:

* Search z-numbers
* translate all z-numbers in running text
* As one-off commands and reading from stdin

## Installation
* Install the [YeahYeah launch manager](https://github.com/sjoerdk/yeahyeah)
* Install this lib::

    $ pip install yeahyeah_ad_plugin

* Follow the steps for [plugin_installation](https://yeahyeah.readthedocs.io/en/latest/plugins.html#plugin-installation) with plugin path to yeahyeah::

    `yeahyeah_ad_plugin.core.ADPlugin`
