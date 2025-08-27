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

   Test Suite
       is a collection of several :term:`test cases <Test Case>`.

   Test Runner
       runs through a :term:`Test Suite` and displays the results.

Example
-------

Suppose you have implemented the following add method in the
:download:`test_arithmetic.py` module:

.. literalinclude:: /document/arithmetic.py
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

Example: Testing an SQLite database
-----------------------------------

#. To test whether the database ``library.db`` was created with
   :download:`create_db.py <../save-data/sqlite/create_db.py>`, we import
   :download:`../save-data/sqlite/create_db.py` and :doc:`os
   <python3:library/os>` in addition to :doc:`sqlite3 <python3:library/sqlite3>`
   and :doc:`unittest <python3:library/unittest>`:

   .. literalinclude:: ../save-data/sqlite/test_sqlite.py
      :language: python
      :lines: 1-5
      :lineno-start: 1

#. Then we first define a test class ``TestCreateDB``:

   .. literalinclude:: ../save-data/sqlite/test_sqlite.py
      :language: python
      :lines: 8
      :lineno-start: 8

#. In it we then define the test method ``test_db_exists``, in which we use
   ``assert`` to assume that the file exists in :doc:`os.path
   <python3:library/os.path>`:

   .. literalinclude:: ../save-data/sqlite/test_sqlite.py
      :language: python
      :lines: 9-10
      :lineno-start: 9

#. Now we also check whether the ``books`` table was created. For this we try to
   create the table again and expect with ``assertRaises`` that ``sqlite`` is
   terminated with an ``OperationalError``:

   .. literalinclude:: ../save-data/sqlite/test_sqlite.py
      :language: python
      :lines: 12-14
      :lineno-start: 12

#. We do not want to carry out further tests on a database in the file system
   but in an SQLite database in the working memory:

   .. literalinclude:: ../save-data/sqlite/test_sqlite.py
      :language: python
      :lines: 17-20
      :lineno-start: 17

.. seealso::
   You can find more examples for testing your SQLite database functions in the
   SQLite test suite `test_sqlite3
   <https://github.com/python/cpython/tree/main/Lib/test/test_sqlite3>`_.
