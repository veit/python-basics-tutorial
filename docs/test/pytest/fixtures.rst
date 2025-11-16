Test fixtures
=============

Now that you have used pytest to write and execute test functions, let’s move on
to :term:`fixtures <Test Fixture>`, which are essential for structuring test
code for almost any non-trivial software system. Fixtures are functions that are
executed by pytest before (and sometimes after) the actual test functions. The
code in the fixture can do whatever you want. You can use fixtures to get a data
set for the tests to work with. You can use fixtures to put a system into a
known state before a test is executed. Fixtures are also used to provide data
for multiple tests.

In this chapter, you will learn how to create and work with fixtures. You will
learn how to structure fixtures to store both setup and teardown code. You will
use ``scope`` to run fixtures once across many tests and learn how tests can use
multiple fixtures. You will also learn how to track code execution through
fixtures and test code.

But before you familiarise yourself with fixtures and use them to test Items,
let’s take a look at a small example fixture and learn how fixtures and test
functions are connected.

.. seealso::
   * `pytest fixtures <https://docs.pytest.org/en/latest/explanation/fixtures.html>`_
   * `pytest fixtures reference
     <https://docs.pytest.org/en/latest/reference/fixtures.html>`_
   * `How to use fixtures
     <https://docs.pytest.org/en/latest/how-to/fixtures.html#how-to-fixtures>`_

First steps with fixtures
-------------------------

Here is a simple fixture that returns a number:

.. code-block:: python

    import pytest


    @pytest.fixture()
    def some_data():
        """The answer to the ultimate question"""
        return 42


    def test_some_data(some_data):
        """Use fixture return value in a test."""
        assert some_data == 42

The ``@pytest.fixture()`` :doc:`decorator </functions/decorators>` is used to
tell pytest that a function is a fixture. If you include the fixture name in the
:term:`parameter` list of a test function, pytest knows that the function should
be executed before the test is run. Fixtures can perform work and also return
data to the test function. In this case, ``@pytest.fixture()`` decorates the
function :func:`some_data`. The test :func:`test_some_data` has the name of the
fixture, :func:`some_data` as a parameter. pytest recognises this and searches
for a fixture with this name.

Test fixtures in pytest refer to the mechanism that allows the separation of
preparation for and cleanup after code from your test functions. pytest handles
exceptions during fixtures differently than during a test function. An
``Exception`` or an ``assert`` error or a :func:`pytest.fail` call that occurs
during the actual test code leads to a ``Fail`` result. During a fixture,
however, the test function is reported as an error. This distinction is helpful
when troubleshooting if a test has failed. If a test ends with a fail, the error
is somewhere in the test function; if a test ends with an error, the error is
somewhere in a fixture.

.. _setup-and-teardown-fixtures:

Using fixtures for setup and teardown
-------------------------------------

Fixtures will be a great help when testing the Items application. The Items
application consists of an API that does most of the work and logic, a lean
:abbr:`CLI (Command Line Interface)` and a database. Handling the database is an
area where fixtures will be of great help:

.. code-block:: python

    from pathlib import Path
    from tempfile import TemporaryDirectory

    import items


    def test_empty():
        with TemporaryDirectory() as db_dir:
            db_path = Path(db_dir)
            db = items.ItemsDB(db_path)
            count = db.count()
            db.close()
            assert count == 0

To be able to call :func:`count`, we need a database object, which we obtain by
calling :func:`items.ItemsDB(db_path)`. The :func:`items.ItemsDB` function
returns an ``ItemsDB`` object. The :term:`parameter` ``db_path`` must be a
``pathlib.Path`` object that points to the database directory. For testing, a
temporary directory that we obtain with :func:`tempfile.TemporaryDirectory`
works.

However, this test function contains some problems: The code to set up the
database before we call :func:`count` is not really what we want to test. Also,
the ``assert`` statement cannot be done before calling :func:`db.close`, because
if the ``assert`` statement fails, the database connection will no longer be
closed. These problems can be solved with pytest fixture:

.. code-block:: python

    import pytest


    @pytest.fixture()
    def items_db():
        with TemporaryDirectory() as db_dir:
            db_path = Path(db_dir)
            db = items.ItemsDB(db_path)
            yield db
            db.close()


    def test_empty(items_db):
        assert items_db.count() == 0

The test function itself is now much easier to read, as we have outsourced the
entire database initialisation to a fixture called ``items_db``. The
``items_db`` fixture prepares the test by providing the database and then
outputting the database object. Only then is the test executed. And only after
the test has run is the database closed again.

Fixture functions are executed before the tests that use them. If there is a
``yield`` in the function, it stops there, passes control to the tests and
continues in the next line after the tests have been completed. The code above
the ``yield`` is setup and the code after the ``yield`` is teardown. The
teardown is guaranteed to be executed regardless of what happens during the
tests.

In our example, ``yield`` takes place within a context manager with a temporary
directory. This directory remains in place while the fixture is in use and the
tests are running. At the end of the test, control is passed back to the
fixture, :func:`db.close` can be executed and the ``with`` block can close
access to the directory.

We can also use fixtures in several tests, for example in

.. code-block:: python

    def test_count(items_db):
        items_db.add_item(items.Item("something"))
        items_db.add_item(items.Item("something else"))
        assert items_db.count() == 2

:func:`test_count` uses the same ``items_db`` fixture. This time we take the
empty database and add two items before checking the count. We can now use
``items_db`` for any test that requires a configured database. The individual
tests, such as :func:`test_empty` and :func:`test_count`, can be kept smaller
and focus on what we really want to test, rather than setup and teardown.

Show fixture execution with ``--setup-show``
--------------------------------------------

Now that we have two tests using the same fixture, it would be interesting to
know in which order they are called. pytest offers the command line option
``--setup-show``, which shows us the order of operations of tests and fixtures,
including the setup and teardown phases of the fixtures:

.. code-block:: pytest

    $ pytest --setup-show tests/test_count.py
    ============================= test session starts ==============================
    …
    collected 2 items

    tests/test_count.py
            SETUP    F items_db
            tests/test_count.py::test_empty (fixtures used: items_db).
            TEARDOWN F items_db
            SETUP    F items_db
            tests/test_count.py::test_count (fixtures used: items_db).
            TEARDOWN F items_db

    ============================== 2 passed in 0.01s ===============================

We can see that our test is running, surrounded by the ``SETUP`` and
``TEARDOWN`` parts of the ``items_db`` fixture. The ``F`` in front of the
fixture name indicates that the fixture is using the function scope, meaning
that the fixture is called before each test function it uses, and then
dismantled afterwards. Next, let’s take a look at the functional scope.

Defining the scope of a fixture
-------------------------------

Each fixture has a specific scope, which determines the order of execution of
setup and teardown in relation to the execution of all test functions that use
the fixture. The scope determines how often setup and teardown are executed when
they are used by multiple test functions.

However, if setting up and connecting to the database or creating large data
sets is time-consuming, you may not want to do this for every single test. We
can change a range so that the slow part only happens once for multiple tests.
Let’s change the scope of our fixture so that the database is only opened once
by adding ``scope="module"`` to the fixture decorator:

.. code-block:: python

    @pytest.fixture(scope="module")
    def items_db():
        with TemporaryDirectory() as db_dir:
            db_path = Path(db_dir)
            db = items.ItemsDB(db_path)
            yield db
            db.close()

.. code-block:: pytest

    $ pytest --setup-show tests/test_count.py
    ============================= test session starts ==============================
    …
    collected 2 items

    tests/test_count.py
        SETUP    M items_db
            tests/test_count.py::test_empty (fixtures used: items_db).
            tests/test_count.py::test_count (fixtures used: items_db).
        TEARDOWN M items_db

    ============================== 2 passed in 0.01s ===============================

We have saved this setup time for the second test function. By changing the
module scope, any test in this module that uses the ``items_db`` fixture can use
the same instance of it without incurring additional setup and teardown time.

