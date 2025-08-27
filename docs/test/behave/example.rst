Example
=======

#. After installing behave, we can create a file called :file:`install.feature`
   in the :file:`features` directory with the following content:

   .. code-block:: gherkin

      Feature: showing off behave

        Scenario: run a simple test
           Given we have behave installed
            When we implement a test
            Then behave will test it for us!

   .. seealso::
      `Features <https://behave.readthedocs.io/en/latest/tutorial/#features>`_

#. Next, we create the file :file:`install.py` in the directory
   :file:`features/steps`:

   .. code-block:: python

      from behave import *


      @given("we have behave installed")
      def step_impl(context):
          pass


      @when("we implement a test")
      def step_impl(context):
          assert True is not False


      @then("behave will test it for us")
      def step_impl(context):
          assert context.failed is False

   .. seealso::
      `Python Step Implementations
      <https://behave.readthedocs.io/en/latest/tutorial/#python-step-implementations>`_

#. Call ``behave``

   .. code-block:: console

      $ behave
      USING RUNNER: behave.runner:Runner
      Feature: showing off behave # features/install.feature:1

        Scenario: run a simple test        # features/install.feature:3
          Given we have behave installed   # features/steps/install.py:3 0.000s
          When we implement a test         # features/steps/install.py:7 0.000s
          Then behave will test it for us  # features/steps/install.py:11 0.000s

      1 feature passed, 0 failed, 0 skipped
      1 scenario passed, 0 failed, 0 skipped
      3 steps passed, 0 failed, 0 skipped
      Took 0min 0.000s
