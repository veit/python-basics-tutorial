Test parameterisation
=====================

Parameterisation allows us to convert a test function into many test cases in
order to test more thoroughly with less work. To do this, we pass multiple sets
of arguments to the test to create new test cases. We’ll take a look at
redundant code that we can avoid with :term:`parameterisation <Parameter>`. Then
we’ll look at three options, in the order in which they should be chosen:

- Parameterisation of functions
- Parameterisation of fixtures
- Using a hook function called ``pytest_generate_tests``

We will solve the same :term:`parameterisation <Parameter>` problem with all
three methods, even if sometimes one solution is preferable to the other.

Testing without ``parametrize``
-------------------------------

Sending some values through a function and checking the output for correctness
is a common pattern when testing software. However, calling a function once with
a set of values is rarely sufficient to fully test the functions. Parameterised
testing is a way to send multiple data sets through the same test and have
pytest report if any of the data sets fail. To understand the problem that
:term:`parameterised <Parameter>` tests are trying to solve, let’s write some
tests for the ``finish()`` API method from :file:`src/items/api.py`:

.. code-block:: python

    def finish(self, item_id: int):
        """Set an item state to done."""
        self.update_item(item_id, Item(state="done"))

The states used in the application are *todo*, *in progress* and *done*, and
``finish()`` sets the state of a card to *done*. To test this, we could

#. create an Item object and add it to the database so we have a card to work
   with
#. call ``finish()``
#. ensure that the final state is *done*.

One variable is the start state of the item. It could be "todo", "in progress"
or even already "done". Let’s test all three:

.. code-block:: python

    from items import Item


    def test_finish_from_in_prog(items_db):
        index = items_db.add_item(
            Item("Update pytest section", state="in progress")
        )
        items_db.finish(index)
        item = items_db.get_item(index)
        assert item.state == "done"


    def test_finish_from_done(items_db):
        index = items_db.add_item(
            Item("Update cibuildwheel section", state="done")
        )
        items_db.finish(index)
        item = items_db.get_item(index)
        assert item.state == "done"


    def test_finish_from_todo(items_db):
        index = items_db.add_item(Item("Update mock tests", state="todo"))
        items_db.finish(index)
        item = items_db.get_item(index)
        assert item.state == "done"

Let’s let it go:

.. code-block:: pytest

    pytest -v tests/test_finish.py
    ============================= test session starts ==============================
    …
    collected 3 items

    tests/test_finish.py::test_finish_from_in_prog PASSED                    [ 33%]
    tests/test_finish.py::test_finish_from_done PASSED                       [ 66%]
    tests/test_finish.py::test_finish_from_todo PASSED                       [100%]

    ============================== 3 passed in 0.00s ===============================

The test functions are very similar. The only differences are the initial state
and the summary. One way to reduce the redundant code is to combine the three
functions into a single function, like this:

.. code-block:: python

    from items import Item


    def test_finish(items_db):
        for i in [
            Item("Update pytest section", state="done"),
            Item("Update cibuildwheel section", state="in progress"),
            Item("Update mock tests", state="todo"),
        ]:
            index = items_db.add_item(i)
            items_db.finish(index)
            item = items_db.get_item(index)
            assert item.state == "done"

Now we run :file:`tests/test_finish.py` again:

.. code-block:: pytest

    $ pytest -v tests/test_finish.py
    ============================= test session starts ==============================
    …
    collected 1 item

    tests/test_finish.py::test_finish PASSED                                 [100%]

    ============================== 1 passed in 0.00s ===============================

This test has also been passed and we have eliminated the superfluous code. But it's not the same:

- Only one test case is reported instead of three.
- If one of the test cases fails, we don’t know which one it is without looking
  at the traceback or other debugging information.
- If one of the test cases fails, the subsequent test cases are not executed.
  pytest stops the execution of a test if an assertion fails.

.. _parameterise-functions:

Parameterising functions
------------------------

To :term:`parameterise <Parameter>` a test function, add parameters to the test
definition and use the ``@pytest.mark.parametrize()`` decorator to define the
arguments to be passed to the test, like this:

.. code-block:: python

    import pytest

    from items import Item


    @pytest.mark.parametrize(
        "start_summary, start_state",
        [
            ("Update pytest section", "done"),
            ("Update cibuildwheel section", "in progress"),
            ("Update mock tests", "todo"),
        ],
    )
    def test_finish(items_db, start_summary, start_state):
        initial_item = Item(summary=start_summary, state=start_state)
        index = items_db.add_item(initial_item)
        items_db.finish(index)
        item = items_db.get_item(index)
        assert item.state == "done"

The ``test_finish()`` function now has its original ``items_db`` fixture as a
:term:`parameter`, but also two new parameters: ``start_summary`` and
``start_state``. These directly match the first argument of
``@pytest.mark.parametrize()``.

#. The first argument of ``@pytest.mark.parametrize()`` is a list of
   :term:`parameter` names. This argument could also be a list of strings, such
   as ``["start_summary", "start_state"]`` or a comma-separated string
   ``"start_summary, start_state"``.
#. The second argument of ``@pytest.mark.parametrize()`` is our list of test
   cases. Each element in the list is a test case represented by a tuple or list
   containing one element for each argument sent to the test function.

pytest performs this test once for each ``(start_summary, start_state)`` pair
and reports each as a separate test:

.. code-block:: console

   $ pytest -v tests/test_finish.py
   ============================= test session starts ==============================
   …
   collected 3 items

   tests/test_finish.py::test_finish[Update pytest section-done] PASSED    [ 33%]
   tests/test_finish.py::test_finish[Update cibuildwheel section-in progress] PASSED [ 66%]
   tests/test_finish.py::test_finish[Update mock tests-todo] PASSED        [100%]

   ============================== 3 passed in 0.00s ===============================

This use of ``parametrize()`` works for our purposes. However, it is not really
important for this ``test start_summary`` and makes every test case more
complex. Let’s change the :term:`parameterisation <Parameter>` in
``start_state`` and see how the syntax changes:

.. code-block:: python

   import pytest

   from items import Item


   @pytest.mark.parametrize(
       "start_state",
       [
           "done",
           "in progress",
           "todo",
       ],
   )
   def test_finish(items_db, start_state):
       i = Item("Update pytest section", state=start_state)
       index = items_db.add_item(i)
       items_db.finish(index)
       item = items_db.get_item(index)
       assert item.state == "done"

When we run the tests now, they focus on the change that is important to us:

.. code-block:: console

   $ pytest -v tests/test_finish.py
   ============================= test session starts ==============================
   …
   collected 3 items

   tests/test_finish.py::test_finish[done] PASSED                           [ 33%]
   tests/test_finish.py::test_finish[in progress] PASSED                    [ 66%]
   tests/test_finish.py::test_finish[todo] PASSED                           [100%]

   ============================== 3 passed in 0.01s ===============================

The output of the two examples differs in that now only the initial state is
listed, namely *todo*, *in progress* and *done*. In the previous example, pytest
still displayed the values of both :term:`parameters <Parameter>`, separated by
a hyphen ``-``. If only one parameter changes, no hyphen is required.

Parameterising fixtures
-----------------------

During function :term:`parameterisation <Parameter>`, pytest called our test
function once for each set of arguments that we specified. With fixture
parameterisation, we move these parameters into a fixture. pytest then calls the
fixture once for each set of values we specify. Subsequently, each test function
that depends on the fixture is called once for each fixture value. The syntax is
also different:

.. code-block:: python

   import pytest

   from items import Item


   @pytest.fixture(params=["done", "in progress", "todo"])
   def start_state(request):
       return request.param


   def test_finish(items_db, start_state):
       i = Item("Update pytest section", state=start_state)
       index = items_db.add_item(i)
       items_db.finish(index)
       item = items_db.get_item(index)
       assert item.state == "done"

This means that pytest calls ``start_state()`` three times, once for each of the
values in ``params``. Each value of ``params`` is stored in ``request.param`` so
that the fixture can use it. Within ``start_state()`` we could have code that
depends on the :term:`parameter` value. In this case, however, only the value of
the parameter is returned.

