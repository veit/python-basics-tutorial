Command line options
====================

In :ref:`dynamic-fixture-scope`, we have already seen how the fixture scope can
be changed using a command line option. Now let’s take a closer look at the
command line options.

Passing different values to a test function
-------------------------------------------

Suppose you want to write a test that depends on a command line option. You can
achieve this using the following pattern:

.. code-block:: python
   :caption: test_example.py

   def test_db(items_db, db_path, cmdopt):
       if cmdopt == "json":
           print("Save as JSON file")
       elif cmdopt == "sqlite":
           print("Save in a SQLite database")
       assert items_db.path() == db_path

For this to work, the command line option must be added and ``cmdopt`` must be
provided via a fixture function:

.. code-block:: python
   :caption: conftest.py

   import pytest


   def pytest_addoption(parser):
       parser.addoption(
           "--cmdopt",
           action="store",
           default="json",
           help="Store data as JSON file or in a SQLite database",
       )


   @pytest.fixture
   def cmdopt(request):
       return request.config.getoption("--cmdopt")

You can then call up your tests, for example, with:

.. code-block:: console

   $ pytest --sqlite

In addition, you can add a simple validation of the input by listing the
options:

.. code-block:: python
   :caption: conftest.py
   :emphasize-lines: 7

   def pytest_addoption(parser):
       parser.addoption(
           "--cmdopt",
           action="store",
           default="json",
           help="Store data as JSON file or in a SQLite database",
           choices=("json", "sqlite"),
       )

This is how we receive feedback on an incorrect argument:

.. code-block:: console

   $ pytest --postgresql
   ERROR: usage: pytest [options] [file_or_dir] [file_or_dir] [...]
   pytest: error: argument --cmdopt: invalid choice: 'postgresql' (choose from json, sqlite)

If you want to provide more detailed error messages, you can use the ``type``
parameter and raise ``pytest.UsageError``:

.. code-block:: python
   :caption: conftest.py
   :emphasize-lines: -6, 15

   def type_checker(value):
       msg = "cmdopt must specify json or sqlite"
       if not value.startswith("json" or "sqlite"):
           raise pytest.UsageError(msg)

       return value


   def pytest_addoption(parser):
       parser.addoption(
           "--cmdopt",
           action="store",
           default="json",
           help="Store data as JSON file or in a SQLite database",
           type=type_checker,
       )

However, command line options often need to be processed outside of the test and
more complex objects need to be passed.

Adding command line options dynamically
---------------------------------------

With :ref:`addopts`, you can add static command line options to your project.
However, you can also change the command line arguments dynamically before they
are processed:

.. code-block:: python
   :caption: conftest.py

   import sys


   def pytest_load_initial_conftests(args):
       if "xdist" in sys.modules:
           import multiprocessing

           num = max(multiprocessing.cpu_count() / 2, 1)
           args[:] = ["-n", str(num)] + args

If you have installed the :ref:`xdist-plugin` plugin, test runs will always be
performed with a number of subprocesses close to your CPU.

Command line option for skipping tests
--------------------------------------

Below, we add a :file:`conftest.py` file with a command line option
``--runslow`` to control the skipping of tests marked with ``pytest.mark.slow``:

.. code-block:: python
   :caption: conftest.py

   import pytest


   def pytest_addoption(parser):
       parser.addoption(
           "--runslow", action="store_true", default=False, help="run slow tests"
       )


   def pytest_collection_modifyitems(config, items):
       if config.getoption("--runslow"):
           # If --runslow is specified on the CLI, slow tests are not skipped.
           return
       skip_slow = pytest.mark.skip(reason="need --runslow option to run")
       for item in items:
           if "slow" in item.keywords:
               item.add_marker(skip_slow)

If we now write a test with the ``@pytest.mark.slow`` decorator, a skipped
‘slow’ test will be displayed when pytest is called:

.. code-block:: pytest

   $ uv run pytest
   ============================= test session starts ==============================
   ...
   test_example.py s.                                                         [100%]

   =========================== short test summary info ============================
   SKIPPED [1] test_example.py:8: need --runslow option to run
   ========================= 1 passed, 1 skipped in 0.05s =========================

Extend test report header
-------------------------

Additional information can be easily provided in a ``pytest -v`` run:

.. code-block:: python
   :caption: conftest.py

   import sys


   def pytest_report_header(config):
       gil = sys._is_gil_enabled()
       return f"Is GIL enabled? {gil}"


.. code-block:: pytest
   :emphasize-lines: 5

   $ uv run pytest -v
   ============================= test session starts ==============================
   platform darwin -- Python 3.14.0b4, pytest-8.4.1, pluggy-1.6.0
   cachedir: .pytest_cache
   Is GIL enabled? False
   rootdir: /Users/veit/sandbox/items
   configfile: pyproject.toml
   plugins: anyio-4.9.0, Faker-37.4.0, cov-6.2.1
   ...
   ============================== 2 passed in 0.04s ===============================

Determine test duration
-----------------------

If you have a large test suite that runs slowly, you will probably want to use
``-vv --durations`` to find out which tests are the slowest.

.. code-block:: pytest

   $ uv run pytest -vv --durations=3
   ============================= test session starts ==============================
   ...
   ============================= slowest 3 durations ==============================
   0.02s setup    tests/api/test_add.py::test_add_from_empty
   0.00s call     tests/cli/test_help.py::test_help[add]
   0.00s call     tests/cli/test_help.py::test_help[update]
   ============================== 83 passed in 0.17s ==============================
