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
      :lines: 14-15
      :lineno-start: 14

#. Select titles containing Python:

   .. literalinclude:: query_data.py
      :language: python
      :lines: 20-26
      :lineno-start: 20

#. Finally, the data can be queried with:

   .. literalinclude:: query_data.py
      :language: python
      :lines: 29-
      :lineno-start: 29

   .. code-block:: rest

    All books from Veit Schiele:
    [(1, 'Python basics', 'en', 'Veit Schiele', 'BSD-3-Clause', '2021-10-28'), (2, 'Jupyter Tutorial', 'en', 'Veit Schiele', 'BSD-3-Clause', '2019-06-27'), (3, 'Jupyter Tutorial', 'de', 'Veit Schiele', 'BSD-3-Clause', '2020-10-26'), (4, 'PyViz Tutorial', 'en', 'Veit Schiele', 'BSD-3-Clause', '2020-04-13')]
    Listing of all books sorted by author:
    (1, 'Python basics', 'en', 'Veit Schiele', 'BSD-3-Clause', '2021-10-28')
    (2, 'Jupyter Tutorial', 'en', 'Veit Schiele', 'BSD-3-Clause', '2019-06-27')
    (3, 'Jupyter Tutorial', 'de', 'Veit Schiele', 'BSD-3-Clause', '2020-10-26')
    (4, 'PyViz Tutorial', 'en', 'Veit Schiele', 'BSD-3-Clause', '2020-04-13')
    All books with Python in the title:
    [(1, 'Python basics', 'en', 'Veit Schiele', 'BSD-3-Clause', '2021-10-28')]
