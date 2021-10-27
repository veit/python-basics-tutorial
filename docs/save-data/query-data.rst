Query data
==========

#. Select all records from an author:

   .. literalinclude:: query_data.py
      :language: python
      :lines: 7-11
      :lineno-start: 7

   For the ``print`` output, we use a formatted string literal or
   :term:`python3:f-string` by prefixing it with an ``f``.

#. Select all records sorted by author:

   .. literalinclude:: query_data.py
      :language: python
      :lines: 13-16
      :lineno-start: 13

#. Select titles containing Python:

   .. literalinclude:: query_data.py
      :language: python
      :lines: 18-24
      :lineno-start: 18
