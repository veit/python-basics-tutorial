Limitations of mocking
======================

One of the biggest problems with using mocks is that, in a test, we are no
longer testing the behaviour but the implementation. However, this is not only
time-consuming but also dangerous: a valid refactoring – for example, changing a
variable name – can cause tests to fail if that particular variable has been
mocked. However, we want our tests to fail only when there are breaks in
behaviour, not simply because of code changes.

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
:ref:`test_add_with_owner <test_add_with_owner>` example as follows:

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
during refactoring. Interestingly, the tests are also about twice as fast:

.. code-block:: pytest

   $ uv run pytest -s tests/cli/test_add.py::test_add_with_owner
   ============================= test session starts ==============================
   …
   configfile: pyproject.toml
   plugins: cov-4.1.0, Faker-19.11.0
   collected 1 item

   tests/cli/test_add.py .

   ============================== 1 passed in 0.03s ===============================

We could also avoid mocking in another way. We could test the behaviour entirely
via the CLI. To do this, we might need to parse the output of the tasks list to
verify that the database contents are correct.

In the API, :func:`add_task` returns an index and provides a ``get_task(index)``
method, which helps with testing. Neither of these methods is available in the
CLI, but they could be. We could perhaps add the commands ``tasks get index`` or
``tasks info index`` so that we can retrieve a task without having to use
``tasks list`` for everything. ``list`` already supports filtering. Perhaps
filtering by index would work, rather than adding a new command. And we could
add output to ``tasks add`` that says something like *Task added at index 3*.
These changes would fall under the category of *Design for Testability*. They do
not appear to involve any major changes to the interface and might be worth
considering in future versions.
