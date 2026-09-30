Test libraries
==============

:doc:`unittest` and :doc:`pytest/index` support the following testing concepts:

.. glossary::

   Test Case
       tests a single scenario.

   Test Fixture
       is a consistent test environment.

   Test Suite
       is a collection of several :term:`test cases <Test case>`.

   Test Runner
       runs through a :term:`test suite` and displays the results.

:doc:`tox` also provides various environments in which tests can be run.
Finally, :doc:`hypothesis` supports you with :term:`black-box testing
<Black-box test>`.

.. toctree::
   :titlesonly:
   :hidden:

   unittest
   pytest/index
   tox
   mock/index
   hypothesis