However, the fixture :term:`parameter` ``scope`` allows for more than just
``module``:

+-----------------------+-----------------------------------------------+
| ``scope`` values      | Description                                   |
+=======================+===============================================+
| ``scope='function'``  | Default value. Is executed once per test      |
|                       | function.                                     |
+-----------------------+-----------------------------------------------+
| ``scope='class'``     | Executed once per test class, regardless of   |
|                       | how many test methods the class contains.     |
+-----------------------+-----------------------------------------------+
| ``scope='module'``    | Executed once per module, regardless of how   |
|                       | ny test functions or methods or other         |
|                       | fixtures in the module use it.                |
+-----------------------+-----------------------------------------------+
| ``scope='package'``   | Executed once per package or test directory,  |
|                       | regardless of how many test functions or      |
|                       | methods or other fixtures are used in the     |
|                       | package.                                      |
+-----------------------+-----------------------------------------------+
| ``scope='session'``   | Executed once per session. All test methods   |
|                       | and functions that use a fixture with session |
|                       | scope share a call for setup and teardown.    |
+-----------------------+-----------------------------------------------+

The scope is therefore determined when a fixture is defined and not at the point
at which it is called. The test functions that use a fixture do not control how
often a fixture is set up and dismantled.

For a fixture defined within a test module, the session and package scopes
behave exactly like the module scopes. To be able to use these other scopes, we
need to use a :file:`conftest.py` file.

Sharing fixtures with :file:`conftest.py`
-----------------------------------------

You can insert fixtures into individual test files, but to share fixtures across
multiple test files, you must use a :file:`conftest.py` file either in the same
directory as the test file that uses it or in a parent directory. The
:file:`conftest.py` file is optional. It is considered a local plugin by pytest
and can contain hook functions and fixtures. Let’s start by moving the
``items_db`` fixture from :file:`test_count.py` to a :file:`conftest.py` file in
the same directory:

.. code-block:: python

    from pathlib import Path
    from tempfile import TemporaryDirectory

    import pytest

    import items


    @pytest.fixture(scope="session")
    def items_db():
        """ItemsDB object connected to a temporary database"""
        with TemporaryDirectory() as db_dir:
            db_path = Path(db_dir)
            db = items.ItemsDB(db_path)
            yield db
            db.close()

.. note::
   Fixtures can only depend on other fixtures in the same or a larger area. A
   fixture with a function scope can therefore depend on other fixtures with a
   function scope. A function scope fixture can also depend on ``class``,
   ``module`` and ``session`` scope fixtures, but not vice versa.

.. warning::
   Although :file:`conftest.py` is a Python module, it should not be imported
   from test files. The :file:`conftest.py` file is automatically read by
   pytest, so you do not need to import ``conftest`` anywhere.

Find where fixtures are defined
-------------------------------

We have moved a fixture from the test module to a :file:`conftest.py` file. We
can have :file:`conftest.py` files at really any level of our test directory.
The tests can use any fixture that is in the same test module as a test
function, or in a :file:`conftest.py` file in the same directory, or at any
level of the parent directory up to the root of the tests.

This creates a problem if you can’t remember where a particular fixture is
located and you want to see the source code. With ``pytest --fixtures`` we can
display where the fixtures are defined:

.. code-block:: pytest

    pytest --fixtures
    ============================= test session starts ==============================
    …
    collected 10 items
    cache -- .../_pytest/cacheprovider.py:532
        Return a cache object that can persist state between testing sessions.
    …
    tmp_path_factory [session scope] -- .../_pytest/tmpdir.py:245
        Return a :class:`pytest.TempPathFactory` instance for the test session.

    tmp_path -- .../_pytest/tmpdir.py:260
        Return a temporary directory path object which is unique to each test
        function invocation, created as a sub directory of the base temporary
        directory.


    --------------------- fixtures defined from tests.conftest ---------------------
    items_db [session scope] -- conftest.py:10
        ItemsDB object connected to a temporary database


    ------------------ fixtures defined from tests.test_fixtures -------------------
    some_data -- test_fixtures.py:5
        The answer to the ultimate question


    ============================ no tests ran in 0.00s =============================

