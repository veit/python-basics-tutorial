Examples
========

You can simply create a file :file:`test_one.py` with the following content:

.. literalinclude:: test_one.py
   :language: python
   :lineno-start: 1

The ``test_sorted()`` function is recognised by pytest as a test function
because it starts with :samp:`test_` and is in a file that starts with
:samp:`test_`. When the test is executed, the ``assert`` statement determines
whether the test succeeded or failed. ``assert`` is a Python built-in keyword
and raises an ``assertionError`` exception if the expression after ``assert`` is
false. Any uncaught exception thrown within a test will cause the test to fail.

Execute pytest
--------------

.. code-block:: pytest

   $ cd docs/test/pytest
   $ pytest test_one.py
   ============================= test session starts ==============================
   …
   collected 1 item

   test_one.py .                                                            [100%]

   ============================== 1 passed in 0.00s ===============================

The dot after :file:`test_one.py` means that a test has been performed and
passed. ``[100%]`` is a percentage display that indicates how many tests of the
test session have been performed so far. As there is only one test, one test
corresponds to 100% of the tests. If you need more information, you can use
``-v`` or ``--verbose``:

.. code-block:: pytest

   $ pytest -v test_one.py
   ============================= test session starts ==============================
   …
   collected 1 item

   test_one.py::test_sorted PASSED                                          [100%]

   ============================== 1 passed in 0.00s ===============================

:file:`test_two.py` on the other hand, fails:

.. code-block:: pytest

   $ pytest test_two.py
   collected 1 item

   test_two.py F                                                            [100%]

   =================================== FAILURES ===================================
   _________________________________ test_failing _________________________________

       def test_failing():
   >       assert sorted([4, 2, 1, 3]) == [0, 1, 2, 3]
   E       assert [1, 2, 3, 4] == [0, 1, 2, 3]
   E         At index 0 diff: 1 != 0
   E         Use -v to get more diff

   test_two.py:2: AssertionError
   =========================== short test summary info ============================
   FAILED test_two.py::test_failing - assert [1, 2, 3, 4] == [0, 1, 2, 3]
   ============================== 1 failed in 0.03s ===============================

The failed test, ``test_in``, gets its own section to show us why it failed. And
``pytest`` tells us exactly what the first error is. This additional section is
called traceback. That’s already a lot of information, but there’s a line that
says we get the full diff with ``-v``. Let’s do that:

.. code-block:: pytest

   $ pytest -v test_two.py
   ============================= test session starts ==============================
   …
   collected 1 item

   test_two.py::test_failing FAILED                                         [100%]

   =================================== FAILURES ===================================
   _________________________________ test_failing _________________________________

       def test_failing():
   >       assert sorted([4, 2, 1, 3]) == [0, 1, 2, 3]
   E       assert [1, 2, 3, 4] == [0, 1, 2, 3]
   E         At index 0 diff: 1 != 0
   E         Full diff:
   E         - [0, 1, 2, 3]
   E         ?  ---
   E         + [1, 2, 3, 4]
   E         ?         +++

   test_two.py:2: AssertionError
   =========================== short test summary info ============================
   FAILED test_two.py::test_failing - assert [1, 2, 3, 4] == [0, 1, 2, 3]
   ============================== 1 failed in 0.03s ===============================

``pytest`` adds ``+`` and ``-`` signs to show us exactly the differences.

So far we have run ``pytest`` with the command :samp:`pytest {FILE}.py`. Now
let's run ``pytest`` in a few more ways. If you don’t specify any files or
directories, pytest will look for tests in the current working directory and
subdirectories; more specifically, it will look for ``.py`` files that start
with :file:`test_` or end with :file:`_test`. If you start pytest in the
directory :file:`docs/test/pytest` without options, two files with tests will be
run:

.. code-block:: pytest

   $ pytest --tb=no
   ============================= test session starts ==============================
   …

   test_one.py .                                                            [ 50%]
   test_two.py F                                                            [100%]

   =========================== short test summary info ============================
   FAILED test_two.py::test_failing - assert [1, 2, 3, 4] == [0, 1, 2, 3]
   ========================= 1 failed, 1 passed in 0.00s ==========================

I have also used the ``--tb=no`` option to disable traceback as we don’t really
need the full output at the moment.

We can also specify a test function within a test file to be executed by adding :samp:`::test_{name}` to the file name:

.. code-block:: pytest

   $ pytest -v test_one.py::test_sorted
   ============================= test session starts ==============================
   …
   collected 1 item

   test_one.py::test_sorted PASSED                                          [100%]

   ============================== 1 passed in 0.00s ===============================

Test results
------------

The possible results of a test function include

``PASSED (.)``
    The test was performed successfully.
``FAILED (F)``
    The test was not performed successfully.
``SKIPPED (s)``
    The test was skipped.
``XFAIL (x)``
    The test should not pass, but was performed and failed.
``XPASS (X)``
    The test was marked ``xfail``, but it ran and passed.
``ERROR (E)``
    An exception occurred during the execution of a :doc:`fixtures`, but not
    during the execution of a test function.
