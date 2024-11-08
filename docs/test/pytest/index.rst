pytest
======

:doc:`pytest <pytest:index>` is an alternative to Python’s :doc:`../unittest`
module that simplifies testing even further.

Features
--------

* More detailed information about failed ``assert`` statements
* Automatic detection of test modules and functions
* Modular fixtures for the management of small or parameterised, long-lived test
  resources
* Can also execute unit tests without presets
* Extensive plug-in architecture, with over 800 external plug-ins

Installation
------------

You can install pytest in `virtual environments <venv>` with:

.. tab:: Linux/macOS

   .. code-block:: console

      $ python -m pip install pytest
      Collecting pytest
      …
      Successfully installed attrs-21.2.0 iniconfig-1.1.1 pluggy-1.0.0 py-1.10.0 pytest-6.2.5 toml-0.10.2

.. tab:: Windows

   .. code-block:: ps1con

      C:> python -m pip install pytest
      Collecting pytest
      …
      Successfully installed attrs-21.2.0 iniconfig-1.1.1 pluggy-1.0.0 py-1.10.0 pytest-6.2.5 toml-0.10.2

.. toctree::
   :titlesonly:
   :hidden:

   examples
   functions
   testsuite
   fixtures
   builtin-fixtures
   params
   markers
   plugins
   config
   debug
   coverage
