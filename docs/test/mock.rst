Mock
====

In this chapter, we will test the :abbr:`CLI (Command Line Interface)`. For this,
we will use the :doc:`mock <python3:library/unittest.mock>` package, which has
been delivered as part of the Python standard library under the name
``unittest.mock`` since Python 3.3. For older versions of Python, you can install
it with :

.. tab:: Linux/macOS

   .. code-block:: console

      $ . .venv/bin/activate
      $ python -m pip install mock

.. tab:: Windows

   .. code-block:: ps1con

      C:> Scripts\activate.bat
      C:> python -m pip install mock

:term:`Mock` objects are sometimes also referred to as test doubles,
:term:`fakes <Fake>` or :term:`stubs <Stubs>`. With pytest’s own monkeypatch
fixture and mock, you should have all the functions you need.

Example
-------

Firstly, we wanted to start with a simple example and check whether the working
days from Monday to Friday are determined correctly.

#. We import ``datetime.datetime`` and ``Mock``:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 1-2
      :lineno-start: 1

#. Then we define two test days:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 5-6
      :lineno-start: 5

#. Now we define a method for checking the working days, whereby the Python
   datetime library treats Mondays as ``0`` and Sundays as ``6``:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 9-11
      :lineno-start: 9

#. Then we mock datetime:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 14
      :lineno-start: 14

#. Finally, we test our two mock objects:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 17-19
      :lineno-start: 17

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 21-23
      :lineno-start: 21

Testing with Typer
------------------

For testing the Items CLI, we will also look at how the ``CliRunner`` provided by
`Typer <https://typer.tiangolo.com>`_ helps with testing. Typer provides a test
interface that allows us to call our application without having to rely on
:func:`python3:subprocess.run` as in the short :ref:`capsys-fixture` example.
This is good because we cannot simulate what is running in a separate process. So
in :file:`tests/cli/conftest.py` we can just pass our application
``items.cli.app`` and a list of strings representing the command to the
:func:`invoke` function of our ``runner``: more precisely, we use
:func:`shlex.split(command_string)` to convert the commands, for example
:samp:`list -o "veit"` into :samp:`["list", "-o", "veit"]` and can then
intercept and return the output.

.. code-block:: python
   :emphasize-lines: 4, 8, 16-17

   import shlex

   import pytest
   from typer.testing import CliRunner

   import items

   runner = CliRunner()


   @pytest.fixture()
   def items_cli(db_path, monkeypatch, items_db):
       monkeypatch.setenv("ITEMS_DB_DIR", db_path.as_posix())

       def run_cli(command_string):
           command_list = shlex.split(command_string)
           result = runner.invoke(items.cli.app, command_list)
           output = result.stdout.rstrip()
           return output

       return run_cli

We can then simply use this fixture to test the version in
:file:`tests/cli/test_version.py`, for example:

.. code-block:: python

   import items


   def test_version(items_cli):
       assert items_cli("version") == items.__version__

.. seealso::
   `Typer Learn Testing <https://typer.tiangolo.com/tutorial/testing/>`_

Mocking of attributes
---------------------

Let’s take a look at how we can use mocking to ensure that, for example,
three-digit version numbers of :func:`items.__version__` are also output
correctly via the CLI. For this we will use :func:`mock.patch.object` as a
context manager:

.. code-block:: python
   :emphasize-lines: 1, 7

   from unittest import mock

   import items


   def test_mock_version(items_cli):
       with mock.patch.object(items, "__version__", "100.0.0"):
           assert items_cli("version") == items.__version__

In our test code, we import ``items``. The resulting items object is what we
will patch. The call to :func:`mock.patch.object`, which is used as a
:doc:`context manager <../control-flow/with>` within a ``with`` block, returns a
mock object that is cleaned up after the ``with`` block:

#. In this case, the ``__version__`` attribute of ``items`` is replaced with
   ``"100.0.0"`` for the duration of the ``with`` block.
