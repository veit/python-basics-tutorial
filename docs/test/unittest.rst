Unittest
========

Suppose you implemented the following method for adding:

.. literalinclude:: arithmetic.py
   :language: python
   :lines: 1,6
   :lineno-start: 1

… then you can test this method with a unittest.

#. To do this, first import your module and the unittest module:

   .. literalinclude:: test_arithmetic.py
      :language: python
      :lines: 1-2
      :lineno-start: 1

#. Afterwards, you can write a test method that exemplifies your addition
   method:

   .. literalinclude:: test_arithmetic.py
      :language: python
      :lines: 4-7
      :lineno-start: 4


#. So that the code can be executed from the command line, we add the following
   method:

   .. literalinclude:: test_arithmetic.py
      :language: python
      :lines: 21-22
      :lineno-start: 21

#. Finally, all tests in :download:`test_arithmetic.py` can be executed with:

   .. code-block:: console

      $ python test_arithmetic.py
      ....
      ----------------------------------------------------------------------
      Ran 4 tests in 0.000s

      OK

   … or a little more verbose:

   .. code-block:: console

      $ python test_arithmetic.py -v
      test_addition (__main__.TestArithmetic) ... ok
      test_division (__main__.TestArithmetic) ... ok
      test_multiplication (__main__.TestArithmetic) ... ok
      test_subtraction (__main__.TestArithmetic) ... ok

      ----------------------------------------------------------------------
      Ran 4 tests in 0.000s

      OK

.. seealso::
   * :doc:`python3:library/unittest`
