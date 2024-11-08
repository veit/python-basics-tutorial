Save and access data
====================

To store data persistently, a process called serialisation or marshalling can be
used. In it, data structures are converted into a linear form and stored. The
reverse process is then called deserialisation or unmarshalling. Python offers
several modules in the standard library that you can be used to serialise and
deserialise objects:

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

NoSQL databases
---------------

There is data that is difficult to transfer into a relational data model. At the
least then you should take a look at
:doc:`Python4DataScience:data-processing/nosql/index`.

.. toctree::
   :titlesonly:
   :hidden:

   filesystem
   pickle
   xml
   sqlite/index
   psycopg