#. We then use :func:`items_cli` to call our CLI application with the
   ``"version"`` command. However, when the :func:`version` method is called,
   the ``__version__`` attribute is not the original string, but the string we
   replaced with :func:`mock.patch.object`.

Mocking classes and methods
---------------------------

In :file:`src/items/cli.py` we have defined :func:`config` as follows:

.. code-block:: python

   def config():
       """List the path to the Items db."""
       with items_db() as db:
           print(db.path())

:func:`items_db` is a :doc:`context manager <../control-flow/with>` that returns
an ``items.ItemsDB`` object. The returned object is then used as a ``db`` to
call :func:`db.path`. So we should mock two things here: ``items.ItemsDB`` and
one of its methods, :func:`path`. Let’s start with the class:

.. code-block:: python

   from unittest import mock

   import items


   def test_mock_itemsdb(items_cli):
       with mock.patch.object(items, "ItemsDB") as MockItemsDB:
           mock_db_path = MockItemsDB.return_value.path.return_value = "/foo/"
           assert items_cli("config") == str(mock_db_path)

Let's make sure that it really works:

.. code-block:: pytest

   $ pytest -v -s tests/cli/test_config.py::test_mock_itemsdb
   ============================= test session starts ==============================
   ...
   configfile: pyproject.toml
   plugins: cov-4.1.0, Faker-19.11.0
   collected 1 item

   tests/cli/test_config.py::test_mock_itemsdb PASSED

   ============================== 1 passed in 0.04s ===============================

Great, now we just have to move the mock for the database to a fixture, because
we will need it in many test methods:

.. code-block:: python

   @pytest.fixture()
   def mock_itemsdb():
       with mock.patch.object(items="ItemsDB") as MockItemsDB:
           yield MockItemsDB.return_value

This fixture mocks the ``ItemsDB`` object and returns the ``return_value`` so
that tests can use it to replace things like ``path``:

.. code-block:: python

   def test_mock_itemsdb(items_cli, mock_itemsdb):
       mock_itemsdb.path.return_value = "/foo/"
       result = runner.invoke(app, ["config"])
       assert result.stdout.rstrip() == "/foo/"

Alternatively, the :func:`@mock.patch` decorator can also be used to mock
classes or objects. In the following examples, the output of ``os.listdir`` is
mocked. This does not require ``db_path`` to be present in the file system:

.. code-block:: python

   import os
   from unittest import mock


   @mock.patch("os.listdir", mock.MagicMock(return_value="db_path"))
   def test_listdir():
       assert "db_path" == os.listdir()

Another alternative is to define the return value separately:

.. code-block:: python

   @mock.patch("os.listdir")
   def test_listdir(mock_listdir):
       mock_listdir.return_value = "db_path"
       assert "db_path" == os.listdir()

Synchronising mocks with ``autospec``
-------------------------------------

Mock objects are usually intended as objects that are used instead of the real
implementation. By default, however, they will accept any access. For example, if
the real object allows :func:`start(index)`, our mock objects should also allow
:func:`start(index)`. However, there is a problem with this. Mock objects are
too flexible by default: they would also accept :func:`stort` or other
misspelled, renamed or deleted methods or :term:`parameters <Parameter>`. Over
time, this can lead to so-called mock drift if the interface you are modelling
changes, but your mock in your test code does not. This form of mock drift can
be solved by adding ``autospec=True`` to the mock during creation:

.. code-block:: python
   :emphasize-lines: 3

   @pytest.fixture()
   def mock_itemsdb():
       with mock.patch.object(items, "ItemsDB") as MockItemsDB:
           yield MockItemsDB.return_value

Usually, this protection is always built in with ``autospec``. The only exception
I know of is if the class or object being mocked has dynamic methods or if
attributes are added at runtime.

.. seealso::
   The Python documentation has a large section on ``autospec``:
   :ref:`python3:auto-speccing`.

