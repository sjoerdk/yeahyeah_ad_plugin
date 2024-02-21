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
* Install this lib:
```
    $ pip install yeahyeah_ad_plugin
```
* yeahyeah_ad_plugin depends on `python-ldap` which might require [build prerequisites](https://www.python-ldap.org/en/latest/installing.html#build-prerequisites) to install.
  If poetry has trouble installing, try installing manually using 'pip install python-ldap'
* Follow the steps for [plugin_installation](https://yeahyeah.readthedocs.io/en/latest/plugins.html#plugin-installation) with plugin path to yeahyeah
```
    `yeahyeah_ad_plugin.core.ADPlugin`
```

## Configuration
Yeahyeah uses a settings file `ad_umcn.json` in the yeahyeah settings directory 
(default: `~/.config/yeahyeah`)

You can save the AD password using `yeahyeah admin umcn_AD set-password`