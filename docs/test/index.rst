Testing
=======

Concepts
--------

.. glossary::
   Test Case
       tests a single scenario.

   Test Fixture
       is a consistent test environment.

       .. seealso::
          `pytest fixtures <https://docs.pytest.org/en/stable/fixture.html>`_

   Test Suite
       is a collection of several :term:`test cases <Test Case>`.

   Test Runner
       runs through a :term:`test suite <Test Suite>` and displays the results.

Python test modules
-------------------

Python contains several built-in modules for testing your code: :doc:`unittest`,
:doc:`mock` and :doc:`doctest`.

.. toctree::
   :titlesonly:
   :hidden:

   unittest
   mock
   doctest

Other test tools
----------------

There are other testing tools for Python that can significantly simplify testing:

:doc:`hypothesis`
    allows you to write tests that are parameterised from a source of examples.
:doc:`pytest`
    simplifies the writing of tests.
:doc:`tox`
    allows testing in different environments.

.. toctree::
   :titlesonly:
   :hidden:

   hypothesis
   pytest
   tox