pytest shows us a list of all available fixtures that our test can use. This
list contains a number of built-in fixtures, which we will look at in
:doc:`builtin-fixtures`, as well as fixtures provided by :doc:`plugins`. The
fixtures found in :file:`conftest.py` files are at the end of the list. If you
specify a directory, pytest will list the fixtures that are available for tests
in that directory. If you specify the name of a test file, pytest also includes
the fixtures defined in the test modules.

The output of pytest contains

* the first line of the docstring of the fixture; by adding ``-v``, the entire
  docstring is included
* the file and line number in which the fixture is defined
* the path if the fixture is not in the current directory

.. note::
   We have to use ``-v`` for pytest 6.x to get the path and the line numbers.
   Only from pytest 7 onwards will these be added without any further option.

You can also use ``--fixtures-per-test`` to see which fixtures are used by each
test and where the fixtures are defined:

.. code-block:: pytest

    pytest --fixtures-per-test test_count.py::test_empty
    ============================= test session starts ==============================
    …
    collected 1 item

    ------------------------- fixtures used by test_empty --------------------------
    ------------------------------ (test_count.py:5) -------------------------------
    items_db -- conftest.py:10
        ItemsDB object connected to a temporary database

    ============================ no tests ran in 0.00s =============================

In this example, we have specified a single test: ``test_count.py::test_empty``.
However, files or directories can also be specified.

Using multiple fixture levels
-----------------------------

Our test code is still problematic at the moment, as both tests depend on the
database being empty at the beginning. This problem becomes very clear when we
add a third test:

.. code-block:: pytest

    $ pytest test_count.py::test_count2
    ============================= test session starts ==============================
    …
    collected 1 item

    test_count.py .                                                          [100%]

    ============================== 1 passed in 0.00s ===============================

It works when executed individually, but not when executed after
``test_count.py::test_count``:

.. code-block:: pytest

    $ pytest test_count.py
    ============================= test session starts ==============================
    …
    collected 3 items

    test_count.py ..F                                                        [100%]

    =================================== FAILURES ===================================
    _________________________________ test_count2 __________________________________

    items_db = <items.api.ItemsDB object at 0x103d3a390>

        def test_count2(items_db):
            items_db.add_item(items.Item("something different"))
    >       assert items_db.count() == 1
    E       assert 3 == 1
    E        +  where 3 = <bound method ItemsDB.count of <items.api.ItemsDB object at 0x103d3a390>>()
    E        +    where <bound method ItemsDB.count of <items.api.ItemsDB object at 0x103d3a390>> = <items.api.ItemsDB object at 0x103d3a390>.count

    test_count.py:15: AssertionError
    =========================== short test summary info ============================
    FAILED test_count.py::test_count2 - assert 3 == 1
    ========================= 1 failed, 2 passed in 0.03s ==========================

There are three items in the database because the previous test already added
two items before ``test_count2`` was executed. However, tests should not rely on
the order of execution. ``test_count2`` only succeeds if it is executed alone,
but fails if it is executed after ``test_count``.

If we still want to try to work with an open database but start all tests with
zero items in the database, we can do this by adding another fixture in
:file:`conftest.py`:

.. code-block:: python

    @pytest.fixture(scope="session")
    def db():
        """ItemsDB object connected to a temporary database"""
        with TemporaryDirectory() as db_dir:
            db_path = Path(db_dir)
            db_ = items.ItemsDB(db_path)
            yield db_
            db_.close()


    @pytest.fixture(scope="function")
    def items_db(db):
        """ItemsDB object that's empty"""
        db.delete_all()
        return db

I have renamed the old ``items_db`` to ``db`` and moved it to the session area.

The ``items_db`` fixture has ``db`` in its :term:`parameter` list, which means
that it depends on the ``db`` fixture. In addition, ``items_db`` is
``function``-orientated, which is a narrower scope than ``db``. If fixtures
depend on other fixtures, they can only use fixtures that have the same or a
larger scope.

