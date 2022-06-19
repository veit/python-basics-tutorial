Query data
==========

#. Select all records from an author:

   .. literalinclude:: query_data.py
      :language: python
      :lines: 6-10
      :lineno-start: 6

   For the ``print`` output, we use a formatted string literal or
   :term:`python3:f-string` by prefixing it with an ``f``.

#. Select all records sorted by author:

   .. literalinclude:: query_data.py
      :language: python
      :lines: 12-13
      :lineno-start: 12

#. Select titles containing Python:

   .. literalinclude:: query_data.py
      :language: python
      :lines: 17-23
      :lineno-start: 17

#. Finally, the data can be queried with:

   .. literalinclude:: query_data.py
      :language: python
      :lines: 25-27
      :lineno-start: 27