The function ``test_finish()`` is identical to the function we used in the
function :term:`parameterisation <Parameter>`, but without the decorator
``parametrize``. Since it has ``start_state`` as a parameter, pytest calls it
once for each value that is passed to the ``start_state()`` fixture. And after
all this, the output looks exactly the same as before:

.. code-block:: console

   $ pytest -v tests/test_finish.py
   ============================= test session starts ==============================
   …
   collected 3 items

   tests/test_finish.py::test_finish[done] PASSED                          [ 33%]
   tests/test_finish.py::test_finish[in progress] PASSED                   [ 66%]
   tests/test_finish.py::test_finish[todo] PASSED                          [100%]

   ============================== 3 passed in 0.01s ===============================

At first glance, fixture :term:`parameterisation <Parameter>` fulfils roughly
the same purpose as function parameterisation, but with a little more code.
However, fixture parameterisation has the advantage that a fixture is executed
for each set of arguments. This is useful if you have setup or teardown code
that needs to be executed for each test case, for example a different database
connection or file content or whatever.

It also has the advantage that many test functions can be executed with the same
set of :term:`parameters <Parameter>`. All tests that use the ``start_state``
fixture are called all three times, once for each ``start state``.

Parameterise with ``pytest_generate_tests``
-------------------------------------------

The third option for :term:`parameterisation <Parameter>` is to use a hook
function called ``pytest_generate_tests``. Hook functions are often used by
:doc:`plugins` to change the normal workflow of pytest. But we can use many of
them in test files and :file:`conftest.py` files.

The implementation of the same flow as before with ``pytest_generate_tests``
looks like this:

.. code-block:: python

   from items import Item


   def pytest_generate_tests(metafunc):
       if "start_state" in metafunc.fixturenames:
           metafunc.parametrize("start_state", ["done", "in progress", "todo"])


   def test_finish(items_db, start_state):
       i = Item("Update pytest section", state=start_state)
       index = items_db.add_item(i)
       items_db.finish(index)
       item = items_db.get_item(index)
       assert item.state == "done"

The ``test_finish()`` function has not changed; we have only changed the way
pytest enters the value for ``initial_state`` for each test call.

The ``pytest_generate_tests`` function that we provide is called by pytest when
it generates its list of tests to run. It is very powerful and our example is
just a simple case of matching the functionality of previous
:term:`parameterisation <Parameter>` methods. However, ``pytest_generate_tests``
is particularly useful if we want to change the parameterisation list at test
collection time in an interesting way. Here are a few possibilities:

