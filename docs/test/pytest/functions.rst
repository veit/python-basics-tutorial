Writing test functions
======================

``assert`` statements
---------------------

When writing test functions, the normal pytest ``assert`` statement is your
most important tool. The simplicity of this statement leads many developers to
favour pytest over other frameworks. Below is a list of some of
:doc:`../unittest`’s ``assert`` forms and ``assert`` helper functions:

+-------------------------------+---------------------------------------+
| pytest                        | unittest                              |
+===============================+=======================================+
| :samp:`assert {something}`    | :samp:`assertTrue({something})`       |
+-------------------------------+---------------------------------------+
| :samp:`assert not {something}`| :samp:`assertFalse({something})`      |
+-------------------------------+---------------------------------------+
| :samp:`assert {x} == {y}`     | :samp:`assertEqual({x}, {y})`         |
+-------------------------------+---------------------------------------+
| :samp:`assert {x} != {y}`     | :samp:`assertNotEqual({x}, {y})`      |
+-------------------------------+---------------------------------------+
| :samp:`assert {x} <= {y}`     | :samp:`assertLessEqual({x}, {y})`     |
+-------------------------------+---------------------------------------+
| :samp:`assert {x} is None`    | :samp:`assertIsNone({x})`             |
+-------------------------------+---------------------------------------+
| :samp:`assert {x} is not None`| :samp:`assertIsNotNone({x})`          |
+-------------------------------+---------------------------------------+

With pytest you can use :samp:`assert {EXPRESSION}` with any expression. If the
expression would evaluate to ``False`` when converted to a boolean value, the
test would fail.

pytest includes a function called ``assert rewriting`` that intercepts
``assert`` calls and replaces them with something that can tell you more about
why your assumptions failed. Let’s see how helpful this rewriting is by looking
at a failed ``assert`` test:

.. code-block:: python

    def test_equality_fails():
        i1 = Item("do something", "veit")
        i2 = Item("do something else", "veit")
        assert i1 == i2

This test fails, but the traceback information is interesting:

