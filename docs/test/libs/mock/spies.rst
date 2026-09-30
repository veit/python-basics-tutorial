Spies
=====

Unlike mocks, :term:`spies <Spy>` wrap around objects and usually forward all
method calls to the original object. Despite its name, :doc:`mock
<python3:library/unittest.mock>` is not only suitable for mocks: the ``wraps``
argument of the :class:`Mock <python3:unittest.mock.Mock>` class can also be
used to create spies. Calls are then forwarded to the wrapped object and return
its actual results, for example:

.. code-block:: pycon

   >>> def test_workinngday():
   ...     spy = Mock(wraps=is_workingday, return_value=monday)
   ...     assert is_workingday()
   ...

However, ``wraps`` only provides the mock’s default behaviour; other
configurations take precedence. If you set ``return_value``, the wrapped object
is not called at all.

If, on the other hand, you set :py:attr:`unittest.mock.Mock.side_effect`, this
is executed instead of the wrapped object, unless it returns
:py:data:`unittest.mock.DEFAULT`; in which case, the call is forwarded.

For example, when implementing the delete command, we can check whether the
Tasks CLI handles error conditions correctly:

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
:func:`delete_task` throwing an exception by assigning the :class:`Exception` to
the mock object’s `side_effect
<https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect>`_ attribute, something like this:

.. code-block:: python

    def test_delete_invalid(mock_tasksdb, tasks_cli):
        mock_tasksdb.delete_task.side_effect = tasks.api.InvalidTaskId
        out = tasks_cli("delete 42")
        assert "Error: Invalid task id 42" in out
