Save and access data
====================

The Python Database API
-----------------------

The Python Database :abbr:`API (Application Programming Interface)` defines a
standard interface for Python database access modules. It’s defined in `PEP 249
<https://www.python.org/dev/peps/pep-0249/>`_ and widely used, e.g. by
:doc:`sqlite <sqlite>`, :doc:`psycopg <psycopg>`, and `mysql-python
<https://sourceforge.net/projects/mysql-python/>`_.

SQLAlchemy
----------

:doc:`jupyter-tutorial:data-processing/postgresql/sqlalchemy` is a widely used
database toolkit. It provides not only an :abbr:`ORM (Object Relational Mapper)`
but also a generalised API for writing database-agnostic code without SQL.
:doc:`jupyter-tutorial:data-processing/postgresql/alembic` is based on
SQLAlchemy and serves as a database migration tool.

NoSQL databases
---------------

There is data that is difficult to transfer into a relational data model. At the 
least then you should take a look at
:doc:`jupyter-tutorial:data-processing/nosql/index`.

.. toctree::
   :titlesonly:
   :hidden:

   pickle
   sqlite
   create-db
   create-data
   create-data-from-csv
   query-data
   update-data
   delete-data
   psycopg