Let’s see if it works:

.. code-block:: pytest

    $ pytest --setup-show test_count.py
    ============================= test session starts ==============================
    …
    collected 3 items

    test_count.py
    SETUP    S db
            SETUP    F items_db (fixtures used: db)
            test_count.py::test_empty (fixtures used: db, items_db).
            TEARDOWN F items_db
            SETUP    F items_db (fixtures used: db)
            test_count.py::test_count (fixtures used: db, items_db).
            TEARDOWN F items_db
            SETUP    F items_db (fixtures used: db)
            test_count.py::test_count2 (fixtures used: db, items_db).
            TEARDOWN F items_db
    TEARDOWN S db

    ============================== 3 passed in 0.00s ===============================

We see that the setup for ``db`` is done first and has the scope of the session
(from the ``S``). The setup for ``items_db`` happens next and before each test
function call and has the scope of the function (from the ``F``). In addition,
all three tests are passed.

Using fixtures for multiple stages can provide incredible speed advantages and
maintain test order independence.

Using multiple fixtures per test or fixture
-------------------------------------------

Another way to use multiple fixtures is to use more than one in a function or
fixture. For example, we can put some pre-planned items together to test them in
one fixture:

.. code-block:: python

    @pytest.fixture(scope="session")
    def items_list():
        """List of different Item objects"""
        return [
            items.Item("Add Python 3.12 static type improvements", "veit", "todo"),
            items.Item("Add tips for efficient testing", "veit", "wip"),
            items.Item("Update cibuildwheel section", "veit", "done"),
            items.Item("Add backend examples", "veit", "done"),
        ]

Then we can use both ``empty_db`` and ``items_list`` in ``test_add.py``:

.. code-block:: python

    def test_add_list(items_db, items_list):
        expected_count = len(items_list)
        for i in items_list:
            items_db.add_item(i)
        assert items_db.count() == expected_count

And fixtures can also use several other fixtures:

.. code-block:: python

    @pytest.fixture(scope="function")
    def populated_db(items_db, items_list):
        """ItemsDB object populated with 'items_list'"""
        for i in items_list:
            items_db.add_item(i)
        return items_db

The fixture ``populated_db`` must be in the function area, as it uses
``items_db``, which is already in the ``function`` area. If you try to place
``populated_db`` in the ``module`` area or a larger area, pytest will issue an
error. Don't forget that if you don’t specify a range, you will get fixtures in
the ``function`` area. Tests that require a populated database can now simply do
this with

.. code-block:: python

    def populated(populated_db):
        assert populated_db.count() > 0

We have seen how different fixture scopes work and how different scopes can be
used in different fixtures. However, you may need to define a scope at runtime.
This is possible with dynamic scoping.

.. _dynamic-fixture-scope:

Set fixture scope dynamically
-----------------------------

Let’s assume we have set up the fixtures as they are now, with ``db`` in the
``session`` scope and ``items_db`` in the ``function`` scope. However, there is
now a risk that the ``items_db`` fixture is empty because it calls
:func:`delete_all`. We therefore want to create a way of setting up the database
completely for each test function by dynamically defining the scope of the
``db`` fixture at runtime. To do this, we first change the scope of ``db`` in
the :file:`conftest.py` file:

.. code-block:: python

    @pytest.fixture(scope=db_scope)
    def db():
        """ItemsDB object connected to a temporary database"""
        with TemporaryDirectory() as db_dir:
            db_path = Path(db_dir)
            db_ = items.ItemsDB(db_path)
            yield db_
            db_.close()

Instead of a specific scope, we have entered a function name: ``db_scope``. Now
we have to write this function:

.. code-block:: python

    def db_scope(fixture_name, config):
        if config.getoption("--fdb", None):
            return "function"
        return "session"

There are many ways in which we can find out which area we should use. In this
case, I decided to use a new command line option ``--fdb``. In order to use this
new option with pytest, we need to write a hook function in the
:file:`conftest.py` file, which I will explain in more detail in :doc:`plugins`:

