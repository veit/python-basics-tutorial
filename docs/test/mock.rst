Mock
====

In this chapter, we will test the :abbr:`CLI (Command line interface)`. To do
this, we will use the :doc:`mock <python3:library/unittest.mock>` library, which
has been included as part of the standard Python library since Python 3.3 under
the name ``unittest.mock``.

Objects that are not real can be :term:`dummies <Dummy>`, :term:`fakes <Fake>`,
:term:`stubs <Stub>`, :term:`mocks <Mock>` or :term:`spies <Spy>`. They are all
known as test doubles. However, with pytest’s own :ref:`monkeypatch-fixture` and
:doc:`unittest.mock <python3:library/unittest.mock>`, you should have all the
functions you need.

The three core functionalities of :doc:`unittest.mock
<python3:library/unittest.mock>` are:

:class:`Mock <python3:unittest.mock.Mock>`
    The Mock class can be used to simulate any object.
:class:`MagickMock <python3:unittest.mock.MagicMock>`
    A subclass of Mock that contains all magic methods, for example ``__str__``,
    ``__len__``  and so on.
:func:`patch <python3:unittest.mock.patch>`-Methode
    An object is searched for within a specific module and replaced with another
    object.

Example
-------

First, we wanted to start with a simple example and check whether the working
days from Monday to Friday are determined correctly.

#. First, we import ``datetime.datetime`` and ``Mock``:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 1-2
      :lineno-start: 1

#. Let’s then define two test days:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 5-6
      :lineno-start: 5

#. Now let’s define a method to check for working days, bearing in mind that
   Python’s datetime library treats Mondays as ``0`` and Sundays as ``6``:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 9-11
      :lineno-start: 9

#. Then we'll mock datetime:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 14
      :lineno-start: 14

#. Finally, we test our two mock objects:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 17-21
      :lineno-start: 17

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 24-
      :lineno-start: 24

Testing with Typer
------------------

When testing the Tasks CLI, we will also look at how the ``CliRunner`` provided
by `Typer <https://typer.tiangolo.com>`_ helps with testing. Typer offers a
testing interface that allows us to invoke our application without having to
use :func:`python3:subprocess.run`, as in the brief :ref:`capsys-fixture`
example. This is useful because we cannot simulate what is running in a separate
process. So, in :file:`tests/cli/conftest.py`, we can simply pass our
application ``cusy.tasks.cli.app`` and a list of strings representing the
command to the :func:`invoke` function of our runner: more specifically, we use
:func:`shlex.split(command_string)` to split the commands, for example
:samp:`list -o "veit"` into :samp:`["list", "-o", "veit"]`, and can then capture
and return the output.

.. code-block:: python
   :emphasize-lines: 4, 8, 16-17

    import shlex

    import pytest
    from typer.testing import CliRunner

    from cusy import tasks

    runner = CliRunner()


    @pytest.fixture()
    def tasks_cli(db_path, monkeypatch, tasks_db):
        monkeypatch.setenv("ITEMS_DB_DIR", db_path.as_posix())

        def run_cli(command_string):
            command_list = shlex.split(command_string)
            result = runner.invoke(tasks.cli.app, command_list)
            output = result.stdout.rstrip()
            return output

        return run_cli

We can then simply use this fixture to test the version in
:file:`tests/cli/test_version.py`, for example:

.. code-block:: python

    from cusy import tasks


    def test_version(tasks_cli):
        assert tasks_cli("version") == tasks.__version__

.. seealso::
   `Typer Learn Testing <https://typer.tiangolo.com/tutorial/testing/>`_

Mocking attributes
------------------

Let’s look at how we can use mocking to ensure that, for example, three-digit
version numbers from :func:`tasks.__version__` are also output correctly via the
CLI. To do this, we’ll use :func:`mock.patch.object` as a context manager:

.. code-block:: python
   :emphasize-lines: 1, 7

    from unittest import mock

    from cusy import tasks


    def test_mock_version(tasks_cli):
        with mock.patch.object(tasks, "__version__", "100.0.0"):
            assert tasks_cli("version") == tasks.__version__

