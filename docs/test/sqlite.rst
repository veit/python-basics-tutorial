Example: Testing the SQLite database
====================================

#. To test whether the database ``library.db`` was created with
   :download:`create_db.py <../save-data/create_db.py>`, we import
   :download:`create_db.py <../save-data/create_db.py>` and :doc:`os
   <python3:library/os>` in addition to :doc:`sqlite3
   <python3:library/sqlite3>` and :doc:`unittest
   <python3:library/unittest>`:

      .. literalinclude:: ../save-data/test_sqlite.py
         :language: python
         :lines: 1-4
         :lineno-start: 1

#. Then we first define a test class ``TestCreateDB``:

      .. literalinclude:: ../save-data/test_sqlite.py
         :language: python
         :lines: 6
         :lineno-start: 6

#. In it, we then define the test method ``test_db_exists``, in which we use
   ``assert`` to assume that the file exists in :doc:`os.path
   <python3:library/os.path>`: 

      .. literalinclude:: ../save-data/test_sqlite.py
         :language: python
         :lines: 8-9
         :lineno-start: 8

#. Now we also check whether the ``books`` table was created. To do this, we try
   to create the table again and use ``assertRaises`` to expect ``sqlite`` to
   end with an :``OperationalError``:

   .. literalinclude:: ../save-data/test_sqlite.py
      :language: python
      :lines: 11-13
      :lineno-start: 11

#. We do not want to carry out further tests on a database in the file system
   but in an SQLite database in the working memory:

   .. literalinclude:: ../save-data/test_sqlite.py
      :language: python
      :lines: 15-19
      :lineno-start: 15

.. seealso::
   You can find more examples for testing your SQLite database functions in the
   SQLite test suite `test_sqlite3
   <https://github.com/python/cpython/tree/main/Lib/test/test_sqlite3>`_.