.. code-block:: python

    def pytest_addoption(parser):
        parser.addoption(
            "--fdb",
            action="store_true",
            default=False,
            help="Create new db for each test",
        )

After all this, the default behaviour is the same as before, with ``db`` in the
``session`` scope:

.. code-block:: pytest

    $ pytest --setup-show test_count.py
    ============================= test session starts ==============================
    …
    collected 3 items

    test_count.py
    SETUP    S db
            SETUP    F items_db (fixtures used: db)
            test_count.py::test_empty (fixtures used: db, items_db).
            TEARDOWN F items_db
            SETUP    F items_db (fixtures used: db)
            test_count.py::test_count (fixtures used: db, items_db).
            TEARDOWN F items_db
            SETUP    F items_db (fixtures used: db)
            test_count.py::test_count2 (fixtures used: db, items_db).
            TEARDOWN F items_db
    TEARDOWN S db

    ============================== 3 passed in 0.00s ===============================

However, if we use the new option, we get a ``db`` fixture in the ``function``
scope:

.. code-block:: pytest

    $ pytest --fdb --setup-show test_count.py
    ============================= test session starts ==============================
    …
    collected 3 items

    test_count.py
            SETUP    F db
            SETUP    F items_db (fixtures used: db)
            test_count.py::test_empty (fixtures used: db, items_db).
            TEARDOWN F items_db
            TEARDOWN F db
            SETUP    F db
            SETUP    F items_db (fixtures used: db)
            test_count.py::test_count (fixtures used: db, items_db).
            TEARDOWN F items_db
            TEARDOWN F db
            SETUP    F db
            SETUP    F items_db (fixtures used: db)
            test_count.py::test_count2 (fixtures used: db, items_db).
            TEARDOWN F items_db
            TEARDOWN F db

    ============================== 3 passed in 0.00s ===============================

The database is now set up before each test function and then dismantled again.

.. seealso::
   * :doc:`command-line-options`

``autouse`` for fixtures that are always used
---------------------------------------------

Previously, all fixtures used by tests were named by the tests or another
fixture in a :term:`parameter` list. However, you can use ``autouse=True`` to
always run a fixture. This is good for code that needs to run at specific times,
but tests are not really dependent on a system state or data from the fixture,
for example:

.. code-block::

    import os


    @pytest.fixture(autouse=True, scope="session")
    def setup_test_env():
        found = os.environ.get("APP_ENV", "")
        os.environ["APP_ENV"] = "TESTING"
        yield
        os.environ["APP_ENV"] = found

.. code-block:: pytest

    pytest --setup-show test_count.py
    ============================= test session starts ==============================
    …
    collected 3 items

    test_count.py
    SETUP    S setup_test_env
    SETUP    S db
            SETUP    F items_db (fixtures used: db)
            test_count.py::test_empty (fixtures used: db, items_db, setup_test_env).
            TEARDOWN F items_db
            SETUP    F items_db (fixtures used: db)
            test_count.py::test_count (fixtures used: db, items_db, setup_test_env).
            TEARDOWN F items_db
            SETUP    F items_db (fixtures used: db)
            test_count.py::test_count2 (fixtures used: db, items_db, setup_test_env).
            TEARDOWN F items_db
    TEARDOWN S db
    TEARDOWN S setup_test_env

    ============================== 3 passed in 0.00s ===============================

.. tip::
   The ``autouse`` feature should be the exception rather than the rule. Opt for
   named fixtures unless you have a really good reason not to do so.

Rename fixtures
---------------

The name of a fixture listed in the :term:`parameter` list of tests and other
fixtures that use this fixture is normally the same as the function name of the
fixture. However, Pytest allows you to rename fixtures with the ``name``
parameter to ``@pytest.fixture()``:

.. code-block:: python

    import pytest


    from items import cli


    @pytest.fixture(scope="session", name="db")
    def _db():
        """The db object"""
        yield db()


    def test_empty(db):
        assert items_db.count() == 0

One case in which renaming can be useful is if the most obvious fixture name
already exists as a variable or function name.
