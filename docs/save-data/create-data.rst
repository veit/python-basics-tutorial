Create data
===========

#. Insert a record into the database:

   .. literalinclude:: create_data.py
      :language: python
      :lines: 7-10
      :lineno-start: 7

#. Save data to database:

   .. literalinclude:: create_data.py
      :language: python
      :lines: 13
      :lineno-start: 13

#. Insert multiple records using the more secure ``?`` method where the number
   of  ``?`` should correspond to the number of columns:

   .. literalinclude:: create_data.py
      :language: python
      :lines: 16-
      :lineno-start: 16