In our test code, we import ``tasks``. The resulting ``tasks`` object is what we
will be patching. The call to :func:`mock.patch.object`, used as a context
manager within a ``with`` block, returns a mock object that is cleaned up after
the ``with`` block:

#. In this case, the ``__version__`` attribute of ``tasks`` is replaced with
   ``"100.0.0"`` for the duration of the ``with`` block.
#. We then use :func:`tasks_cli` to run our CLI application with the ``version``
   command. However, when the :func:`version` method is called, the
   ``__version__`` attribute is not the original string, but the string we
   replaced it with using :func:`mock.patch.object`.

Mocking classes and methods
---------------------------

In :file:`src/cusy/tasks/cli.py`, we have defined :func:`config` as follows:

.. code-block:: python

    def config():
        """List the path to the Tasks db."""
        with tasks_db() as db:
            print(db.path())

:func:`tasks_db` is a :doc:`context manager <../control-flow/with>` that returns
a ``tasks.TasksDB`` object. The returned object is then used as ``db`` to call
:func:`db.path`. So here we need to mock two things: ``tasks.TasksDB`` and one
of its methods, :func:`path`. Let’s start with the class:

.. code-block:: python

    from unittest import mock

    from cusy import tasks


    def test_mock_tasksdb(tasks_cli):
        with mock.patch.object(tasks, "TasksDB") as MockTasksDB:
            mock_db_path = MockTasksDB.return_value.path.return_value = "/foo/"
            assert tasks_cli("config") == str(mock_db_path)

Let’s make sure it really works:

.. code-block:: pytest

    $ uv run pytest -v -s tests/cli/test_config.py::test_mock_tasksdb
    ============================= test session starts ==============================
    ...
    configfile: pyproject.toml
    plugins: cov-4.1.0, Faker-19.11.0
    collected 1 item

    tests/cli/test_config.py::test_mock_tasksdb PASSED

    ============================== 1 passed in 0.04s ===============================

Great, now we just need to move the database mock into a fixture, as we’ll need
it in lots of test methods:

.. code-block:: python

    @pytest.fixture()
    def mock_tasksdb():
        with mock.patch.object(tasks, "TasksDB") as MockTasksDB:
            yield MockTasksDB.return_value

This fixture mocks the ``TasksDB`` object and returns the ``return_value``, so
that tests can use it to substitute values for things like ``path``:

.. code-block:: python

    def test_mock_tasksdb(tasks_cli, mock_tasksdb):
        mock_tasksdb.path.return_value = "/foo/"
        result = runner.invoke(app, ["config"])
        assert result.stdout.rstrip() == "/foo/"

Alternatively, the :func:`@mock.patch` decorator can also be used to mock
classes or objects. In the following examples, the output of ``os.listdir`` is
mocked. For this, ``db_path`` does not need to exist on the file system:

.. code-block:: python

    import os
    from unittest import mock


    @mock.patch("os.listdir", mock.MagicMock(return_value="db_path"))
    def test_listdir():
        assert "db_path" == os.listdir()

Another option is to define the return value separately:

.. code-block:: python

    @mock.patch("os.listdir")
    def test_listdir(mock_listdir):
        mock_listdir.return_value = "db_path"
        assert "db_path" == os.listdir()

Synchronising mocks with ``autospec``
-------------------------------------

Mock objects are generally intended to be used in place of the real
implementation. By default, however, they will accept any access. For example,
if the real object allows :func:`.start(index)`, our mock objects should also
allow :func:`.start(index)`. However, there is a problem here. By default, mock
objects are too flexible: they would also accept :func:`stort` or other
misspelled, renamed or deleted methods or parameters. Over time, this can lead
to what is known as *‘mock drift’*, where the interface you are mocking changes,
but your mock in your test code does not. This form of mock drift can be
resolved by adding ``autospec=True`` to the mock during creation:

.. code-block:: python
   :emphasize-lines: 3

    @pytest.fixture()
    def mock_tasksdb():
        with mock.patch.object(tasks, "TasksDB", autospec=True) as MockTasksDB:
            yield MockTasksDB.return_value

This protection is usually always included when using ``autospec``. The only
exception I am aware of is when the class or object being mocked has dynamic
methods, or when attributes are added at runtime.

