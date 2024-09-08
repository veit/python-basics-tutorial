Structure test suite
====================

You should ensure that assertions are kept at the end of test functions. This
recommendation is so common that it has at least two names:

Arrange-Act-Assert (AAA)
    became popular as part of :term:`test-driven development (TDD) <Test-driven
    development>`.
Given-When-Then (GWT)
    is used in the context of behaviour-driven development (BDD).

The division into these free phases has many advantages. This separates the
parts

Given/Arrange
   The initial state. This is where you set up data or the environment to
   prepare the action.
When/Act
    An action is executed. This is the focus of the test – the behaviour that
    we want to ensure works correctly.
Then/Assert
    An expected result or end state should occur. At the end of the test, we
    make sure that the action has led to the expected behaviour.

A common counter-pattern is the *Arrange–Assert–Act–Assert–Act–Assert…* pattern,
where a variety of actions followed by state or behavioural checks validate a
workflow. This seems reasonable until the test fails. Any of the actions could
have caused the failure, so the test doesn’t focus on testing a particular
behaviour. Or it could have been the setup in *Arrange* that caused the error.
This nested ``assert`` pattern leads to tests that are difficult to debug and
maintain. Sticking to * Given-When-Then* or *Arrange-Act-Assert* keeps the test
focused and makes it more maintainable.

Let’s apply this structure to one of our first tests as an example:

.. code-block:: python

    def test_equality_fail():
        # Given two item objects with known contents
        i1 = Item("do something", "veit")
        i2 = Item("do something else", "veit.schiele")
        # WHEN the two item objects are not identical
        if i1 != i2:
            # THEN the result will be a string
            pytest.fail("The items are not identical!")

The structure helps you to organise the test functions and focus on testing
**one** behaviour. The structure also helps you to think of other test cases.
Focusing on an initial state helps you to think of other states that might be
relevant for testing the same action. Similarly, focusing on an ideal outcome
helps you think of other possible outcomes, such as failure states or error
states, that should also be tested with other test cases.

Grouping tests with classes
---------------------------

Up to now, we have written test functions within test modules in a file system
directory. This structuring of the test code actually works quite well and is
sufficient for many projects. However, pytest also allows us to group tests with
classes. Let’s take some of the test functions that relate to the equality of
items and group them into a class:

.. code-block:: python

    class TestEquality:
        def test_equality(self):
            i1 = Item("do something", "veit", "todo", 42)
            i2 = Item("do something", "veit", "todo", 42)
            assert i1 == i2

        def test_equality_with_diff_ids(self):
            i1 = Item("do something", "veit", "todo", 42)
            i2 = Item("do something", "veit", "todo", 43)
            assert i1 == i2

        def test_inequality(self):
            i1 = Item("do something", "veit", "todo", 42)
            i2 = Item("do something else", "veit", "done", 42)
            assert i1 != i2

The code looks pretty much the same as before, with the exception that each
method must have an initial ``self`` argument. We can now execute all these
methods together by specifying the class:

.. code-block:: pytest

    $ pytest -v tests/test_classes.py::TestEquality
    ============================= test session starts ==============================
    …
    collected 3 items

    tests/test_classes.py::TestEquality::test_equality PASSED                [ 33%]
    tests/test_classes.py::TestEquality::test_equality_with_diff_ids PASSED  [ 66%]
    tests/test_classes.py::TestEquality::test_inequality PASSED              [100%]

    ============================== 3 passed in 0.00s ===============================

However, we can still call a single method:

.. code-block:: pytest

    $ pytest -v tests/test_classes.py::TestEquality::test_equality
    ============================= test session starts ==============================
    …
    collected 1 item

    tests/test_classes.py::TestEquality::test_equality PASSED                [100%]

    ============================== 1 passed in 0.00s ===============================

If you are familiar with :doc:`/oop/index` and :doc:`class inheritance
</oop/inheritance>`, you can use hierarchies of test classes for inherited
helper methods. I recommend that you use test classes sparingly and mainly for
grouping, even in productive test code. If you go to too much trouble with test
class inheritance, it will get confusing in the future.

Executing a subset of tests
---------------------------

In the previous section, we used test classes to execute a subset of tests.
Executing a small group of tests is very handy when debugging, or if you want to
limit the tests to a specific section of the codebase you are working on. pytest
allows you to execute a subset of tests in different ways:

