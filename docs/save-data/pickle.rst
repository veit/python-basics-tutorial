The ``pickle`` module
=====================

If you want to serialise Python objects, you can simply use the Python
:doc:`pickle <python3:library/pickle>` module that comes with Python.

.. note::
   Note, however, that pickle is not secure, so you should not process data that
   comes from untrusted sources.

   Also, Pickle versions are not always backwards compatible.

Here is an example of a Python dict that contains multiple data types:

#. Importing the ``pickle`` module

   .. literalinclude:: pickle_example.py
      :language: python
      :lines: 1
      :lineno-start: 1

#. Serialise the Python object with ``pickle``:

   .. literalinclude:: pickle_example.py
      :language: python
      :lines: 4-8
      :lineno-start: 4

#. Writing the serialised data:

   .. literalinclude:: pickle_example.py
      :language: python
      :lines: 10-11
      :lineno-start: 10

#. Loading the pickled data:

   .. literalinclude:: pickle_example.py
      :language: python
      :lines: 14-15
      :lineno-start: 14

#. Output of the picked data:

   .. literalinclude:: pickle_example.py
      :language: python
      :lines: 18
      :lineno-start: 18

   .. code-block:: python

      {'a': [1, 2.0, (3+4j)], 'b': ('character string', b'byte string'), 'c': {False, True, None}}

In addition to :py:func:`pickle.dump` and  :py:func:`pickle.load`, there are
also the functions :py:func:`pickle.dumps` and :py:func:`pickle.loads`. The
appended ``s`` indicates that these functions process strings.

.. seealso::
   * :doc:`Python-Module-Dokumentation <python3:library/pickle>`
   * `Using Pickle <https://wiki.python.org/moin/UsingPickle>`_
