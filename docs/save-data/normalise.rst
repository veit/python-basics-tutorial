Normalising the data
====================

`Normalisation <https://en.wikipedia.org/wiki/Database_normalization>`_ is the
division of attributes or table columns into several relations or tables so that
no redundancies are included.

Example
-------

In the following example, we normalise the language in which the books were
published.

#. To do this, we first create a new table ``languages`` with the columns ``id``
   and ``language_code``:

   .. literalinclude:: normalise.py
      :language: python
      :lines: 6-9
      :lineno-start: 6

#. Then we create the values ``de`` and ``en`` in this table:

   .. literalinclude:: normalise.py
      :language: python
      :lines: 12-18
      :lineno-start: 12

#. Since SQLite does not support ``MODIFY COLUMN``, we now create a temporary
   table ``temp`` with all columns from ``books`` and a column ``language_code``
   that uses the column ``id`` from the ``languages`` table as a foreign key:

   .. literalinclude:: normalise.py
      :language: python
      :lines: 22-32
      :lineno-start: 22

#. Now we transfer the values from the ``books`` table to the ``temp`` table:

   .. literalinclude:: normalise.py
      :language: python
      :lines: 35-37
      :lineno-start: 35

#. Transfer the specification of the language in ``books`` as the ``id`` of the
   data records from the ``languages`` table to ``temp``.

   .. literalinclude:: normalise.py
      :language: python
      :lines: 40-44
      :lineno-start: 40

#. Now we can delete the ``languages`` column in the ``temp`` table:

   .. literalinclude:: normalise.py
      :language: python
      :lines: 55
      :lineno-start: 55

   .. note::
      ``DROP COLUMN`` can only be used from Python versions from 3.8 that were
      released after 27 April 2021.

      With older Python versions, another table would have to be created that no
      longer contains the languages column and then the data records from
      ``temp`` would have to be inserted into this table.

#. The ``books`` table can now also be deleted:

   .. literalinclude:: normalise.py
      :language: python
      :lines: 57
      :lineno-start: 57

#. And finally, the ``temp`` table can be renamed ``books``:

   .. literalinclude:: normalise.py
      :language: python
      :lines: 59
      :lineno-start: 59