.. seealso::
   The Python documentation has a large section on ``autospec``:
   :ref:`python3:auto-speccing`.

Checking a call with :func:`assert_called_with`
-----------------------------------------------

So far, we have used the return values of a mocking method to ensure that our
application code handles the return values correctly. But sometimes there is no
useful return value, for example in :samp:`tasks add some tasks -o veit`. In
these cases, we can ask the mock object whether it was called correctly. After
calling :func:`tasks_cli("add some tasks -o veit")`, we do not use the API to
check whether the task has been added to the database, but instead use a mock to
ensure that the CLI has correctly called the right API method. The
implementation of the :func:`add` command ultimately calls :func:`db.add_task`
with a ``Task`` object:

.. _test_add_with_owner:

.. code-block:: python
   :emphasize-lines: 4

   def test_add_with_owner(mock_tasksdb, tasks_cli):
       tasks_cli("add some task -o veit")
       expected = tasks.Task("some task", owner="veit", state="todo")
       mock_tasksdb.add_task.assert_called_with(expected)

If :func:`add_task` is not called, or is called with the wrong type or the wrong
object content, the test fails. For example, if we capitalise the string
``"Veit"`` in expected but not in the CLI call, we get the following output:

.. code-block:: pytest
   :emphasize-lines: 10-13, 16

   $ uv run pytest -s tests/cli/test_add.py::test_add_with_owner
   ============================= test session starts ==============================
   ...
   configfile: pyproject.toml
   plugins: cov-4.1.0, Faker-19.11.0
   collected 1 item

   tests/cli/test_add.py F
   ...
   >           raise AssertionError(_error_message()) from cause
   E           AssertionError: expected call not found.
   E           Expected: add_task(Task(summary='some task', owner='Veit', state='todo', id=None))
   E           Actual: add_task(Task(summary='some task', owner='veit', state='todo', id=None))
   ...
   =========================== short test summary info ============================
   FAILED tests/cli/test_add.py::test_add_with_owner - AssertionError: expected call not found.
   ============================== 1 failed in 0.08s ===============================

.. seealso::
   There are a whole range of variants of :func:`assert_called`. You can find a
   complete list and description in `unittest.mock.Mock.assert_called
   <https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called>`_.

   If the only way to test is to ensure the correct call has been made, the
   various :func:`assert_called*` methods serve their purpose.

Creating error conditions
-------------------------

Let’s now check whether the Tasks CLI handles error conditions correctly. Here,
for example, is the implementation of the delete command:

.. code-block:: python

    @app.command()
    def delete(task_id: int):
        """Remove task in db with given id."""
        with tasks_db() as db:
            try:
                db.delete_task(task_id)
            except tasks.InvalidTaskId:
                print(f"Error: Invalid task id {task_id}")

To test how the CLI handles an error condition, we can simulate
:func:`delete_task` throwing an exception by assigning the exception to the mock
object’s `side_effect
<https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect>`_
attribute, something like this:

.. code-block:: python

    def test_delete_invalid(mock_tasksdb, tasks_cli):
        mock_tasksdb.delete_task.side_effect = tasks.api.InvalidTaskId
        out = tasks_cli("delete 42")
        assert "Error: Invalid task id 42" in out

That’s all we need to test the CLI: mocking return values, checking calls to
mock functions, and mocking exceptions. However, there are a whole host of other
mocking techniques that we haven’t covered. So be sure to read up on
:doc:`python3:library/unittest.mock` — the mock object library — if you want to
make extensive use of mocking.

Limitations of Mocking
----------------------

One of the biggest problems with using mocks is that, in a test, we are no
longer testing the behaviour but the implementation. This is not only
time-consuming but also dangerous: a valid refactoring – such as changing a
variable name – can cause tests to fail if that particular variable has been
mocked. However, we want our tests to fail only when there are breaks in
behaviour, not simply due to code changes.

Sometimes, though, mocking is the easiest way to generate exceptions or error
conditions and ensure that your code handles them correctly. There are also
cases where testing behaviour is impractical, such as when accessing a payment
API or sending emails. In these cases, it is a good option to test whether your
code calls a specific API method at the right time and with the correct
parameters.

