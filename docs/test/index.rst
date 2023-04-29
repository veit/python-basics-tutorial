Testing
=======

Basically, a distinction is made between static and dynamic test procedures.

.. glossary::

   Static test procedures
    are used to check the source code, but it is not executed. They are divided
    into

    * `Reviews <https://en.wikipedia.org/wiki/Software_review>`_ and
    * `Static program analysis
      <https://en.wikipedia.org/wiki/Static_program_analysis>`_

      There are various Python packages that can help you with static program
      analysis, including including
      :doc:`jupyter-tutorial:productive/qa/flake8`,
      :doc:`jupyter-tutorial:productive/qa/pysa` and
      :doc:`jupyter-tutorial:productive/qa/wily`.

   Dynamic test procedures
    are used to find errors when executing the source code. Thereby a
    distinction is made between whitebox and backbox tests.

    Whitebox tests
        are developed with knowledge of the source code and the software
        structure. Various modules are available in Python:

        :doc:`unittest`
            supports you in automating tests.
        :doc:`mock`
            allows you to create and use mock objects.
        :doc:`doctest`
            allows you to test tests written in Python docstrings.
        :doc:`tox`
            allows you to test in different environments.

    Black box tests
        are developed without knowledge of the source code. Besides
        :doc:`unittest`, :doc:`hypothesis` can also be used in Python for such
        tests.

.. seealso::
   * `Python Testing and Continuous Integration
     <http://carpentries-incubator.github.io/python-testing/>`_

.. toctree::
   :titlesonly:
   :hidden:

   unittest
   sqlite
   mock
   doctest
   hypothesis
   pytest
   tox
   unittest2
   coverage
