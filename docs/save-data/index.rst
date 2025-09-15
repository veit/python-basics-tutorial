Save and access data
====================

You can save your data persistently in :doc:`files and directories
<files-directories>`. In the Python standard library, there are also several
modules for converting data into a linear form. This process is called
*serialisation* or *marshalling*. The reverse process is called
*deserialisation* or *unmarshalling*. And if the :ref:`built-in modules
<builtin-file-modules>` are not sufficient, you can also use the
:ref:`pandas-io-tools`.

the :doc:`marshal <python3:library/marshal>` module
    is mainly used internally by Python and should not be used to store data in
    a backwards compatible way.
the :doc:`pickle <pickle>` module
    if you don’t need a readable format or interoperability.
the :doc:`json <python3:library/json>` module
    you can use to exchange data for different languages in a readable form.
the :doc:`xml <xml>` module
    you can also use to exchange data in different languages in a readable form.

.. tip::
   `cusy Seminar
   <https://cusy.io/en/our-training-courses/read-write-and-provide-data-with-python>`_

.. toctree::
   :titlesonly:
   :hidden:

   files-directories
   modules
   pickle
   xml

The Python Database API
-----------------------

The Python Database :abbr:`API (Application Programming Interface)` defines a
standard interface for Python database access modules. It’s defined in
:pep:`249` and widely used, for example by :doc:`sqlite <sqlite/index>`,
:doc:`psycopg <psycopg>`, and `mysql-python
<https://sourceforge.net/projects/mysql-python/>`_.

SQLAlchemy
----------

:doc:`Python4DataScience:data-processing/postgresql/sqlalchemy` is a widely used
database toolkit. It provides not only an :abbr:`ORM (Object Relational Mapper)`
but also a generalised API for writing database-agnostic code without SQL.
:doc:`Python4DataScience:data-processing/postgresql/alembic` is based on
SQLAlchemy and serves as a database migration tool.

.. toctree::
   :titlesonly:
   :hidden:

   sqlite/index
   psycopg

NoSQL databases
---------------

There is data that is difficult to transfer into a relational data model. At the
least then you should take a look at
:doc:`Python4DataScience:data-processing/nosql/index`.
