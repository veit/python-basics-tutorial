``autospec``
============

Mock objects are generally intended to be used in place of the real
implementation. By default, however, they will accept any access. For example,
if the real object allows ``start(index)``, our mock objects should also allow
``start(index)``. However, there is a problem here. By default, mock objects are
too flexible: they would also accept ``stort()`` or other misspelt, renamed or
deleted methods or parameters. Over time, this can lead to what is known as
‘mock drift’, where the interface you are mocking changes, but your mock in your
test code does not. This form of mock drift can be resolved by adding
``autospec=True`` to the mock during creation:

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
