Configuration
=============

You can use configuration files to change the way pytest runs. If you repeatedly
use certain options in your tests, such as :samp:`--verbose` or
:samp:`--strict-markers`, you can store them in a configuration file so that you
don’t have to enter them again and again. In addition to the configuration
files, there are a handful of other files that are helpful when using pytest to
make writing and running tests easier:

:file:`pytest.ini`
    This is the most important configuration file of pytest, with which you can
    change the default behaviour of pytest. It also defines the root directory
    of pytest, or ``rootdir``.
:file:`conftest.py`
    This file contains :doc:`fixtures` and hook functions. It can exist in
    ``rootdir`` or in any subdirectory.
:file:`__init__.py`
    If this file is stored in test subdirectories, it enables the use of
    identical test file names in several test directories.

If you already have a :file:`tox.ini`, :file:`pyproject.toml` or
:file:`setup.cfg` in your project, they can take the place of the
:file:`pytest.ini` file: :file:`tox.ini` is used by :doc:`../tox`,
:file:`pyproject.toml` and :file:`setup.cfg` are used for packaging Python
projects and can be used to store settings for various tools, including pytest.

You should have a configuration file, either :file:`pytest.ini`, or a ``pytest``
section in :file:`tox.ini`, :file:`pyproject.toml` or in :file:`setup.cfg`.

The configuration file defines the top-level directory from which ``pytest`` is
started.

Let’s take a look at some of these files in the context of a project directory
structure:

.. code-block:: console
   :emphasize-lines: 3, 7, 8

   items
   ├── …
   ├── pytest.ini
   ├── src
   │   └── …
   └── tests
       ├── __init__.py
       ├── conftest.py
       └── test_….py

In the case of the ``items`` project that we have used for testing so far, there
is a :file:`pytest.ini` file and a :file:`tests` directory at the top level. We
will refer to this structure when we talk about the various files in the rest of
this section.

Saving settings and options in :file:`pytest.ini`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ini

   [pytest]
   addopts =
       --strict-markers
       --strict-config
       -ra
   testpaths = tests
   markers =
       smoke: Small subset of all tests
       exception: Only run expected exceptions

``[pytest]`` marks the start of the pytest section. This is followed by the
individual settings. For configuration settings that allow more than one value,
the values can be written either in one or more lines in the form
:samp:`{SETTING} = {VALUE1} {VALUE2}`. With ``markers``, however, only one
marker per line is permitted.

This example is a simple :file:`pytest.ini` file that I use in almost all my
projects. Let’s briefly go through the individual lines:

.. _addopts:

``addopts``
    allows you to specify the pytest options that we always want to execute in
    this project.
``--strict-markers``
    instructs pytest to issue an error instead of a warning for every
    unregistered marker that appears in the test code. This allows us to avoid
    typos in marker names.
``--strict-config``
    instructs pytest to issue an error instead of a warning if difficulties
    arise when parsing configuration files. This prevents typing errors in the
    configuration file from going unnoticed.
``-ra``
    instructs pytest to display not only additional information on failures and
    errors at the end of a test run, but also a test summary.

    ``-r``
        displays additional information on the test summary.
    ``a``
        displays all but the passed tests. This adds the information
        ``skipped``, ``xfailed`` or ``xpassed`` to the failures and errors.

``testpaths = tests``
    tells pytest where to look for tests if you have not specified a file or
    directory name on the command line. In our case, pytest searches in the
    :file:`tests` directory.

    At first glance, it may seem superfluous to set ``testpaths`` to
    :file:`tests`, as pytest searches there anyway and we do not have any
    :file:`test_` files in our :file:`src` or :file:`docs` directories. However,
    specifying a ``testpaths`` directory can save a little startup time,
    especially if our :file:`src`, :file:`docs` or other directories are quite
    large.

``markers =``
    is used to declare markers, as described in
    :ref:`select-tests-with-markers`.

.. seealso::
   You can specify many other configuration settings and command line options in
   the configuration files, which you can display using the ``pytest --help``
   command.

Using other configuration files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are writing tests for a project that already has a
:file:`pyproject.toml`, :file:`tox.ini` or :file:`setup.cfg` file, you can use
:file:`pytest.ini` to store your pytest configuration settings, or you can store
your configuration settings in one of these alternative configuration files. The
syntax of the two non-ini files is slightly different, so we will take a closer
look at both files.

:file:`pyproject.toml`
::::::::::::::::::::::

The :file:`pyproject.toml` file was originally intended for the packaging of
Python projects; however, it can also be used to define project settings.

As :doc:`Python4DataScience:data-processing/serialisation-formats/toml/index` is
a different standard for configuration files than :file:`.ini` files, the format
is also slightly different:

.. code-block:: toml

   [tool.pytest.ini_options]
   addopts = [
       "--strict-markers",
       "--strict-config",
       "-ra"
       ]
   testpaths = "tests"
   markers = [
       "exception: Only run expected exceptions",
       "finish: Only run finish tests",
       "smoke: Small subset of all tests",
       "num_items: Number of items to be pre-filled for the items_db fixture"
       ]

Instead of ``[pytest]``, the section begins with ``[tool.pytest.ini_options]``,
the values must be enclosed in quotes and lists of values must be lists of
character strings in square brackets.

:file:`setup.cfg`
:::::::::::::::::

The file format of the :file:`setup.cfg` corresponds to an :file:`.ini` file:

.. code-block:: ini

   [tool:pytest]
   addopts =
       --strict-markers
       --strict-config
       -ra
   testpaths = tests
   markers =
       smoke: Small subset of all tests
       exception: Only run expected exceptions

The only difference between this and :file:`pytest.ini` is the specification of
the ``[tool:pytest]`` section.

.. warning::
   However, the parser of the :file:`.cfg` file differs from the parser of the
   :file:`.ini` file, and this difference can cause problems that are difficult
   to track down, see also `pytest documentation
   <https://docs.pytest.org/en/latest/reference/customize.html#setup-cfg>`_.

Set ``rootdir``
---------------

Before pytest searches for test files to execute, it reads the configuration
file :file:`pytest.ini`, :file:`tox.ini`, :file:`pyproject.toml` or
:file:`setup.cfg`, which contains a pytest section:

* if you have specified a :file:`test` directory, pytest will start searching
  there
* if you have specified several files or directories, pytest starts with the
  parent directory
* if you do not specify a file or directory, pytest starts in the current
  directory.

If pytest finds a configuration file in the start directory, this is the root
and if not, pytest goes up the directory tree until it finds a configuration
file that contains a pytest section. Once pytest has found a configuration file,
it marks the directory in which it found it as ``rootdir``. This root directory
is also the relative root of the IDs. pytest also tells you where it has found a
configuration file. Using these rules, we can run tests at different levels and
be sure that pytest finds the correct configuration file:

.. code-block:: pytest
   :emphasize-lines: 5, 6

   $ cd items
   $ pytest
   ============================= test session starts ==============================
   ...
   rootdir: /Users/veit/cusy/prj/items
   configfile: pyproject.toml
   testpaths: tests
   plugins: Faker-19.11.0
   collected 39 items
   ...

:file:`conftest.py` for sharing local fixtures and hook functions
-----------------------------------------------------------------

The :file:`conftest.py` file is used to store fixtures and hook functions, see
also :doc:`fixtures` and :doc:`plugins`. You can have as many
:file:`conftest.py` files in a project as you like. Everything that is defined
in a :file:`conftest.py` file applies to tests in this directory and all
subdirectories. If you have a :file:`conftest.py` file at the top test level,
the fixtures defined there can be used for all tests. If there are special
fixtures that only apply to a subdirectory, these can be defined in another
conftest.py file in this subdirectory. For example, the CLI tests may require
different fixtures than the API tests, and you can also share some of them.

.. tip::
   However, it is a good idea to keep only one :file:`conftest.py` file so that
   you can easily find the fixture definitions. Even though we can always find
   out where a fixture is defined with ``pytest --fixtures -v``, it is still
   easier if it is always defined in the one :file:`conftest.py` file.

:file:`__init__.py` to avoid collision of test file names
---------------------------------------------------------

The :file:`__init__.py` file allows you to have duplicate test filenames. If you
have :file:`__init__.py` files in each test subdirectory, you can use the same
test filename in multiple directories, for example:

.. code-block:: console
   :emphasize-lines: 8, 11

   items
   ├── …
   ├── pytest.ini
   ├── src
   │   └── …
   └── tests
       ├── api
       │   ├── __init__.py
       │   └── test_add.py
       ├── cli
       │   ├── __init__.py
       │   ├── conftest.py
       │   └── test_add.py
       └── conftest.py

Now we can test the ``add`` functionality both via the :abbr:`API (Application
Programming Interface)` and via the :abbr:`CLI (Command Line Interface)`,
whereby a :file:`test_add.py` is located in both directories:

.. code-block:: pytest

   $ pytest
   ============================= test session starts ==============================
   ...
   rootdir: /Users/veit/cusy/prj/items
   configfile: pyproject.toml
   testpaths: tests
   plugins: Faker-19.11.0
   collected 6 items

   tests/api/test_add.py ....                                               [ 66%]
   tests/cli/test_add.py ..                                                 [100%]

   ============================== 6 passed in 0.03s ===============================


----

Most of my projects start with the following configuration:

.. code-block:: ini

   addopts =
      --strict-markers
      --strict-config
      -ra

.. seealso::
   * `Configuration
     <https://docs.pytest.org/en/latest/reference/customize.html>`_
   * `Configuration Options
     <https://docs.pytest.org/en/latest/reference/reference.html#configuration-options>`_
