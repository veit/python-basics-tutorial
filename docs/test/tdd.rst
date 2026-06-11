Test-Driven Development
=======================

:term:`Test-Driven Development` (:term:`TDD`) is characterised by the fact that
tests for a function are written first, before the function is implemented. More
specifically, only as much code should be implemented as is necessary to pass
the tests.

Repeat this *‘test first, then implement’* process until the function meets your
current requirements.

This idea was introduced in the late 1990s by Kent Beck in his book
`‘Test-Driven Development: By Example’
<https://archive.org/details/est-driven-development-by-example/test-driven-development-by-example/>`_.
The three simple, repetitive steps have become known as *‘Red – Green –
Refactor’*:

#. Write tests for the next function to be added.
#. Write the function code until the test passes.
#. Refactor both the new and the old code to improve its structure.

TDD aims to ensure that the process implements a requirement more efficiently,
whilst also ensuring that it is thoroughly tested for the specific use case. No
time should be wasted implementing options and features simply in case they
might prove useful later on. You should get exactly what you need, when you need
it, and nothing more.

However, these three steps were a significant simplification, and so, at the end
of 2023, Kent Beck attempted to clear up some of the misunderstandings with
`Canon TDD <https://tidyfirst.substack.com/p/canon-tdd>`_. As in the Agile
Manifesto, people and interactions are prioritised over processes and tools:

    “If you’re doing something different than the following workflow & it works
    for you, congratulations! It’s not Canon TDD, but who cares? There’s no gold
    star for following these steps exactly.”

Only then does he outline the following five steps::

#. Test list

   All expected variants of the new behaviour are listed: *“This is the base
   case, and what should happen in this or that exceptional case.”* The aim here
   is to analyse the behaviour, not the software design or implementation.

   .. admonition:: Example: Calculating the mean
      :collapsible: closed

      For a mean calculation, the initial test list might look like this:

      * The base case is that the mean is calculated from a sequence, a list or
        an iterator.
      * A number of the appropriate type should be returned, which may also be
        an integer.
      * If the set or sequence is empty, an error message should be displayed.
      * If one or more elements are :doc:`../types/strings/index`, an attempt
        should be made to convert them into numbers of the appropriate type.
      * If the conversion of individual elements into numbers fails, an
        appropriate error message should be displayed.

#. Write a test

   You should write just one test, including *setup*, *invocation* and
   *assertion*. Although design decisions will be made whilst writing this test,
   they will primarily concern the interface, not the implementation itself.

   .. admonition:: Example: Calculating the mean
      :collapsible: closed

      The basic test might look like this:

      .. code-block:: python

         @pytest.mark.xfail(
             strict=True, raises=AssertionError, reason="Not implemented yet"
         )
         def test_mean_base():
             ls = [1, 2, 3]
             tp = tuple(ls)
             st = set(ls)
             assert mean(ls) == mean(tp) == mean(st) == 2

      We have simply defined that the function should be called :func:`mean` and
      that it can take a :doc:`../types/sequences-sets/lists`, a
      :doc:`../types/sequences-sets/tuples` or a
      :doc:`../types/sequences-sets/sets` as a parameter.

      By using the :doc:`decorator <../functions/decorators>`
      :func:`@pytest.mark.xfail`, we expect this test to fail initially.

      Next, we’ll write a minimal version of :func:`mean` that should cause our
      test to fail:

      .. code-block:: python

         def mean(se):
             pass

      .. code-block:: pytest

         $ uv run pytest -v test_mean.py
         ============================= test session starts ==============================
         ...

         test_mean.py::test_mean_base XFAIL (Not implemented yet)                 [100%]

         ============================== 1 xfailed in 0.08s ==============================

   Writing the test **before** the implementation has the following advantages:

   * The implementation is faster, as we already have code in the test to call
     the implementation.
   * This ensures that the test actually fails.

     With legacy code, we write a test for an existing behaviour. To ensure that
     the test can indeed fail, we then temporarily delete the implementation.
     Finally, we retrieve the implementation from version control.

   * The test forces us to change our perspective and focus on the interface for
     calling the code.
   * The test indicates to us when the implementation step is complete.

   With legacy code, writing tests becomes more difficult. Although you can also
   write a test for an existing behaviour here, passing the test does not tell
   you whether it can also fail. That is why we temporarily remove the
   implementation to ensure the test fails.

#. Passing the test

   Modify the code so that the test (and all previous tests) passes, and if you
   find that another test is required, add it to the test list.

   .. admonition:: Example: Calculating the mean
      :collapsible: closed

      Now let’s modify our :func:`mean` function so that our test passes:

      .. code-block:: python

           def mean(se):
               return sum(se) / len(se)

      We will now remove the ``pytest.mark.xfail`` decorator, as we expect the
      test to pass now:

      .. code-block:: pytest

         $ uv run pytest -v test_mean.py
         ============================= test session starts ==============================
         ...

         test_mean.py::test_mean_base PASSED                                      [100%]

         ============================== 1 passed in 0.15s ===============================

   .. warning::

       the past, mistakes were often made at this stage:

      * Deleting assertions so that the test passes
      * Copying values calculated by the function into the test function
      * Not ‘wearing two hats’ and trying to refactor at this stage

#. Optional: Refactoring

   Now is the time to make decisions regarding the implementation design.

   .. warning::

      Mistakes are also frequently made during this step:

      * Refactoring that goes beyond this behaviour
      * Premature abstraction: duplicates are merely indications and not a
        mandatory requirement for refactoring

#. Go back to 2 until the list is empty

   Test and implement until the desired behaviour is achieved.

.. note::
   We also use test-driven development when we use coding agents to assist us
   with software development:

   .. code-block:: md
      :caption: AGENTS.md

      - Use Test Driven Development (TDD) for all code you write. Write tests before writing the implementation code.
      - When you come across a bug or regression, think hard about writing a test and also how to create code that will prevent this from a happening again in the future.

   .. seealso::
      * :ref:`agentic-software-engineering:testing`
