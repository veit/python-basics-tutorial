Unittest
========

:doc:`unittest <python3:library/unittest>` helps you in test automation with
shared setup and tear down code as well as aggregation and independence of
tests.

For this it provides the following test concepts:

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

Example
-------

Suppose you have implemented the following method for adding in the module
:download:`test_arithmetic.py`:

.. literalinclude:: arithmetic.py
   :language: python
   :lines: 1-6
   :lineno-start: 1

… then you can test this method with a unittest.

#. To do this, first import your module and the unittest module:

   .. literalinclude:: test_arithmetic.py
      :language: python
      :lines: 1-3
      :lineno-start: 1

#. Afterwards, you can write a test method that exemplifies your addition
   method:

   .. literalinclude:: test_arithmetic.py
      :language: python
      :lines: 6-8
      :lineno-start: 6


#. In order to be able to import the unit tests into other modules as well, you
   should add the following lines:

   .. literalinclude:: test_arithmetic.py
      :language: python
      :lines: 23-24
      :lineno-start: 23

#. Finally, all tests in :download:`test_arithmetic.py` can be executed with:

   .. tab:: Linux/macOS

      .. code-block:: console

         $ bin/python test_arithmetic.py
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

   … or a little more verbose:

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

         C:> Scripts\python test_arithmetic.py -v
         test_addition (__main__.TestArithmetic) ... ok
         test_division (__main__.TestArithmetic) ... ok
         test_multiplication (__main__.TestArithmetic) ... ok
         test_subtraction (__main__.TestArithmetic) ... ok

         ----------------------------------------------------------------------
         Ran 4 tests in 0.000s

         OK

.. seealso::
   * :doc:`python3:library/unittest`