Check call with :func:`assert_called_with`
------------------------------------------

So far, we have used the return values of a mocking method to ensure that our
application code handles the return values correctly. But sometimes there is no
useful return value, for example with :samp:`items add some tasks -o veit`. In
these cases, we can ask the mock object if it was called correctly. After calling
:func:`items_cli("add some tasks -o veit")`, the API is not used to check
whether the item has entered the database, but a mock is used to ensure that the
CLI has called the API method correctly. Finally, the implementation of the
:func:`add` function calls :func:`db.add_item` with an ``Item`` object:

.. _test_add_with_owner:

.. code-block:: python
   :emphasize-lines: 4

   def test_add_with_owner(mock_itemsdb, items_cli):
       items_cli("add some task -o veit")
       expected = items.Item("some task", owner="veit", state="todo")
       mock_itemsdb.add_item.assert_called_with(expected)

If :func:`add_item` is not called or is called with the wrong type or the wrong
object content, the test fails. For example, if we capitalise the string
``"Veit"`` in ``expected``, but not in the CLI call, we get the following output:

.. code-block:: pytest
   :emphasize-lines: 10-13, 16

   $ pytest -s tests/cli/test_add.py::test_add_with_owner
   ============================= test session starts ==============================
   ...
   configfile: pyproject.toml
   plugins: cov-4.1.0, Faker-19.11.0
   collected 1 item

   tests/cli/test_add.py F
   ...
   >           raise AssertionError(_error_message()) from cause
   E           AssertionError: expected call not found.
   E           Expected: add_item(Item(summary='some task', owner='Veit', state='todo', id=None))
   E           Actual: add_item(Item(summary='some task', owner='veit', state='todo', id=None))
   ...
   =========================== short test summary info ============================
   FAILED tests/cli/test_add.py::test_add_with_owner - AssertionError: expected call not found.
   ============================== 1 failed in 0.08s ===============================

.. seealso::
   There is a whole range of variants of :func:`assert_called`. A complete list
   and description can be found in `unittest.mock.Mock.assert_called
   <https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called>`_.

   If the only way to test is to ensure the correct call, the various assert_called*() methods fulfil their purpose.

   Wenn die einzige Möglichkeit zum Testen darin besteht, den korrekten Aufruf
   sicherzustellen, erfüllen die verschiedenen :func:`assert_called*`-Methoden
   ihren Zweck.

Create error conditions
-----------------------

Let’s now check if the Items CLI handles error conditions correctly. For example,
here is the implementation of the delete command:

.. code-block:: python

   @app.command()
   def delete(item_id: int):
       """Remove item in db with given id."""
       with items_db() as db:
           try:
               db.delete_item(item_id)
           except items.InvalidItemId:
               print(f"Error: Invalid item id {item_id}")

To test how the CLI handles an error condition, we can pretend that
:func:`delete_item` generates an exception by assigning the exception to the
`side_effect
<https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect>`_
attribute of the mock object, like this:

.. code-block:: python

   def test_delete_invalid(mock_itemsdb, items_cli):
       mock_itemsdb.delete_item.side_effect = items.api.InvalidItemId
       out = items_cli("delete 42")
       assert "Error: Invalid item id 42" in out

That’s all we need to test the CLI: mocking return values, checking calls to mock
functions and mocking exceptions. However, there is a whole range of other
mocking techniques that we have not covered. So be sure to read
:doc:`python3:library/unittest.mock` if you want to use mocking extensively.

Limitations of mocking
----------------------

One of the biggest problems with using mocks is that we are no longer testing the
behaviour in a test, but the implementation. However, this is not only
time-consuming but also dangerous: a valid refactoring, for example changing a
variable name, can cause tests to fail if that particular variable has been
mocked. However, we only want our tests to fail when there are breaks in
behaviour, not just when there are code changes.

