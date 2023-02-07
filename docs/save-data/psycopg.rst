The psycopg module
==================

#. Install the psycopg module

   .. code-block:: console

      $ python3 -m pip install psycopg
      Collecting psycopg
        Downloading psycopg-3.0.1-py3-none-any.whl (140 kB)
           |████████████████████████████████| 140 kB 3.4 MB/s
      Installing collected packages: psycopg
      Successfully installed psycopg-3.0.1

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
