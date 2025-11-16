Markers
=======

Markers in pytest can be thought of as tags or labels. If some tests are slow,
you can mark them with ``@pytest.mark.slow`` and have pytest skip those tests if
you are in a hurry. You can select a handful of tests from a test suite and mark
them with ``@pytest.mark.smoke`` and run them as the first stage of a test
pipeline in a :term:`CI` system. You can really use markers for any reason you
have to run just a few tests.

pytest contains a handful of built-in markers that change the behaviour of the
test execution. We have already used one of these, ``@pytest.mark.parametrize``,
in :ref:`parameterise-functions`. In addition to the custom markers we can
create and add to our tests, the built-in markers tell pytest to do something
special with the marked tests.

Below, we will explore both types of markers in more detail: the built-in
markers that change behaviour and the custom markers that we can create to
select which tests to run. We can also use markers to pass information to a
fixture that is used by a test.

Using built-in markers
----------------------

The pytest built-in markers are used to modify the test execution. Here is the
complete list of built-in markers included in pytest:

:samp:`@pytest.mark.filterwarnings({WARNUNG})`
    This marker adds a warning filter to the specified test.
:samp:`@pytest.mark.skip(reason={None})`
    This marker skips the test with an optional reason.
:samp:`@pytest.mark.skipif({BEDINGUNG}, ...*, {GRUND})`
    This marker skips the test if one of the conditions is ``True``.
:samp:`@pytest.mark.xfail({BEDINGUNG}, ...* {GRUND}, run={True}, raises={None}, strict={xfail_strict})`
    This marker tells pytest that we expect the test to fail.
:samp:`@pytest.mark.parametrize({ARG1, ARG2, ...`
    This marker calls a test function several times, passing different arguments
    one after the other.
:samp:`@pytest.mark.usefixtures({FIXTURE1, FIXTURE2, ...`
    This marker identifies tests that require all the specified fixtures.

We have already used :doc:`@pytest.mark.parametrize <params>`. Let’s go through
the other three most commonly used built-in markers with some examples to see
how they work.

Skipping tests with ``@pytest.mark.skip``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``skip`` marker allows us to skip a test. Let’s say we want to add the
ability to sort in a future version of the ``Items`` application and want the
``Item`` class to support comparisons. We write a test for comparing ``Item``
objects with ``<`` as follows:

.. code-block:: python

    from items import Item


    def test_less_than():
        i1 = Item("Update pytest section")
        i2 = Item("Update cibuildwheel section")
        assert i1 < i2


    def test_equality():
        i1 = Item("Update pytest section")
        i2 = Item("Update pytest section")
        assert i1 == i2

And it fails:

.. code-block:: pytest

    pytest --tb=short tests/test_compare.py
    ============================= test session starts ==============================
    ...
    collected 2 items

    tests/test_compare.py F.                                                 [100%]

    =================================== FAILURES ===================================
    ________________________________ test_less_than ________________________________
    tests/test_compare.py:7: in test_less_than
        assert i1 < i2
    E   TypeError: '<' not supported between instances of 'Item' and 'Item'
    =========================== short test summary info ============================
    FAILED tests/test_compare.py::test_less_than - TypeError: '<' not supported between instances of 'Item' and 'Item'
    ========================= 1 failed, 1 passed in 0.03s ==========================

The error is simply due to the fact that we have not yet implemented this
function. However, we don’t have to throw this test away again; we can simply
omit it:

.. code-block:: python
   :emphasize-lines: 1, 6

    import pytest

    from items import Item


    @pytest.mark.skip(reason="Items do not yet allow a < comparison")
    def test_less_than():
        i1 = Item("Update pytest section")
        i2 = Item("Update cibuildwheel section")
        assert i1 < i2

The marker ``@pytest.mark.skip()`` instructs pytest to skip the test. Specifying
a reason is optional, but it helps with further development. When we execute
skipped tests, they are displayed as ``s``:

.. code-block::
   :emphasize-lines: 6

    $ pytest --tb=short tests/test_compare.py
    ============================= test session starts ==============================
    ...
    collected 2 items

    tests/test_compare.py s.                                                 [100%]

    ========================= 1 passed, 1 skipped in 0.00s =========================

