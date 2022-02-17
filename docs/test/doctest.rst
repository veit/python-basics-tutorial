Doctest
=======

The Python module  :doc:`doctest <python3:library/doctest>` checks whether tests
specified in a docstring are fulfilled.

#. In :download:`arithmetic.py` you can add a docstring:

   .. literalinclude:: arithmetic.py
      :language: python
      :lines: 2-5
      :lineno-start: 2

#. Then you can test it with

   .. tab:: Linux/MacOS

      .. code-block:: console

       $ bin/python -m doctest arithmetic.py -v
       Trying:
           add(7,6)
       Expecting:
           13
       ok
       1 items had no tests:
           arithmetic
       1 items passed all tests:
          1 tests in arithmetic.add
       1 tests in 2 items.
       1 passed and 0 failed.
       Test passed.

   .. tab:: Windows

      .. code-block:: console

       C:> Scripts\python -m doctest arithmetic.py -v
       Trying:
           add(7,6)
       Expecting:
           13
       ok
       1 items had no tests:
           arithmetic
       1 items passed all tests:
          1 tests in arithmetic.add
       1 tests in 2 items.
       1 passed and 0 failed.
       Test passed.

#. So that the doctests can also be imported into other modules, you should add
   the following lines:

   .. literalinclude:: arithmetic.py
      :language: python
      :lines: 29-31
      :lineno-start: 29