+-----------------------------------------------+-----------------------------------------------------------------------+
| Subset                                        | Syntax                                                                |
+===============================================+=======================================================================+
| All tests in one directory                    | :samp:`pytest {path}`                                                 |
+-----------------------------------------------+-----------------------------------------------------------------------+
| All tests in a module                         | :samp:`pytest {path}/test_{module}.py`                                |
+-----------------------------------------------+-----------------------------------------------------------------------+
| All files changed in the working directory of | :samp:`pytest $(git diff --name-only 'tests/test_*.py')`              |
| a :doc:`Git                                   |                                                                       |
| <Python4DataScience:productive/git/index>`    |                                                                       |
| repository                                    |                                                                       |
+-----------------------------------------------+-----------------------------------------------------------------------+
| All tests in a class                          | :samp:`pytest {path}/test_{module}.py::Test{Class}`                   |
+-----------------------------------------------+-----------------------------------------------------------------------+
| Single test function                          | :samp:`pytest {path}/test_{module}.py::test_{function}`               |
+-----------------------------------------------+-----------------------------------------------------------------------+
| Single test method                            | :samp:`pytest {path}/test_{module}.py::Test{Class}::test_{method}`    |
+-----------------------------------------------+-----------------------------------------------------------------------+
| Tests that correspond to a                    | :samp:`pytest -k {pattern}`                                           |
| name pattern                                  |                                                                       |
+-----------------------------------------------+-----------------------------------------------------------------------+
| Tests by marker                               | see :doc:`markers`                                                    |
+-----------------------------------------------+-----------------------------------------------------------------------+

Whether ``pytest`` finds your test code depends on the naming:

* Test files should be named :samp:`test_{something}.py` or
  :samp:`{something}_test.py`.
* Test methods and functions should be named :samp:`test_{something}`.
* Test classes should be named :samp:`Test{Something}`.

.. tip::
   Use a directory structure that corresponds to the way you want to run your
   code, because it is easy to run a complete subdirectory. This way you can
   divide features and functions or use subsystems as a basis or orientate
   yourself on the code structure.

You can also use :samp:`-k {pattern}` to filter directories, classes or test
prefixes, for example all tests of class ``TestEquality``.

.. code-block:: pytest

    $ pytest -v -k TestEquality
    ============================= test session starts ==============================
    …
    collected 7 items / 4 deselected / 3 selected

    test_classes.py::TestEquality::test_equality PASSED                      [ 33%]
    test_classes.py::TestEquality::test_equality_with_diff_ids PASSED        [ 66%]
    test_classes.py::TestEquality::test_inequality PASSED                    [100%]

    ======================= 3 passed, 4 deselected in 0.00s ========================

or all tests with ``equality`` in the name:

.. code-block:: pytest

    pytest -v --tb=no -k equality
    ============================= test session starts ==============================
    …
    collected 7 items / 3 deselected / 4 selected

    test_classes.py::TestEquality::test_equality PASSED                      [ 25%]
    test_classes.py::TestEquality::test_equality_with_diff_ids PASSED        [ 50%]
    test_classes.py::TestEquality::test_inequality PASSED                    [ 75%]
    test_item_fail.py::test_equality_fail FAILED                             [100%]

    =========================== short test summary info ============================
    FAILED test_item_fail.py::test_equality_fail - Failed: The items are not identical!
    ================== 1 failed, 3 passed, 3 deselected in 0.01s ===================

Unfortunately, one of these is our error example. We can remove it by expanding
the expression:

.. code-block:: pytest

    $ pytest -v --tb=no -k "equality and not equality_fail"
    ============================= test session starts ==============================
    …
    collected 7 items / 4 deselected / 3 selected

    test_classes.py::TestEquality::test_equality PASSED                      [ 33%]
    test_classes.py::TestEquality::test_equality_with_diff_ids PASSED        [ 66%]
    test_classes.py::TestEquality::test_inequality PASSED                    [100%]

    ======================= 3 passed, 4 deselected in 0.00s ========================

The keywords ``and``, ``not``, ``or`` and ``()`` are allowed to create complex
expressions. Here is a test run of all tests with or "ids" in the name, but not
in the "TestEquality" class:

.. code-block:: pytest

    $ pytest -v --tb=no -k "(inequality or id) and not _fail"
    ============================= test session starts ==============================
    …
    collected 7 items / 4 deselected / 3 selected

    test_classes.py::TestEquality::test_equality_with_diff_ids PASSED        [ 33%]
    test_classes.py::TestEquality::test_inequality PASSED                    [ 66%]
    test_helper.py::test_ident PASSED                                        [100%]

    ======================= 3 passed, 4 deselected in 0.00s ========================

.. _keyword:

The ``-k`` keyword option, together with ``and``, ``not`` and ``or``, offers
great flexibility when selecting the tests you want to run. This proves to be
very helpful when troubleshooting or developing new tests.

.. tip::
   It is a good idea to use quotation marks when selecting a test to run as the
   hyphens, brackets and spaces can confuse the shells.
