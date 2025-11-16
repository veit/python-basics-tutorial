pytest
======

:doc:`pytest <pytest:index>` is an alternative to Python’s :doc:`../unittest`
module that simplifies testing even further.

* pytest automatically recognises tests based on filenames and functions that
  start with ``test_``, while unittest derives test classes and methods from
  :class:`unittest.TestCase`. This results in simpler, more readable syntax with
  less boilerplate code.
* unittest provides a set of assertion methods (for example,
  :func:`assertEqual`, :func:`assertTrue`, :func:`assertRaises`). With pytest,
  the same assertions can be defined, but using Python’s standard :func:`assert`
  statement. This often results in more meaningful error messages and better
  introspection.
* unittest only provides :func:`setUp` and :func:`tearDown` methods for
  fixtures. In pytest, on the other hand, :doc:`fixtures <fixtures>` are defined
  as functions, which promotes reusability and simplifies the management of
  test dependencies.
* Parametrised tests are possible in unittest, but require additional effort.
  pytest, however, includes the :doc:`decorator  <../../functions/decorators>`
  ``@pytest.mark.parametrize``, which makes it easy to run test functions with
  different inputs and expected outputs.
* pytest has an extensive ecosystem with over 800 :doc:`plugins` for advanced
  testing requirements; unittest is more limited in its extensibility.

Installation
------------

You can install pytest in `virtual environments <venv>` with:

.. tab:: Linux/macOS

   .. code-block:: console

      $ python -m pip install pytest
      Collecting pytest
      ...
      Successfully installed attrs-21.2.0 iniconfig-1.1.1 pluggy-1.0.0 py-1.10.0 pytest-6.2.5 toml-0.10.2

.. tab:: Windows

   .. code-block:: ps1con

      C:> python -m pip install pytest
      Collecting pytest
      ...
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
   command-line-options
   debug
   coverage