… or verbos as ``SKIPPED``:

.. code-block::
   :emphasize-lines: 1, 10

    $ pytest -v -ra tests/test_compare.py
    ============================= test session starts ==============================
    ...
    collected 2 items

    tests/test_compare.py::test_less_than SKIPPED (Items do not yet allo...) [ 50%]
    tests/test_compare.py::test_equality PASSED                              [100%]

    =========================== short test summary info ============================
    SKIPPED [1] tests/test_compare.py:6: Items do not yet allow a < comparison
    ========================= 1 passed, 1 skipped in 0.00s =========================

Since we have instructed pytest with ``-r`` to output a short summary of our
tests, we get an additional line at the bottom that lists the reason we
specified in the marker. The ``a`` in ``-ra`` stands for *all except passed*.
The ``-ra`` options are the most common, as we almost always want to know why
certain tests failed.

.. seealso::
   * `Skipping test functions
     <https://docs.pytest.org/en/latest/how-to/skipping.html#skipping-test-functions>`_

Conditional skipping of tests with ``@pytest.mark.skipif``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Suppose we know that we will not support sorting in versions 0.1.x of the Items
app, but we will support it in version 0.2.x. Then we can instruct pytest to
skip the test for all versions of items lower than 0.2.x as follows:

.. code-block:: python
   :emphasize-lines: 2, 4, 8-11

    import pytest
    from packaging.version import parse

    import items
    from items import Item


    @pytest.mark.skipif(
        parse(items.__version__).minor < 2,
        reason="The comparison with < is not yet supported in version 0.1.x.",
    )
    def test_less_than():
        i1 = Item("Update pytest section")
        i2 = Item("Update cibuildwheel section")
        assert i1 < i2

With the ``skipif`` marker, you can enter as many conditions as you like, and if
one of them is true, the test is skipped. In our case, we use
``packaging.version.parse`` to isolate the minor version and compare it with the
number 2.

In this example, `packaging <https://pypi.org/project/packaging/>`_ is used as
an additional package. If you want to try out the example, install it first with
``python -m pip install packaging``.

.. tip::
   ``skipif`` is also ideal if tests need to be written differently for
   different operating systems.

.. seealso::
   * `skipif <https://docs.pytest.org/en/latest/how-to/skipping.html#id1>`_

``@pytest.mark.xfail``
~~~~~~~~~~~~~~~~~~~~~~

If we want to run all tests, even those that we know will fail, we can use the
marker ``xfail`` or more precisely :samp:`@pytest.mark.xfail({CONDITION}, {...
*, {REASON}, run={True}, raises={None}, strict={True})`. The first set of
:term:`parameters <Parameter>` for this fixture is the same as for  ``skipif``.

``run``
    The test is executed by default, unless ``run=False`` is set.
``raises``
    allows you to specify an exception type or a tuple of exception types that
    should result in an ``xfail``. Any other exception will cause the test to
    fail.
``strict``
    tells pytest whether passed tests ``(strict=False)`` should be marked as
    ``XPASS`` or with ``strict=True`` as ``FAIL``.

Let’s take a look at an example:

.. code-block:: python
   :emphasize-lines: 8-15, 18-22, 25-

    import pytest
    from packaging.version import parse

    import items
    from items import Item


    @pytest.mark.xfail(
        parse(items.__version__).minor < 2,
        reason="The comparison with < is not yet supported in version 0.1.x.",
    )
    def test_less_than():
        i1 = Item("Update pytest section")
        i2 = Item("Update cibuildwheel section")
        assert i1 < i2


    @pytest.mark.xfail(reason="Feature #17: not implemented yet")
    def test_xpass():
        i1 = Item("Update pytest section")
        i2 = Item("Update pytest section")
        assert i1 == i2


    @pytest.mark.xfail(reason="Feature #17: not implemented yet", strict=True)
    def test_xfail_strict():
        i1 = Item("Update pytest section")
        i2 = Item("Update pytest section")
        assert i1 == i2