.. code-block:: pytest

    $ pytest tests/test_item_fails.py
    ============================= test session starts ==============================
    …
    collected 1 item

    tests/test_item_fails.py F                                               [100%]

    =================================== FAILURES ===================================
    _____________________________ test_equality_fails ______________________________

        def test_equality_fails():
            i1 = Item("do something", "veit")
            i2 = Item("do something else", "veit.schiele")
    >       assert i1 == i2
    E       AssertionError: assert Item(summary=...odo', id=None) == Item(summary=...odo', id=None)
    E
    E         Omitting 1 identical items, use -vv to show
    E         Differing attributes:
    E         ['summary', 'owner']
    E
    E         Drill down into differing attribute summary:
    E           summary: 'do something' != 'do something else'...
    E
    E         ...Full output truncated (8 lines hidden), use '-vv' to show

    tests/test_item_fails.py:7: AssertionError
    =========================== short test summary info ============================
    FAILED tests/test_item_fails.py::test_equality_fails - AssertionError: assert Item(summary=...odo', id=None) == Item(summary=...od...
    ============================== 1 failed in 0.03s ===============================

That’s a lot of information:

For each failed test, the exact line of the error is displayed with a ``>``
pointing to the error.

The ``E`` lines show you additional information about the ``assert`` error so
you can figure out what went wrong. I intentionally entered two mismatches in
``test_equality_fails()``, but only the first one was displayed. Let’s try again
with the ``-vv`` option as suggested in the error message:

.. code-block:: pytest

    $ pytest -vv tests/test_item_fails.py
    ============================= test session starts ==============================
    …
    collected 1 item

    tests/test_item_fails.py::test_equality_fails FAILED                     [100%]

    =================================== FAILURES ===================================
    _____________________________ test_equality_fails ______________________________

        def test_equality_fails():
            i1 = Item("do something", "veit")
            i2 = Item("do something else", "veit.schiele")
    >       assert i1 == i2
    E       AssertionError: assert Item(summary='do something', owner='veit', state='todo', id=None) == Item(summary='do something else', owner='veit.schiele', state='todo', id=None)
    E
    E         Matching attributes:
    E         ['state']
    E         Differing attributes:
    E         ['summary', 'owner']
    E
    E         Drill down into differing attribute summary:
    E           summary: 'do something' != 'do something else'
    E           - do something else
    E           ?             -----
    E           + do something
    E
    E         Drill down into differing attribute owner:
    E           owner: 'veit' != 'veit.schiele'
    E           - veit.schiele
    E           + veit

    tests/test_item_fails.py:7: AssertionError
    =========================== short test summary info ============================
    FAILED tests/test_item_fails.py::test_equality_fails - AssertionError: assert Item(summary='do something', owner='veit', state='to...
    ============================== 1 failed in 0.03s ===============================

pytest has listed exactly which attributes match and which do not. The exact
deviations were also highlighted.

For comparison, we can see what Python displays for ``assert`` errors. To be
able to call the test directly from Python, we need to add a block at the end of
:file:`tests/test_item_fails.py`:

.. code-block:: python

    if __name__ == "__main__":
        test_equality_fails()

If we now run the test with Python, we get the following result:

.. code-block:: pycon

    python tests/test_item_fails.py
    Traceback (most recent call last):
      File "tests/test_item_fails.py", line 11, in <module>
        test_equality_fails()
      File "tests/test_item_fails.py", line 7, in test_equality_fails
        assert i1 == i2
               ^^^^^^^^
    AssertionError

That doesn’t tell us much. The pytest output gives us much more information
about why our assumptions failed.

.. _pytest_fail:

Failing with ``pytest.fail()`` and exceptions
---------------------------------------------

Failing assertions is the main way that tests fail. But this is not the only
way. A test also fails if there is an uncaught :doc:`/control-flow/exceptions`.
This can happen when

* an ``assert`` statement fails, resulting in an ``AssertionError`` exception,
* the test code calls ``pytest.fail()``, which leads to an exception, or
* another exception is thrown.

Although any exception can cause a test to fail, I prefer to use ``assert``. In
rare cases where ``assert`` is not appropriate, I usually use ``pytest.fail()``.

Here is an example of using pytest’s ``fail()`` function to explicitly fail a
test:

.. code-block:: python

    def test_with_fail():
        i1 = Item("do something", "veit")
        i2 = Item("do something else", "veit.schiele")
        if i1 != i2:
            pytest.fail("The items are not identical!")

The output is as follows:

.. code-block:: pytest

    pytest tests/test_item_fails.py
    ============================= test session starts ==============================
    …
    collected 1 item

    tests/test_item_fails.py F                                               [100%]

    =================================== FAILURES ===================================
    ________________________________ test_with_fail ________________________________

        def test_with_fail():
            i1 = Item("do something", "veit")
            i2 = Item("do something else", "veit.schiele")
            if i1 != i2:
    >           pytest.fail("The items are not identical!")
    E           Failed: The items are not identical!

    tests/test_item_fails.py:10: Failed
    =========================== short test summary info ============================
    FAILED tests/test_item_fails.py::test_with_fail - Failed: The items are not identical!
    ============================== 1 failed in 0.03s ===============================

When calling ``pytest.fail()`` or throwing an exception, we do not get the
``assert`` rewriting provided by pytest. However, there are useful occasions to
use ``pytest.fail()``, such as in an ``assertion`` utility.

Writing ``assertion`` helper functions
--------------------------------------

An ``assertion`` helper function is used to package a complicated ``assertion``
check. For example, the ``Item`` data class is set up so that two items with
different IDs still report equality. If we want a stricter check, we could
write a helper function called ``assert_ident`` as follows:

.. code-block:: python

    import pytest

    from items import Item


    def assert_ident(i1: Item, i2: Item):
        __tracebackhide__ = True
        assert i1 == i2
        if i1.id != i2.id:
            pytest.fail(f"The IDs do not match: {i1.id} != {i2.id}")


    def test_ident():
        i1 = Item("something to do", id=42)
        i2 = Item("something to do", id=42)
        assert_ident(i1, i2)


    def test_ident_fail():
        i1 = Item("something to do", id=42)
        i2 = Item("something to do", id=43)
        assert_ident(i1, i2)


The ``assert_ident`` function sets ``__tracebackhide__ = True``. The result is
that failed tests are not included in the traceback. The normal ``assert i1 ==
i2`` is then used to check everything except id for equality.

Finally, the IDs checked ``pytest.fail()`` are used to fail the test with a
helpful message. Let’s take a look at what this looks like after execution:

.. code-block:: pytest

    $ pytest tests/test_helper.py
    ============================= test session starts ==============================
    …
    collected 2 items

    tests/test_helper.py .F                                                  [100%]

    =================================== FAILURES ===================================
    _______________________________ test_ident_fail ________________________________

        def test_ident_fail():
            i1 = Item("something to do", id=42)
            i2 = Item("something to do", id=43)
    >       assert_ident(i1, i2)
    E       Failed: The IDs do not match: 42 != 43

    tests/test_helper.py:22: Failed
    =========================== short test summary info ============================
    FAILED tests/test_helper.py::test_ident_fail - Failed: The IDs do not match: 42 != 43
    ========================= 1 failed, 1 passed in 0.03s ==========================

Testing for expected exceptions
-------------------------------

We have looked at how any exception can cause a test to fail. But what if part
of the code we are testing should raise an exception? For this we use
``pytest.raises()`` to test for expected exceptions. An example of this would be
the Items API, which has an ``ItemsDB`` class that requires a path argument.

.. code-block:: python

    from items.api import ItemsDB


    def test_db_exists():
        ItemsDB()

.. code-block:: pytest

    $ pytest --tb=short tests/test_db.py
    ============================= test session starts ==============================
    …
    collected 1 item

    tests/test_db.py F                                                       [100%]

    =================================== FAILURES ===================================
    ________________________________ test_db_exists ________________________________
    tests/test_db.py:5: in test_db_exists
        ItemsDB()
    E   TypeError: ItemsDB.__init__() missing 1 required positional argument: 'db_path'
    =========================== short test summary info ============================
    FAILED tests/test_db.py::test_db_exists - TypeError: ItemsDB.__init__() missing 1 required positional argument: 'db_p...
    ============================== 1 failed in 0.03s ===============================

Here I have used the shorter traceback format ``--tb=short`` because we don’t
need to see the full traceback to find out which exception was thrown.

The exception ``TypeError`` seems to make sense because the error occurs when
trying to initialise the custom ``ItemsDB`` type. We can write a test to ensure
that this exception is thrown, something like this:

.. code-block:: python

    import pytest

    from items.api import ItemsDB


    def test_db_exists():
        with pytest.raises(TypeError):
            ItemsDB()

The instruction with ``pytest.raises(TypeError):`` states that the next code
block should throw a ``TypeError`` exception. If no exception or another
exception is raised, the test fails.

We have just checked the type of the exception in ``test_db_exists()``. We can
also check if the message is correct, or any other aspect of the exception, such
as additional parameters:

.. code-block:: python

    def test_db_exists():
        match_regex = "missing 1 .* positional argument"
        with pytest.raises(TypeError, match=match_regex):
            ItemsDB()

or

.. code-block:: python

    def test_db_exists():
        with pytest.raises(TypeError) as exc_info:
            ItemsDB()
        expected = "missing 1 required positional argument"
        assert expected in str(exc_info.value)
