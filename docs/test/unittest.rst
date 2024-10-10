Unittest
========

:doc:`unittest <python3:library/unittest>` supports you in test automation with
shared setup and tear-down code as well as aggregation and independence of
tests.

It provides the following test concepts:

.. glossary::

   Test Case
       tests a single scenario.

   Test Fixture
       is a consistent test environment.

       .. seealso::
          * `pytest fixtures
            <https://docs.pytest.org/en/latest/explanation/fixtures.html>`_
          * `About fixtures
            <https://docs.pytest.org/en/latest/explanation/fixtures.html#about-fixtures>`_
          * `Fixtures reference
            <https://docs.pytest.org/en/latest/reference/fixtures.html>`_
          * `How to use fixtures
            <https://docs.pytest.org/en/latest/how-to/fixtures.html#how-to-fixtures>`_

   Test Suite
       is a collection of several :term:`test cases <Test Case>`.

   Test Runner
       runs through a :term:`Test Suite` and displays the results.

Example
-------

Suppose you have implemented the following add method in the
:download:`test_arithmetic.py` module:

.. literalinclude:: arithmetic.py
   :language: python
   :lines: 1-6
   :lineno-start: 1

… then you can test this method with a Unittest.

#. To do this, you must first import your module and the unittest module:

   .. literalinclude:: test_arithmetic.py
      :language: python
      :lines: 1, 6
      :lineno-start: 1

#. Then you can write a test method that illustrates your addition method:

   .. literalinclude:: test_arithmetic.py
      :language: python
      :lines: 6-9
      :lineno-start: 6

#. In order to import the unittests into other modules, you should add the
   following lines:

   .. literalinclude:: test_arithmetic.py
      :language: python
      :lines: 23-24
      :lineno-start: 23

#. Finally, all tests in :download:`test_arithmetic.py` can be executed:

   .. tab:: Linux/macOS

      .. code-block:: console

         $ python test_arithmetic.py
         ....
         ----------------------------------------------------------------------
         Ran 4 tests in 0.000s

         OK

   .. tab:: Windows

      .. code-block:: ps1con

         C:> python test_arithmetic.py
         ....
         ----------------------------------------------------------------------
         Ran 4 tests in 0.000s

         OK

   … or a little more detailed:

   .. tab:: Linux/macOS

      .. code-block:: ps1con

         $ python test_arithmetic.py -v
         test_addition (__main__.TestArithmetic) ... ok
         test_division (__main__.TestArithmetic) ... ok
         test_multiplication (__main__.TestArithmetic) ... ok
         test_subtraction (__main__.TestArithmetic) ... ok

         ----------------------------------------------------------------------
         Ran 4 tests in 0.000s

         OK

   .. tab:: Windows

      .. code-block:: ps1con

         C:> python test_arithmetic.py -v
         test_addition (__main__.TestArithmetic) ... ok
         test_division (__main__.TestArithmetic) ... ok
         test_multiplication (__main__.TestArithmetic) ... ok
         test_subtraction (__main__.TestArithmetic) ... ok

         ----------------------------------------------------------------------
         Ran 4 tests in 0.000s

         OK

.. seealso::
   * :doc:`python3:library/unittest`
