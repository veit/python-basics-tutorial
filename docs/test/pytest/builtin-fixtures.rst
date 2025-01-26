Built-in fixtures
=================

Reusing common fixtures is such a good idea that pytest has built in some
commonly used fixtures. The built-in fixtures help you to do some very useful
things in your tests easily and consistently. Among other things, pytest
includes built-in fixtures that can handle temporary directories and files,
access command line options, communicate between test sessions, validate output
streams, change environment variables and query warnings.

``tmp_path`` and ``tmp_path_factory``
-------------------------------------

The :ref:`tmp_path <pytest:tmp_path>` and `tmp_path_factory
<https://docs.pytest.org/en/latest/how-to/tmp_path.html#the-tmp-path-factory-fixture>`_
fixtures are used to create temporary directories. The ``tmp_path`` fixture for
the ``function`` scope returns a :class:`pathlib.path` instance that points to a
temporary directory that persists during the test and a little longer. The
``tmp_path_factory`` for a session scope fixture returns a ``TempPathFactory``
object. This object has an ``mktemp()`` function that returns path objects. With
``mktemp()`` you can create multiple temporary directories.

In :doc:`fixtures` we have used the standard library
``tempfile.TemporaryDirectory`` for our ``db`` fixture:

.. code-block:: python

   from pathlib import Path
   from tempfile import TemporaryDirectory


   @pytest.fixture(scope="session")
   def db():
       """ItemsDB object connected to a temporary database"""
       with TemporaryDirectory() as db_dir:
           db_path = Path(db_dir)
           db_ = items.ItemsDB(db_path)
           yield db_
           db_.close()

Let’s use one of the new built-ins instead. Since our ``db`` fixture is in the
``session`` scope, we can’t use ``tmp_path`` because ``session`` scope fixtures
can’t use ``function`` scope fixtures. However, we can use ``tmp_path_factory``:

.. code-block:: python

   @pytest.fixture(scope="session")
   def db(tmp_path_factory):
       """ItemsDB object connected to a temporary database"""
       db_path = tmp_path_factory.mktemp("items_db")
       db_ = items.ItemsDB(db_path)
       yield db_
       db_.close()

.. note::
   We can also remove two import statements because we don’t need to import
   ``pathlib`` or ``tempfile``.

.. tip::
   Do not use :ref:`tmpdir <pytest:tmpdir>` or :ref:`tmpdir_factory
   <pytest:tmpdir>` as they provide :class:`py.path.local` objects, a legacy
   type.

The base directory for all temporary pytest directories is system and
application-dependent. It contains a :samp:`pytest-{NUM}` part, where
:samp:`{NUM}` is incremented for each session. The base directory is left
unchanged immediately after a session so that you can examine it in the case of
test errors. pytest finally cleans them up. Only the last few temporary base
directories are left on the system.

You can also specify your own base directory with :samp:`pytest
--basetemp={MYDIR}`.

.. _capsys-fixture:

``capsys``
----------

Sometimes the application code should output something to ``stdout``, ``stderr``
:abbr:`etc. (et cetera)` The Items example project therefore also has a command
line interface, which we now want to test.

The ``items version`` command should output the version:

.. code-block:: console

   $ items version
   0.1.0

The version is also available via Python:

.. code-block:: pycon

   >>> import items
   >>> items.__version__
   '0.1.0'

One way to test this is

#. execute the command with ``subprocess.run()``
#. capture the output
#. compare it with the version from the API

.. code-block:: python

   import subprocess

   import items


   def test_version():
       process = subprocess.run(
           ["items", "version"], capture_output=True, text=True
       )
       output = process.stdout.rstrip()
       assert output == items.__version__

The ``rstrip()`` function is used to remove the line break.

The `capsys
<https://docs.pytest.org/en/latest/reference/reference.html#capsys>`_ fixture
allows us to capture writes to ``stdout`` and ``stderr``. We can call the method
that implements this in the :abbr:`CLI (Command Line Interface)` directly and
use capsys to read the output:

.. code-block::

   import items


   def test_version(capsys):
       items.cli.version()
       output = capsys.readouterr().out.rstrip()
       assert output == items.__version__

The ``capsys.readouterr()`` method returns a ``namedtuple`` that contains
``out`` and ``err``. We only read the ``out`` part and then we remove the line
break with ``rstrip()``.

Another feature of ``capsys`` is the ability to temporarily disable pytest’s
normal output capture. pytest normally captures the output of your tests and
application code. This includes ``print`` statements.

.. code-block:: python

   import items


   def test_stdout():
       version = items.__version__
       print("\nitems " + version)

However, when we run the test, we do not see any output:

.. code-block:: pytest

   $ pytest tests/test_output.py
   ============================= test session starts ==============================
   …
   collected 1 item

   tests/test_output.py .                                                   [100%]

   ============================== 1 passed in 0.00s ===============================

pytest captures the entire output. While this helps to keep the command line
session clean, there may be times when we want to see the entire output, even if
the test passes. For this we can use the ``-s`` or ``--capture=no`` option:

.. code-block:: pytest
   :emphasize-lines: 7

   $ pytest -s tests/test_output.py
   ============================= test session starts ==============================
   …
   collected 1 item

   tests/test_output.py
   items 0.1.0
   .

   ============================== 1 passed in 0.00s ===============================

Another way to always include the output is ``capsys.disabled()``:

.. code-block:: python

   import items


   def test_stdout(capsys):
       with capsys.disabled():
           version = items.__version__
           print("\nitems " + version)

Now the output is always displayed in the ``with`` block, even without the
``-s`` option:

.. code-block:: pytest

   $ pytest tests/test_output.py
   ============================= test session starts ==============================
   …
   collected 1 item

   tests/test_output.py
   items 0.1.0
   .                                                   [100%]

   ============================== 1 passed in 0.00s ===============================

.. seealso::

   ``capfd``
       Like ``capsys``, but captures file descriptors 1 and 2, which are
       normally the same as ``stdout`` and ``stderr``
   ``capsysbinary``
       While capsys captures text, capsysbinary captures bytes
   ``capfdbinary``
       captures bytes in file descriptors 1 and 2
   ``caplog``
       captures output written with the logging package

.. _monkeypatch-fixture:

``monkeypatch``
---------------

With ``capsys`` I can control the ``stdout`` and ``stderr`` output just fine,
but it’s still not the way I want to test the :abbr:`CLI (Command Line
Interface)`. The Items application uses a library called `Typer
<https://typer.tiangolo.com>`_, which contains a runner function to test our
code the way we would expect a command line test to, which stays in process and
provides us with output hooks, for example:

.. code-block:: python

   from typer.testing import CliRunner

   import items


   def test_version():
       runner = CliRunner()
       result = runner.invoke(items.app, ["version"])
       output = result.output.rstrip()
       assert output == items.__version__

We will use this method of output testing as a starting point for the rest of
the Items CLI tests. I started with the CLI tests by testing the Items version.
To test the rest of the CLI, we need to redirect the database to a temporary
directory, just like we did when testing the API using :ref:`fixtures for setup
and teardown <setup-and-teardown-fixtures>`. We now use `monkeypatch
<https://docs.pytest.org/en/latest/reference/reference.html#monkeypatch>`_ for
this:

A monkey patch is a dynamic change to a class or module during runtime. During
testing, monkey patching is a convenient way to take over part of the runtime
environment of the application code and replace either input or output
dependencies with objects or functions that are more suitable for testing. With
the built-in fixture ``monkeypatch`` you can do this in the context of a single
test. It is used to change objects, dicts, environment variables, ``PYTHONPATH``
or the current directory. It’s like a mini version of :doc:`../mock`. And when
the test ends, regardless of whether it passes or fails, the original, unpatched
code is restored and everything that was changed by the patch is undone.

.. seealso::
   `How to monkeypatch/mock modules and environments
   <https://docs.pytest.org/en/latest/how-to/monkeypatch.html>`_

The ``monkeypatch`` fixture offers the following functions:

+-------------------------------------------------------+-----------------------+
| Function                                              | Description           |
+=======================================================+=======================+
| :samp:`setattr(TARGET, NAME, VALUE, raising=True)`    | sets an attribute     |
| [1]_                                                  |                       |
+-------------------------------------------------------+-----------------------+
| :samp:`delattr(TARGET, NAME, raising=True)` [1]_      | deletes an attribute  |
+-------------------------------------------------------+-----------------------+
| :samp:`setitem(DICT, NAME, VALUE)`                    | sets a dict entry     |
|                                                       |                       |
+-------------------------------------------------------+-----------------------+
| :samp:`delitem(DICT, NAME, raising=True)` [1]_        | deletes a dict entry  |
+-------------------------------------------------------+-----------------------+
| :samp:`setenv(NAME, VALUE, prepend=None)` [2]_        | sets an environment   |
|                                                       | variable              |
+-------------------------------------------------------+-----------------------+
| :samp:`delenv(NAME, raising=True)` [1]_               | deletes an environment|
|                                                       | variable              |
+-------------------------------------------------------+-----------------------+
| :samp:`syspath_prepend(PATH)`                         | expands the path      |
|                                                       | ``sys.path``          |
+-------------------------------------------------------+-----------------------+
| :samp:`chdir(PATH)`                                   | changes the current   |
|                                                       | working directory     |
+-------------------------------------------------------+-----------------------+

.. [1] The ``raising`` :term:`parameter` tells pytest whether an exception
       should be thrown if the element is not (yet) present.
.. [2] The ``prepend`` :term:`parameter` of ``setenv()`` can be a character. If
       it is set, the value of the environment variable is changed to
       :samp:`{VALUE} + prepend + {OLD_VALUE}`

We can use ``monkeypatch`` to redirect the :abbr:`CLI (Command Line Interface)`
to a temporary directory for the database in two ways. Both methods require
knowledge of the application code. Let’s take a look at the method
``cli.get_path()`` in :file:`src/items/cli.py`:

.. code-block:: python

   import os
   import pathlib


   def get_path():
       db_path_env = os.getenv("ITEMS_DB_DIR", "")
       if db_path_env:
           db_path = pathlib.Path(db_path_env)
       else:
           db_path = pathlib.Path.home() / "items_db"
       return db_path

This method tells the rest of the CLI code where the database is located. To
display the location of the database on the command line, we now also define
``config()`` in :file:`src/items/cli.py`:

.. code-block:: python

   @app.command()
   def config():
       """Return the path to the Items db."""
       with items_db() as db:
           print(db.path())

.. code-block:: console

   $ items config
   /Users/veit/items_db

To test these methods, we can now patch either the entire ``get_path()``
function or the ``pathlib.Path()`` attribute ``home``. To do this, we first
define an auxiliary function ``run_items_cli`` in :file:`tests/test_config.py`,
which outputs the same as ``items`` on the command line:

.. code-block:: python

   from typer.testing import CliRunner

   import items


   def run_items_cli(*params):
       runner = CliRunner()
       result = runner.invoke(items.app, params)
       return result.output.rstrip()

We can then write our test, which patches the entire ``get_path()`` function:

.. code-block:: python

   def test_get_path(monkeypatch, tmp_path):
       def fake_get_path():
           return tmp_path

       monkeypatch.setattr(items.cli, "get_path", fake_get_path)
       assert run_items_cli("config") == str(tmp_path)

The ``get_path()`` function from ``items.cli`` cannot simply be replaced by
``tmp_path``, as this is a ``pathlib.Path`` object that cannot be called. It is
therefore replaced by the ``fake_get_path()`` function. Alternatively, however,
we can also patch the home attribute of ``pathlib.Path``:

.. code-block:: python

   def test_home(monkeypatch, tmp_path):
       items_dir = tmp_path / "items_db"

       def fake_home():
           return tmp_path

       monkeypatch.setattr(items.cli.pathlib.Path, "home", fake_home)
       assert run_items_cli("config") == str(items_dir)

However, *monkey patching* and *mocking* complicate testing, so we will look for
ways to avoid this whenever possible. In our case, it might be useful to set an
environment variable :envvar:`ITEMS_DB_DIR` that can be easily patched:

.. code-block:: python

   def test_env_var(monkeypatch, tmp_path):
       monkeypatch.setenv("ITEMS_DB_DIR", str(tmp_path))
       assert run_items_cli("config") == str(tmp_path)

Remaining built-in fixtures
---------------------------

+-------------------------------+-----------------------------------------------+
| Built-in fixture              | Description                                   |
+===============================+===============================================+
| ``capfd``,                    | Variants of ``capsys`` that work with file    |
| ``capfdbinary``,              | descriptors and/or binary output.             |
| ``capsysbinary``              |                                               |
+-------------------------------+-----------------------------------------------+
| ``caplog``                    | similar to ``capsys``; used for messages      |
|                               | created with Python’s logging system.         |
+-------------------------------+-----------------------------------------------+
| ``cache``                     | is used to store and retrieve values across   |
|                               | multiple Pytest runs.                         |
|                               |                                               |
|                               | It allows ``last-failed``, ``failed-first``   |
|                               | and similar options.                          |
+-------------------------------+-----------------------------------------------+
| ``doctest_namespace``         | useful if you want to use pytest to perform   |
|                               | :doc:`doctests <../../document/doctest>`.     |
+-------------------------------+-----------------------------------------------+
| ``pytestconfig``              | is used to get access to configuration values,|
|                               | plugin managers and hooks.                    |
+-------------------------------+-----------------------------------------------+
| ``record_property``,          | is used to add additional properties to the   |
| ``record_testsuite_property`` | test or test suite.                           |
|                               |                                               |
|                               | Especially useful for adding data to a report |
|                               | used by :abbr:`CI (Continuous Integration)`   |
|                               | tools.                                        |
+-------------------------------+-----------------------------------------------+
| ``recwarn``                   | is used to test warning messages.             |
+-------------------------------+-----------------------------------------------+
| ``request``                   | is used to provide information about the      |
|                               | executed test function.                       |
|                               |                                               |
|                               | is mostly used in the :term:`parameterisation |
|                               | <Parameter>` fixtures.                        |
+-------------------------------+-----------------------------------------------+
| ``pytester``, ``testdir``     | Used to provide a temporary test directory to |
|                               | support the execution and testing of pytest   |
|                               | plugins. ``pytester`` is the ``pathlib`` based|
|                               | replacement for the ``py.path`` based         |
|                               | ``testdir``.                                  |
+-------------------------------+-----------------------------------------------+
| ``tmpdir``,                   | similar to ``tmp_path`` and                   |
| ``tmpdir_factory``            | ``tmp_path_factory``; used to return a        |
|                               | ``py.path.local`` object instead of a         |
|                               | ``pathlib.Path`` object.                      |
+-------------------------------+-----------------------------------------------+

You can get the complete list of built-in fixtures by running ``pytest
--fixtures``.

.. seealso::
   * `Built-in fixtures
     <https://docs.pytest.org/en/latest/reference/fixtures.html#built-in-fixtures>`_
