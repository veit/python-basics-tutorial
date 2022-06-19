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
