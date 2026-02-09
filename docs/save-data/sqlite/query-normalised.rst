Query normalised data
=====================

#. Query all books sorted by ``language_id`` and ``title``:

   .. literalinclude:: query_normalised.py
      :language: python
      :lines: 7-11
      :lineno-start: 7

   .. code-block:: pycon

      >>> import create_db
      >>> import create_data_from_csv
      >>> import normalise
      >>> import query_normalised
      All books ordered by language id and title:
      (1, 'Veit Schiele', 'Jupyter Tutorial')
      (2, 'Veit Schiele', 'Jupyter Tutorial')
      (2, 'Veit Schiele', 'PyViz Tutorial')
      (2, 'Veit Schiele', 'Python basics')

#. In order to receive not only the ID of the languages but also the
   corresponding language codes, a connection to the language codes stored there
   is established with ``JOIN`` via the ``id`` column in the ``languages``
   table:

   .. literalinclude:: query_normalised.py
      :language: python
      :lines: 14-22
      :lineno-start: 14

   .. code-block:: pycon

      >>> import query_normalised
      …
      All books ordered by language code and title:
      ('de', 'Veit Schiele', 'Jupyter Tutorial')
      ('en', 'Veit Schiele', 'Jupyter Tutorial')
      ('en', 'Veit Schiele', 'PyViz Tutorial')
      ('en', 'Veit Schiele', 'Python basics')
