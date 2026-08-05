Examples
========

Mocking ``datetime.datetime``
-----------------------------

We wanted to start with a simple example to check whether the working days from
Monday to Friday are calculated correctly.

#. First, we import :class:`datetime.datetime` and :class:`Mock
   <python3:unittest.mock.Mock>`:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 1-2
      :lineno-start: 1

#. Next, we’ll define two test days:

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

#. Then let’s mock ``datetime``:

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

Mocking the CLI
---------------

When testing the Tasks CLI, we’ll also look at how the ``CliRunner`` provided by
`Typer <https://typer.tiangolo.com>`_ helps with testing. Typer offers a testing
interface that allows us to invoke our application without having to resort to
:func:`python3:subprocess.run`, as in the brief :ref:`capsys-fixture` example.
This is useful because we cannot simulate what runs in a separate process. So,
in :file:`tests/cli/conftest.py`, we can simply pass our application
``cusy.tasks.cli.app`` and a list of strings representing the command to the
:func:`invoke` function of our ``runner``: more specifically, we use
``shlex.split(command_string)`` to parse the commands, for example, :samp:`list
-o 'veit'` into :samp:`["list", "-o", "veit"]`, and can then capture and return
the output.

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

We can then simply use this fixture to test, for example, the version in
:file:`tests/cli/test_version.py`:

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
are going to patch. The call to :func:`mock.patch.object`, used as a
:doc:`context manager <../../control-flow/with>` within a ``with`` block,
returns a mock object that is cleaned up after the ``with`` block:

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

:func:`tasks_db` is a :doc:`context manager  <../../control-flow/with>` that
returns a ``tasks.TasksDB`` object. The returned object is then used as ``db``
to call :func:`db.path`. So we need to mock two things here: ``tasks.TasksDB``
and one of its methods, :func:`path`. Let’s start with the class:

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

Alternatively, the :func:`@mock.patch` :doc:`decorator
<../../functions/decorators>` can also be used to mock classes or objects. In
the following examples, the output of ``os.listdir`` is mocked. For this,
``db_path`` does not need to exist on the file system:

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