However, sometimes mocking is the easiest way to create exceptions or error
conditions and make sure your code handles them correctly. There are also cases
where testing behaviour is unreasonable, such as when accessing a payment API or
sending emails. In these cases, a good option is to test whether your code calls
a specific API method at the right time and with the right :term:`parameters
<Parameter>`.

.. seealso::
   * Hynek Schlawack: `“Don’t Mock What You Don’t Own”
     <https://hynek.me/articles/what-to-mock-in-5-mins/>`_

Avoid mocking with tests on multiple levels
-------------------------------------------

We can also test the Items CLI without mocks by also using the API. We will not
test the API, but only use it to check the behaviour of actions that are executed
via the CLI. We can also test the :ref:`test_add_with_owner
<test_add_with_owner>` example as follows:

.. code-block:: python

   def test_add_with_owner(items_db, items_cli):
       items_cli("add some task -o veit")
       expected = items.Item("some task", owner="veit", state="todo")
       all = items_db.list_items()
       assert len(all) == 1
       assert all[0] == expected

Mocking tests the implementation of the command line interface and ensures that
an API call is made with certain :term:`parameters <Parameter>`. The
mixed-layer approach tests the behaviour to ensure that the result meets our
expectations. This approach is much less of a change detector and has a greater
chance of remaining valid during a refactoring. Interestingly, the tests are
also about twice as fast:

.. code-block:: pytest

   $ pytest -s tests/cli/test_add.py::test_add_with_owner
   ============================= test session starts ==============================
   ...
   configfile: pyproject.toml
   plugins: cov-4.1.0, Faker-19.11.0
   collected 1 item

   tests/cli/test_add.py .

   ============================== 1 passed in 0.03s ===============================

We could also avoid mocking in another way. We could test the behaviour
completely via the CLI. This might require parsing the output of the items list
to check the correct database content.

In the API, :func:`add_item` returns an index and provides a
:func:`get_item(index)` method to help with testing. Both methods are not
available in the CLI, but could be. We could perhaps add the ``items get index``
or ``items info index`` commands so we can retrieve an item instead of having to
use ``items list`` for everything. ``list`` also already supports filtering.
Maybe filtering by index would work instead of adding a new command. And we could
add an output to ``items add`` that says something like *Item added at index 3*.
These changes would fall into the *Design for Testability* category. They also
don’t seem to be deep interface interventions and perhaps should be considered in
future versions.

Plugins to support mocking
--------------------------

So far we have focussed on the direct use of :doc:`mock
<python3:library/unittest.mock>`. However, there are many plugins that help with
mocking, such as `pytest-mock <https://pypi.org/project/pytest-mock/>`_, which
provides a ``mocker`` fixture. One advantage is that the fixture cleans up after
itself, so you don’t need to use a ``with`` block like we did in our examples.

There are also some special mocking libraries:

- The following are suitable for mocking database accesses:

  - `pytest-postgresql <https://pypi.org/project/pytest-postgresql/>`_
  - `pytest-mongo <https://pypi.org/project/pytest-mongo/>`_
  - `pytest-mysql <https://pypi.org/project/pytest-mysql/>`_
  - `pytest-dynamodb <https://pypi.org/project/pytest-dynamodb/>`_.

- You can use `pytest-httpserver <https://pypi.org/project/pytest_httpserver/>`_
  to test HTTP servers.
- You can use `responses <https://pypi.org/project/responses/>`_ or `betamax
  <https://pypi.org/project/betamax/>`_ to mock `requests
  <https://pypi.org/project/requests/>`_.
- Other tools for different requirements are:

  - `pytest-rabbitmq <https://pypi.org/project/pytest-rabbitmq/>`_
  - `pytest-solr <https://pypi.org/project/pytest-solr/>`_
  - `pytest-elasticsearch <https://pypi.org/project/pytest-elasticsearch/>`_ and
    `pytest-redis <https://pypi.org/project/pytest-redis/>`_.
