``assert_called``
=================

So far, we have used the return values of a mocking method to ensure that our
application code handles the return values correctly. However, sometimes there
is no useful return value, for example, with :samp:`tasks add some tasks -o
veit`. In such cases, we can use :func:`assert_called_with` to check whether the
mock object was called correctly. After calling :samp:`tasks_cli("add some tasks
-o veit")`, we do not use the API to check whether the item has been added to
the database; instead, we use a mock to ensure that the CLI has correctly called
the correct API method. The implementation of the :func:`add` command ultimately
calls :func:`db.add_task` with a ``Task`` object:

.. _test_add_with_owner:

.. code-block:: python
   :emphasize-lines: 4

   def test_add_with_owner(mock_tasksdb, tasks_cli):
       tasks_cli("add some task -o veit")
       expected = tasks.Task("some task", owner="veit", state="todo")
       mock_tasksdb.add_task.assert_called_with(expected)

If :func:`add_task` is not called, or is called with the wrong type or the wrong
object content, the test fails. For example, if we capitalise the string
``Veit`` in the expected section but not in the CLI call, we get the following
output:

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
   complete list and description in :py:meth:`unittest.mock.Mock.assert_called`.

   If the only way to test is to ensure that the function has been called
   correctly, the various :meth:`assert_called*` methods serve their purpose.
