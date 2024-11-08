Testing
=======

Basically, a distinction is made between static and dynamic test procedures.

.. glossary::

   Static test procedures
    are used to check the source code, but it’s not executed. They are divided
    into

    * :ref:`reviews <code_reviews>` and
    * `static program analysis
      <https://en.wikipedia.org/wiki/Static_program_analysis>`_

      There are several Python packages that can help you with static program
      analysis, including :doc:`Python4DataScience:productive/qa/flake8`,
      :doc:`Python4DataScience:productive/qa/pysa` and
      :doc:`Python4DataScience:productive/qa/wily`.

   Dynamic testing
    are used to find errors when executing the source code. A distinction is
    made between whitebox and backbox tests.

    Whitebox tests
        are developed with knowledge of the source code and the software
        structure. In Python, various modules are available:

        :doc:`unittest`
            supports you in automating tests.
        :doc:`mock`
            allows you to create and use mock objects.
        :doc:`../document/doctest`
            allows you to test tests written in Python docstrings.
        :doc:`tox`
            allows you to test in different environments.

    Blackbox tests
        are developed without knowledge of the source code. In addition to
        :doc:`unittest`, :doc:`hypothesis` can also be used in Python for such
        tests.

.. tip::
   `cusy seminar: Efficient testing with Python
   <https://cusy.io/en/our-training-courses/efficient-testing-with-python>`_

.. seealso::
   * `Python Testing and Continuous Integration
     <http://carpentries-incubator.github.io/python-testing/>`_

.. toctree::
   :titlesonly:
   :hidden:

   pytest/index
   unittest
   mock
   hypothesis
   tox
   glossary