We have three tests here: one that we know will fail, and two that we know will
pass. These tests demonstrate both the failing and passing of using ``xfail``
and the effects of using ``strict``. The first example also uses the optional
``condition`` :term:`parameter`, which works like ``skipif``’s conditions. And
this is what the result looks like:

.. code-block::

    pytest -v -ra tests/test_xfail.py
    ============================= test session starts ==============================
    ...
    collected 3 items

    tests/test_xfail.py::test_less_than XFAIL (The comparison with < is ...) [ 33%]
    tests/test_xfail.py::test_xpass XPASS (Feature #17: not implemented yet) [ 66%]
    tests/test_xfail.py::test_xfail_strict FAILED                            [100%]

    =================================== FAILURES ===================================
    ______________________________ test_xfail_strict _______________________________
    [XPASS(strict)] Feature #17: not implemented yet
    =========================== short test summary info ============================
    XFAIL tests/test_xfail.py::test_less_than - The comparison with < is not yet supported in version 0.1.x.
    XPASS tests/test_xfail.py::test_xpass Feature #17: not implemented yet
    FAILED tests/test_xfail.py::test_xfail_strict
    =================== 1 failed, 1 xfailed, 1 xpassed in 0.02s ====================

Tests labelled with ``xfail``:

- Failed tests are displayed with ``XFAIL``.
- Passed tests with ``strict=False`` result in ``XPASSED``.
- Passed tests with ``strict=True`` result in ``FAILED``.

If a test fails that is marked with ``xfail``, which means it is output with
``XFAIL``, we were right in assuming that the test will fail.

For tests that were marked ``xfail`` but actually passed, there are two
possibilities: If they are supposed to result in ``XFAIL``, then you should keep
your hands off strictly. If, on the other hand, they should result in
``FAILED``, then set ``strict``. You can either set ``strict`` as an option for
the ``xfail`` marker, as we have done in this example, or you can also set it
globally with the setting ``xfail_strict=True`` in the pytest configuration file
:file:`pytest.ini`.

A pragmatic reason to always use ``xfail_strict=True`` is that we usually take a
closer look at all failed tests. And so we also look at the cases in which the
expectations of the test do not match the result.

``xfail`` can be very helpful if you are working in test-driven development and
you are writing test cases that you know are not yet implemented but that you
want to implement soon. Leave the ``xfail`` tests on the feature branch in which
the function is implemented.

Or something breaks, one or more tests fail, and you can’t work on fixing it
right away. Marking the tests as ``xfail``, ``strict=true`` with the error/issue
report ID in reason is a good way to keep the test running and not forget about
it.

However, if you are just brainstorming about the behaviours of your application,
you should not write tests and mark them with ``xfail`` or ``skip`` yet: here I
would recommend :abbr:`YAGNI (‘You Aren’t Gonna Need It’)`. Always implement
things only when they are actually needed and never when you only suspect that
you will need them.

.. tip::
   * You should set :samp:`xfail_strict = True` in :file:`pytest.ini` to turn
     all ``XPASSED`` results into ``FAILED``.
   * You should also always use :samp:`-ra` or at least :samp:`-rxX` to display
     the reason.
   * And finally, you should specify an error number in ``reason``.
   * ``pytest --runxfail`` basically ignores the ``xfail`` markers. This is very
     useful in the final stages of pre-production testing.

.. _select-tests-with-markers:

Selection of tests with your own markers
----------------------------------------

You can think of your own markers as tags or labels. They can be used to select
tests that should be executed or skipped.

Let’s say we want to label some of our tests with ``smoke``. Segmenting a subset
of tests into a smoke test suite is a common practice to be able to run a
representative set of tests that can quickly tell us if anything is wrong with
any of the main systems. In addition, we will label some of our tests with
``exception`` – those that check for expected exceptions:

.. code-block:: python
   :emphasize-lines: 6

    import pytest

    from items import InvalidItemId, Item


    @pytest.mark.smoke
    def test_start(items_db):
        """
        Change state from ‘todo’ to ‘in progress’
        """
        i = items_db.add_item(Item("Update pytest section", state="todo"))
        items_db.start(i)
        s = items_db.get_item(i)
        assert s.state == "in progress"

Now we should be able to select only this test by using the ``-m smoke`` option:

.. code-block:: pytest

    $ pytest -v -m smoke tests/test_start.py
    ============================= test session starts ==============================
    ...
    collected 2 items / 1 deselected / 1 selected

    tests/test_start.py::test_start PASSED                                   [100%]

    =============================== warnings summary ===============================
    tests/test_start.py:6
      /Users/veit/items/tests/test_start.py:6: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
        @pytest.mark.smoke

    -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
    ================== 1 passed, 1 deselected, 1 warning in 0.00s ==================

Now we were only able to run one test, but we also received a warning:
``PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?`` It
helps to avoid typos. pytest wants us to register custom markers by adding a
marker section to :file:`pytest.ini`, for example:

.. code-block:: ini

    [pytest]
    markers =
        smoke: Small subset of all tests

Now pytest no longer warns us of an unknown marker:

.. code-block::
   :emphasize-lines: 4

    $ pytest -v -m smoke tests/test_start.py
    ============================= test session starts ==============================
    ...
    configfile: pytest.ini
    collected 2 items / 1 deselected / 1 selected

    tests/test_start.py::test_start PASSED                                   [100%]

    ======================= 1 passed, 1 deselected in 0.00s ========================

Let's do the same with the ``exception`` marker for ``test_start_non_existent``.

#. First, we register the marker in :file:`pytest.ini`:

   .. code-block:: ini
      :emphasize-lines: 4

      [pytest]
      markers =
          smoke: Small subset of tests
          exception: Only run expected exceptions

#. Then we add the marker to the test:

   .. code-block:: python
      :emphasize-lines: 1

      @pytest.mark.exception
      def test_start_non_existent(items_db):
          """
          Shouldn’t start a non-existent item.
          """
          # any_number will be invalid, db is empty
          any_number = 44

          with pytest.raises(InvalidItemId):
              items_db.start(any_number)

#. Finally, we run the test with ``-m exception``:

   .. code-block:: pytest

      $ pytest -v -m exception tests/test_start.py
      ============================= test session starts ==============================
      ...
      configfile: pytest.ini
      collected 2 items / 1 deselected / 1 selected

      tests/test_start.py::test_start_non_existent PASSED                      [100%]

      ======================= 1 passed, 1 deselected in 0.01s ========================

Markers for files, classes and parameters
-----------------------------------------

With the tests in :file:`test_start.py`, we have added
:samp:`@pytest.mark.{MARKER_NAME}` decorators to test functions. We can also add
markers to entire files or classes to mark multiple tests, or go into
:term:`parameterised <Parameter>` tests and mark individual parameterisations.
We can even set multiple markers on a single test. First, we set in
:file:`test_finish.py` with a file-level marker:

.. code-block:: python
   :emphasize-lines: 5

   import pytest

   from items import Item

   pytestmark = pytest.mark.finish

If pytest sees a ``pytestmark`` attribute in a test module, it will apply the
marker(s) to all tests in that module. If you want to apply more than one marker
to the file, you can use a list form: :samp:`pytestmark =
[pytest.mark.{MARKER_ONE}, pytest.mark.{MARKER_TWO}]`.

Another way to mark multiple tests at the same time is to have tests in a class
and use markers at class level:

.. code-block:: python
   :emphasize-lines: 1

   @pytest.mark.smoke
   class TestFinish:
       def test_finish_from_todo(self, items_db):
           i = items_db.add_item(Item("Update pytest section", state="todo"))
           items_db.finish(i)
           s = items_db.get_item(i)
           assert s.state == "done"

       def test_finish_from_in_prog(self, items_db):
           i = items_db.add_item(
               Item("Update pytest section", state="in progress")
           )
           items_db.finish(i)
           s = items_db.get_item(i)
           assert s.state == "done"

       def test_finish_from_done(self, items_db):
           i = items_db.add_item(Item("Update pytest section", state="done"))
           items_db.finish(i)
           s = items_db.get_item(i)
           assert s.state == "done"

The test class :class:`TestFinish` is labelled with ``@pytest.mark.smoke``. If
you mark a test class in this way, every test method in the class will be
labelled with the same marker.

We can also mark only certain test cases of a :term:`parameterised <Parameter>`
test:

.. code-block:: python
   :emphasize-lines: 5

   @pytest.mark.parametrize(
       "states",
       [
           "todo",
           pytest.param("in progress", marks=pytest.mark.smoke),
           "done",
       ],
   )
   def test_finish(items_db, start_state):
       i = items_db.add_item(Item("Update pytest section", state=states))
       items_db.finish(i)
       s = items_db.get_item(i)
       assert s.state == "done"

The :func:`test_finish` function is not directly marked, but only one of its
:term:`parameters <Parameter>`: :samp:`pytest.param("in progress",
marks=pytest.mark.smoke)`. You can use more than one marker by using the list
form:
:samp:`marks=[pytest.mark.{ONE}, pytest.mark.{TWO}]`. If you want to mark all
test cases of a :term:`parameterised <Parameter>` test, insert the marker either
above or below the decorator ``parametrize``, as with a normal function.

The previous example referred to function :term:`parameterisation <Parameter>`.
However, you can also mark fixtures in the same way:

.. code-block:: python
   :emphasize-lines: 8-9, 12

   @pytest.fixture(
       params=[
           "todo",
           pytest.param("in progress", marks=pytest.mark.smoke),
           "done",
       ]
   )
   def start_state_fixture(request):
       return request.param


   def test_finish(items_db, start_state_fixture):
       i = items_db.add_item(
           Item("Update pytest section", state=start_state_fixture)
       )
       items_db.finish(i)
       s = items_db.get_item(i)
       assert s.state == "done"

If you want to add more than one marker to a function, you can simply stack
them. For example, :func:`test_finish_non_existent` is marked with both
``@pytest.mark.smoke`` and ``@pytest.mark.exception``:

.. code-block:: python
   :emphasize-lines: 4-5

   from items import InvalidItemId, Item


   @pytest.mark.smoke
   @pytest.mark.exception
   def test_finish_non_existent(items_db):
       i = 44  # any_number will be invalid, db is empty
       with pytest.raises(InvalidItemId):
           items_db.finish(i)

We have added a number of markers to :file:`test_finish.py` in various ways. We
use the markers to select the tests to be executed instead of a test file:

.. code-block:: pytest

   $ cd tests
   $ tests % pytest -v -m exception
   ============================= test session starts ==============================
   ...
   configfile: pytest.ini
   collected 36 items / 34 deselected / 2 selected

   test_finish.py::test_finish_non_existent PASSED                          [ 50%]
   test_start.py::test_start_non_existent PASSED                            [100%]

   ======================= 2 passed, 34 deselected in 0.07s =======================

Markers together with ``and``, ``or``, ``not`` and ``()``
---------------------------------------------------------

We can logically combine markers to select tests, just like we used ``-k``
together with keywords to select test cases in a :ref:`test suite <keyword>`. So
we can only select the ``finish`` tests that deal with ``exception``:

.. code-block:: pytest

   $ pytest -v -m "finish and exception"
   ============================= test session starts ==============================
   ...
   configfile: pytest.ini
   collected 36 items / 35 deselected / 1 selected

   test_finish.py::test_finish_non_existent PASSED                          [100%]

   ======================= 1 passed, 35 deselected in 0.08s =======================

We can also use all logical operations together:

.. code-block:: pytest

   $ pytest -v -m "(exception or smoke) and (not finish)"
   ============================= test session starts ==============================
   ...
   configfile: pytest.ini
   collected 36 items / 34 deselected / 2 selected

   test_start.py::test_start PASSED                                         [ 50%]
   test_start.py::test_start_non_existent PASSED                            [100%]

   ======================= 2 passed, 34 deselected in 0.08s =======================

Finally, we can also combine markers and keywords for the selection, for
example, to perform smoke tests that are not part of the :class:`TestFinish`
class:

.. code-block:: console

   $ pytest -v -m smoke -k "not TestFinish"
   ============================= test session starts ==============================
   ...
   configfile: pytest.ini
   collected 36 items / 33 deselected / 3 selected

   test_finish.py::test_finish[in progress] PASSED                          [ 33%]
   test_finish.py::test_finish_non_existent PASSED                          [ 66%]
   test_start.py::test_start PASSED                                         [100%]

   ======================= 3 passed, 33 deselected in 0.07s =======================

When using markers and keywords, note that the names of the markers must be
complete with the :samp:`-m {MARKERNAME}` option, while keywords are more of a
substring with the :samp:`-k {KEYWORD}` option.

``--strict-markers``
--------------------

Usually we get a warning if a marker is not registered. If we want this warning
to be an error instead, we can use the ``--strict-markers`` option. This has two
advantages:

#. The error is already output when the tests to be executed are collected and
   not at runtime. If you have a test suite that takes longer than a few
   seconds, you will appreciate getting this feedback quickly.
#. Secondly, errors are sometimes easier to recognise than warnings, especially
   in systems with :term:`continuous integration`.

.. tip::
   It is therefore recommended to always use ``--strict-markers``. However,
   instead of entering the option again and again, you can add
   ``--strict-markers`` to the ``addopts`` section of :file:`pytest.ini`:

   .. code-block:: ini
      :emphasize-lines: 3-4

      [pytest]
      ...
      addopts =
          --strict-markers

.. _marker_fixtures_combined:

Combining markers with fixtures
-------------------------------

Markers can be used in conjunction with fixtures, plugins and hook functions.
The built-in markers require :term:`parameters <Parameter>`, while the custom
markers we have used so far do not require parameters. Let’s create a new marker
called ``num_items`` that we can pass to the ``items_db`` fixture. The
``items_db`` fixture currently cleans up the database for each test that wants
to use it:

.. code-block:: python

   @pytest.fixture(scope="function")
   def items_db(session_items_db):
       db = session_items_db
       db.delete_all()
       return db

For example, if we want to have four items in the database when our test starts,
we can simply write a different but similar fixture:

.. code-block:: python

   @pytest.fixture(scope="session")
   def items_list():
       """List of different Item objects"""
       return [
           items.Item("Add Python 3.12 static type improvements", "veit", "todo"),
           items.Item("Add tips for efficient testing", "veit", "wip"),
           items.Item("Update cibuildwheel section", "veit", "done"),
           items.Item("Add backend examples", "veit", "done"),
       ]


   @pytest.fixture(scope="function")
   def populated_db(items_db, items_list):
       """ItemsDB object populated with 'items_list'"""
       for i in items_list:
           items_db.add_item(i)
       return items_db

We could then use the original fixture for tests, which provides an empty
database, and the new fixture for tests, which contains a database with four
items:

.. code-block:: python

   def test_zero_item(items_db):
       assert items_db.count() == 0


   def test_four_items(populated_db):
       assert populated_db.count() == 4

We now have the option of testing either zero or four items in the database. But
what if we want to have no, four or 13 items? Then we don’t want to write a new
fixture each time. Markers allow us to tell a test how many items we want to
have. This requires three steps:

#. First, we define three different tests in :file:`test_items.py` with our
   marker ``@pytest.mark.num_items``:

   .. code-block:: python

      @pytest.mark.num_items
      def test_zero_item(items_db):
          assert items_db.count() == 0


      @pytest.mark.num_items(4)
      def test_four_items(items_db):
          assert items_db.count() == 4


      @pytest.mark.num_items(13)
      def test_thirteen_items(items_db):
          assert items_db.count() == 13

#. We must then declare this marker in the :file:`pytest.ini` file:

   .. code-block:: ini
      :emphasize-lines: 4

      [pytest]
      markers =
          ...
          num_items: Number of items to be pre-filled for the items_db fixture

#. Now we modify the ``items_db`` fixture in the :file:`conftest.py` file to be
   able to use the marker. To avoid having to hard-code the item information, we
   will use the Python package `Faker <https://faker.readthedocs.io/>`_, which
   we can install with ``python -m pip install faker``:

   .. code-block:: python
      :linenos:
      :emphasize-lines: 5, 12-

      import os
      from pathlib import Path
      from tempfile import TemporaryDirectory

      import faker
      import pytest

      import items

      ...


      @pytest.fixture(scope="function")
      def items_db(session_items_db, request, faker):
          db = session_items_db
          db.delete_all()
          # Support for random selection "@pytest.mark.num_items({NUMBER})`.
          faker.seed_instance(99)
          m = request.node.get_closest_marker("num_items")
          if m and len(m.args) > 0:
              num_items = m.args[0]
              for _ in range(num_items):
                  db.add_item(
                      Item(summary=faker.sentence(), owner=faker.first_name())
                  )
          return db

   There are a lot of changes here that we want to go through now.

   Line 13
    We have added ``request`` and ``faker`` to the list of ``items_db``
    :term:`parameters <Parameter>`.
   Line 18
    This sets the randomness of faker so that we get the same data every time.
    We are not using faker here for very random data, but to avoid having to
    invent data ourselves.
   Line 19
    Here we use ``request``, more precisely ``request.node`` for the pytest
    representation of a test. ``get_closest_marker('num_items')`` returns a
    marker object if the test is marked with ``num_items``, otherwise it returns
    ``None``. The :func:`get_closest_marker` function returns the marker closest
    t545o the test, which is usually what we want.
   Line 20
    The expression is true if the test is marked with ``num_items`` and an
    argument is given. The additional ``len`` check is there so that if someone
    accidentally just uses ``pytest.mark.num_items`` without specifying the
    number of items, this part is skipped.
   Line 22–24
    Once we know how many items we need to create, we let Faker create some data
    for us. Faker provides the Faker fixture.

    * For the ``summary`` field, the :func:`faker.sentence` method works.
    * The :func:`faker.first_name` method works for the  ``Owner`` field.

    .. seealso::
       * There are many other options that you can use with Faker. Have a look
         at the `Faker documentation <https://faker.readthedocs.io/>`_.

       * In addition to Faker, there are other libraries that provide fake data,
         see :ref:`Fake plugins <fake_plugins>`.

Let’s run the tests now to make sure everything is working properly:

.. code-block:: pytest

   $ pytest -v -s test_items.py
   ============================= test session starts ==============================
   ...
   configfile: pytest.ini
   plugins: Faker-19.10.0
   collected 3 items

   test_items.py::test_zero_item PASSED
   test_items.py::test_four_items PASSED
   test_items.py::test_thirteen_items PASSED

   ============================== 3 passed in 0.09s ===============================

.. note::
   You can add a ``print`` statement to :func:`test_four_items` to get an
   impression of what the data from Faker looks like:

   .. code-block:: python
      :emphasize-lines: 4-

      @pytest.mark.num_items(4)
      def test_four_items(items_db):
          assert items_db.count() == 4
          print()
          for i in items_db.list_items():
              print(i)

   You can then call the tests in :file:`test_items.py` again:

   .. code-block:: pytest
      :emphasize-lines: 10-13

      $ pytest -v -s test_items.py
      ============================= test session starts ==============================
      ...
      configfile: pytest.ini
      plugins: Faker-19.10.0
      collected 3 items

      test_items.py::test_zero_item PASSED
      test_items.py::test_four_items
      Item(summary='Herself outside discover card beautiful rock.', owner='Alyssa', state='todo', id=1)
      Item(summary='Bed perhaps current reveal open society small.', owner='Lynn', state='todo', id=2)
      Item(summary='Charge produce sure full water.', owner='Allison', state='todo', id=3)
      Item(summary='Light I especially account.', owner='James', state='todo', id=4)
      PASSED
      test_items.py::test_thirteen_items PASSED

      ============================== 3 passed in 0.09s ===============================

Generating markers
------------------

Suppose you have a test suite that marks tests for specific platforms, namely
``pytest.mark.darwin``, ``pytest.mark.win32``, and so on, and you also have
tests that run on all platforms and do not have a specific marker. If you are
looking for a way to run only the tests for your specific platform, you can use
the following:

.. code-block:: python
   :caption: conftest.py

   import sys

   import pytest

   ALL = {"win32", "darwin", "linux"}


   def pytest_setup(item):
       supported_platforms = ALL.intersection(
           mark.name for mark in item.iter_markers()
       )
       pf = sys.platform
       if supported_platforms and pf not in supported_platforms:
           pytest.skip(f"cannot run on platform {pf}")

This means that tests are skipped if they have been specified for another
platform. Now let's create a small test file to show what this looks like:

.. code-block:: python
   :caption: test_platform.py

   import pytest


   def test_foo_everywhere():
       pass


   @pytest.mark.win32
   def test_foo_on_win32():
       pass


   @pytest.mark.darwin
   def test_foo_on_darwin():
       pass


   @pytest.mark.linux
   def test_foo_on_linux():
       pass

Now we can run pytest and see the reasons for the skipped tests:

.. code-block:: pytest

   $ uv run pytest -rs tests/test_platform.py
   ============================= test session starts ==============================
   platform darwin -- Python 3.14.0b4, pytest-8.4.1, pluggy-1.6.0
   ...
   collected 4 items

   tests/test_platform.py ..ss                                              [100%]

   =========================== short test summary info ============================
   SKIPPED [2] tests/conftest.py:20: cannot run on platform darwin
   ========================= 2 passed, 2 skipped in 0.03s =========================

or more specifically:

.. code-block:: pytest

   $ uv run pytest -m darwin -rs tests/test_platform.py
   ============================= test session starts ==============================
   platform darwin -- Python 3.14.0b4, pytest-8.4.1, pluggy-1.6.0
   ...
   collected 4 items / 3 deselected / 1 selected

   tests/test_platform.py .                                                 [100%]

   ======================= 1 passed, 3 deselected in 0.02s ========================

Markers based on test names
---------------------------

Alternatively, markers can also be specified using the names of the test
functions by implementing a hook that automatically defines markers:

.. code-block:: python
   :caption: test_platform.py

   def test_foo_everywhere():
       pass


   def test_foo_on_win32():
       pass


   def test_foo_on_darwin():
       pass


   def test_foo_on_linux():
       pass

Now we dynamically define three markers in :file:`conftest.py` in
`pytest_collection_modifyitems
<https://docs.pytest.org/en/latest/reference/reference.html#pytest.hookspec.pytest_collection_modifyitems>`_:

.. code-block:: python
   :caption: conftest.py

   import pytest


   def pytest_collection_modifyitems(items):
       for item in items:
           if "win32" in item.nodeid:
               item.add_marker(pytest.mark.win32)
           elif "darwin" in item.nodeid:
               item.add_marker(pytest.mark.darwin)
           elif "linux" in item.nodeid:
               item.add_marker(pytest.mark.linux)

Now we can use the ``-m`` option to select a set:

.. code-block:: pytest

   $ uv run pytest -m darwin
   ============================= test session starts ==============================
   platform darwin -- Python 3.14.0, pytest-9.0.1, pluggy-1.6.0
   ...
   collected 4 items / 3 deselected / 1 selected

   tests/test_platform.py .                                                 [100%]

   ======================= 1 passed, 3 deselected in 0.00s ========================

List markers
------------

We’ve already covered a lot of markers: the built-in markers ``skip``,
``skipif`` and ``xfail``, our own markers ``smoke``, ``exception``, ``finish``
and ``num_items`` and there are also a few more built-in markers. And when we
start using :doc:`plugins`, more markers may be added. To list all available
markers with descriptions and :term:`parameters <Parameter>`, you can run
``pytest --markers``:

.. code-block:: pytest

   $ pytest --markers
   @pytest.mark.exception: Only run expected exceptions

   @pytest.mark.finish: Only run finish tests

   @pytest.mark.smoke: Small subset of all tests

   @pytest.mark.num_items: Number of items to be pre-filled for the items_db fixture

   @pytest.mark.filterwarnings(warning): add a warning filter to the given test. see https://docs.pytest.org/en/stable/how-to/capture-warnings.html#pytest-mark-filterwarnings
   ...

This is a very handy feature that allows us to quickly search for markers and a
good reason to add useful descriptions to our own markers.