.. seealso::
   * `“Don’t Mock What You Don’t Own”
     <https://hynek.me/articles/what-to-mock-in-5-mins/>`_ by Hynek Schlawack

.. note::
   Even in agent-based software development, we try to avoid mocking as much as
   possible:

   .. code-block:: md
      :caption: AGENTS.md

      - Prefer testing real code where possible. Use mocks and `monkeypatch` when absolute necessary. Try to avoid mocking as much as possible.

   .. seealso::
      * :ref:`agentic-software-engineering:testing`

Avoiding mocks with multi-level testing
---------------------------------------

We can also test the Tasks CLI without using mocks by utilising the API. In
doing so, we will not be testing the API itself, but simply using it to verify
the behaviour of actions executed via the CLI. We can also test the
:ref:`test_add_with_owner` example as follows:

.. code-block:: python

   def test_add_with_owner(tasks_db, tasks_cli):
       tasks_cli("add some task -o veit")
       expected = tasks.Task("some task", owner="veit", state="todo")
       all = tasks_db.list_tasks()
       assert len(all) == 1
       assert all[0] == expected

Mocking tests the implementation of the command-line interface and ensures that
an API call is made with specific parameters. With the mixed-layer approach, the
behaviour is tested to ensure that the result meets our expectations. This
approach is much less of a change detector and is more likely to remain valid
during a refactoring. Interestingly, the tests are also about twice as fast:

.. code-block:: pytest

   $ uv run pytest -s tests/cli/test_add.py::test_add_with_owner
   ============================= test session starts ==============================
   ...
   configfile: pyproject.toml
   plugins: cov-4.1.0, Faker-19.11.0
   collected 1 item

   tests/cli/test_add.py .

   ============================== 1 passed in 0.03s ===============================

We could also avoid mocking in another way. We could test the behaviour entirely
via the CLI. To do this, we might need to parse the output of the tasks list to
verify that the database contents are correct.

In the API, :func:`add_task` returns an index and provides a
:func:`get_task(index)` method, which helps with testing. Neither of these
methods is available in the CLI, but they could be. We could perhaps add the
commands tasks get index or tasks info index so that we can retrieve a task
instead of having to use tasks list for everything. list already supports
filtering. Perhaps filtering by index would work, rather than adding a new
command. And we could add output to ``tasks add`` that says something like
*‘Task added at index 3’*. These changes would fall under the category of
*Design for Testability*. They do not appear to involve any major changes to the
interface and might be worth considering in future versions.

Plugins to support mocking
--------------------------

So far, we have focused on the direct use of :doc:`mock
<python3:library/unittest.mock>`. However, there are many plugins that help with
mocking, such as `pytest-mock <https://pypi.org/project/pytest-mock/>`_, which
provides a ``mocker`` fixture. One advantage is that the fixture cleans up after
itself, so you don’t need to use a ``with`` block, as we did in our examples.

There are also some specialised mocking libraries:

- For mocking database access, the following are suitable

  - `pytest-postgresql <https://pypi.org/project/pytest-postgresql/>`_
  - `pytest-mongo <https://pypi.org/project/pytest-mongo/>`_
  - `pytest-mysql <https://pypi.org/project/pytest-mysql/>`_
  - `pytest-dynamodb <https://pypi.org/project/pytest-dynamodb/>`_.

- To test HTTP servers, you can use `pytest-httpserver
  <https://pypi.org/project/pytest_httpserver/>`_.
- To mock `requests <https://pypi.org/project/requests/>`_, you can use
  `responses <https://pypi.org/project/responses/>`_ or `betamax
  <https://pypi.org/project/betamax/>`_.
- Other tools for various requirements include

  - `pytest-rabbitmq <https://pypi.org/project/pytest-rabbitmq/>`_
  - `pytest-solr <https://pypi.org/project/pytest-solr/>`_
  - `pytest-elasticsearch <https://pypi.org/project/pytest-elasticsearch/>`_ and
    `pytest-redis <https://pypi.org/project/pytest-redis/>`_.
