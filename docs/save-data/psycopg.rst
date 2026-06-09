The psycopg module
==================

#. Install the psycopg module

   .. code-block:: console

      $ uv add psycopg
      Resolved 3 packages in 4ms
      Built psycopg-env @ file:///Users/veit/sandbox/psycopg_env
      Prepared 1 package in 7ms
      Uninstalled 1 package in 0.96ms
      Installed 2 packages in 5ms
       + psycopg==3.3.4
       ~ psycopg-env==0.1.0 (from file:///Users/veit/cusy/trn/python-basics-tutorial)

#. Import the psycopg module

   .. literalinclude:: psycopg.py
      :language: python
      :lines: 1
      :linenos:

#. Create a database

   .. literalinclude:: psycopg.py
      :language: python
      :lines: 3-4
      :lineno-start: 3

#. Query the database

   .. literalinclude:: psycopg.py
      :language: python
      :lines: 7-8
      :lineno-start: 7

#. Close cursor and connection

   .. literalinclude:: psycopg.py
      :language: python
      :lines: 11-12
      :lineno-start: 11
