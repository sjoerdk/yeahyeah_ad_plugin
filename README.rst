==================
YeahYeah AD Plugin
==================


.. image:: https://img.shields.io/pypi/v/yeahyeah_ad_plugin.svg
        :target: https://pypi.python.org/pypi/yeahyeah_ad_plugin

.. image:: https://img.shields.io/travis/sjoerdk/yeahyeah_ad_plugin.svg
        :target: https://travis-ci.org/sjoerdk/yeahyeah_ad_plugin

.. image:: https://readthedocs.org/projects/yeahyeah-ad-plugin/badge/?version=latest
        :target: https://yeahyeah-ad-plugin.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/sjoerdk/yeahyeah_ad_plugin/shield.svg
     :target: https://pyup.io/repos/github/sjoerdk/yeahyeah_ad_plugin/
     :alt: Updates



Adds Active Directory interfacing to YeahYeah launch manager <https://github.com/sjoerdk/yeahyeah>


* Free software: MIT license
* Documentation: https://yeahyeah-ad-plugin.readthedocs.io.


Features
--------

AD connection fully based on umcnad_ library:

* Search z-numbers
* translate all z-numbers in running text
* As one-off commands and reading from stdin

Installation
------------
* Install the YeahYeah_ launch manager
* Install this lib::

    $ pip install yeahyeah_ad_plugin

* Follow the steps for plugin_installation_ with plugin path to yeahyeah::

    `yeahyeah_ad_plugin.core.ADPlugin`


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

.. _umcnad: https://github.com/DIAGNijmegen/umcnad
.. _YeahYeah: https://github.com/sjoerdk/yeahyeah
.. _plugin_installation: https://yeahyeah.readthedocs.io/en/latest/plugins.html#plugin-installation