- We could change our :term:`parameterisation <Parameter>` list based on a
  command line option that :samp:`metafunc.config.getoption("--SOME_OPTION")`
  [#]_ gives us. Maybe we add an ``--excessive`` option to test more values, or
  a ``--quick`` option to test only a few.
- The :term:`parameterisation <Parameter>` list of a parameter can be based on
  the presence of another parameter. For example, for test functions that query
  two related parameters, we can parameterise both with a different set of
  values than if the test queries only one of the parameters.
- We can :term:`parameterise <Parameter>` two related parameters at the same
  time, for example :samp:`metafunc.parametrize({"TUTORIAL, TOPIC", [("PYTHON
  BASICS", "TESTING"), ("PYTHON BASICS", "DOCUMENTING"), ("PYTHON FOR DATA
  SCIENCE, "GIT"), …]})`.

We have now become familiar with three ways of :term:`parameterising
<Parameter>` tests. Although we only create three test cases from one test
function in the :samp:`{finish()}` example, parameterisation can generate a
large number of test cases.

.. seealso::
   * `Basic pytest_generate_tests example
     <https://docs.pytest.org/en/stable/how-to/parametrize.html#basic-pytest-generate-tests-example>`_
   * `Generating parameters combinations, depending on command line
     <https://docs.pytest.org/en/stable/example/parametrize.html#generating-parameters-combinations-depending-on-command-line>`_
   * `A quick port of “testscenarios”
     <https://docs.pytest.org/en/stable/example/parametrize.html#a-quick-port-of-testscenarios>`_
   * `Deferring the setup of parametrized resources
     <https://docs.pytest.org/en/stable/example/parametrize.html#deferring-the-setup-of-parametrized-resources>`_
   * `Parametrizing test methods through per-class configuration
     <https://docs.pytest.org/en/stable/example/parametrize.html#parametrizing-test-methods-through-per-class-configuration>`_

Postponing the setup of parameterised resources
-----------------------------------------------

Test functions are parameterised at the time of recording. It is therefore
advisable to only set up complex resources such as database connections or
sub-processes when the actual test is being executed. Here is a simple example
of how you can achieve this.

.. code-block:: python
   :caption: test_backends.py

   import pytest


   def test_db_initialised(items_db):
       # An example test
       if items_db.__class__.__name__ == "Sqlite":
           pytest.fail("Deliberately failing for demonstration purposes")

We can now add a test configuration that generates two calls to the
``test_db_initialised`` function and also implements a factory that creates a
database object for the actual test calls:

.. code-block:: python
   :caption: conftest.py

   import pytest


   def pytest_generate_tests(metafunc):
       if "items_db" in metafunc.fixturenames:
           metafunc.parametrize("items_db", ["json", "sqlite"], indirect=True)


   class Json:
       "JSON object"


   class Sqlite:
       "Sqlite database object"


   @pytest.fixture
   def items_db(request):
       if request.param == "json":
           return Json()
       elif request.param == "sqlite":
           return Sqlite()
       else:
           raise ValueError("Invalid internal test config")

First, let’s take a look at what it looks like at the time of setup:

.. code-block:: pytest
   :emphasize-lines: 12-13

   $ uv run pytest tests/test_backends.py --collect-only
   ============================= test session starts ==============================
   platform darwin -- Python 3.14.0b4, pytest-8.4.1, pluggy-1.6.0
   rootdir: /Users/veit/sandbox/items
   configfile: pyproject.toml
   plugins: anyio-4.9.0, Faker-37.4.0, cov-6.2.1
   collected 2 items

   <Dir items>
     <Dir tests>
       <Module test_backends.py>
         <Function test_db_initialised[json]>
         <Function test_db_initialised[sqlite]>

   ========================== 2 test collected in 0.01s ===========================

.. code-block:: pytest

   $ uv run pytest -q tests/test_backends.py
   .F                                                                   [100%]
   ================================= FAILURES =================================
   _______________________ test_db_initialised[sqlite] ________________________

   db = <conftest.Sqlite object at 2491125695488>

       def test_db_initialised(items_db):
           # An example test
           if db.__class__.__name__ == "Sqlite":
   >           pytest.fail("Deliberately failing for demo purposes")
   E           Failed: Deliberately failing for demo purposes

   test_backends.py:8: Failed
   ========================= short test summary info ==========================
   FAILED tests/test_backends.py::test_db_initialised[sqlite] - Failed: deli...
   1 failed, 1 passed in 0.03s

Parametrised exceptions
-----------------------

`pytest.raises() <https://docs.pytest.org/en/latest/reference/reference.html#pytest.raises>`_
    can be used with the decorator ``pytest.mark.parametrize`` to write
    parametrised tests in which some tests raise exceptions and others do not.

`contextlib.nullcontext <https://docs.python.org/3/library/contextlib.html#contextlib.nullcontext>`_
    can be used to test test cases that are not expected to raise exceptions but
    should return a specific value. The value is specified as the
    ``enter_result`` parameter, which is available as the target of the ``with``
    statement.

Example of parameterised exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from contextlib import nullcontext

   import pytest


   @pytest.mark.parametrize(
       "divisor, expectation",
       [
           (3, nullcontext(2)),
           (2, nullcontext(3)),
           (1, nullcontext(6)),
           (0, pytest.raises(ZeroDivisionError)),
       ],
   )
   def test_division(divisor, expectation):
       """Test expected division results."""
       with expectation as e:
           assert (6 / divisor) == e

The first three test cases should run without exceptions, while the fourth
should raise a ``ZeroDivisionError`` exception, as expected by pytest.

----

.. [#] https://docs.pytest.org/en/latest/reference/reference.html#metafunc
