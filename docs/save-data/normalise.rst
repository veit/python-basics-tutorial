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
      :lines: 11-17
      :lineno-start: 11

#. Since SQLite does not support ``MODIFY COLUMN``, we now create a temporary
   table ``temp`` with all columns from ``books`` and a column ``language_code``
   that uses the column ``id`` from the ``languages`` table as a foreign key:

   .. literalinclude:: normalise.py
      :language: python
      :lines: 19-29
      :lineno-start: 19

#. Now we transfer the values from the ``books`` table to the ``temp`` table:

   .. literalinclude:: normalise.py
      :language: python
      :lines: 31-33
      :lineno-start: 31

#. Transfer the specification of the language in ``books`` as the ``id`` of the
   data records from the ``languages`` table to ``temp``.

   .. literalinclude:: normalise.py
      :language: python
      :lines: 35-43
      :lineno-start: 35

#. Now we can delete the ``languages`` column in the ``temp`` table:

   .. literalinclude:: normalise.py
      :language: python
      :lines: 48-49
      :lineno-start: 48

   .. note::
      ``DROP COLUMN`` can only be used from Python versions from 3.8 that were
      released after 27 April 2021.

      With older Python versions, another table would have to be created that no
      longer contains the languages column and then the data records from
      ``temp`` would have to be inserted into this table.

#. The ``books`` table can now also be deleted:

   .. literalinclude:: normalise.py
      :language: python
      :lines: 51-52
      :lineno-start: 51

#. And finally, the ``temp`` table can be renamed ``books``:

   .. literalinclude:: normalise.py
      :language: python
      :lines: 54-55
      :lineno-start: 54
