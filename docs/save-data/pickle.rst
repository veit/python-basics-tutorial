The ``pickle`` module
=====================

Python can write any data structure to a file, read that data structure back out
of the file, and recreate it with just a few commands. This capability can be
very useful because it can save you many pages of code that does nothing but
write the state of a programme to a file and read that state back in.

Python provides this capability via the :doc:`pickle <python3:library/pickle>`
module. Pickle is powerful, but simple to use. Suppose that the entire state of
a programme is stored in three variables: ``a``, ``b`` and ``c``. You can store
this state in a file called ``data.pickle`` as follows:

#. Importing the ``pickle`` module

   .. literalinclude:: pickle_example.py
      :language: python
      :lines: 1
      :lineno-start: 1

#. Define different data

   .. literalinclude:: pickle_example.py
      :language: python
      :lines: 3-5
      :lineno-start: 3

#. Writing the data

   .. literalinclude:: pickle_example.py
      :language: python
      :lines: 8-11
      :lineno-start: 8

   It does not matter what was stored in the variables. The content can be as
   simple as numbers or as complex as a list of dictionaries containing
   instances of user-defined classes. :py:func:`pickle.dump` saves everything.

   The pickle module can store almost anything in this way. It can handle
   :doc:`/types/numbers`, :doc:`/types/lists`, :doc:`/types/tuples`,
   :doc:`/types/dicts`, :doc:`/types/strings` and pretty much anything made up
   of these object types, including all class instances. It also handles shared
   objects, cyclic references and other complex storage structures correctly by
   storing shared objects only once and restoring them as shared objects, not as
   identical copies.

#. Loading pickled data:

   This data can be read in again during a later programme run with
   :py:func:`pickle.load`:

   .. literalinclude:: pickle_example.py
      :language: python
      :lines: 14-17
      :lineno-start: 14

#. Output the pickled data:

   .. literalinclude:: pickle_example.py
      :language: python
      :lines: 20
      :lineno-start: 20

   .. code-block:: python

      [1, 2.0, (3+4j)] ('character string', b'byte string') {False, None, True}

However, in most cases you will not want to restore all your data in the order
it was saved. A simple and effective way to restore only the data of interest is
to write a save function that stores all the data you want to save in a
dictionary and then use Pickle to save the dictionary. You can then use a
complementary restore function to read the dictionary back in and assign the
values in the dictionary to the appropriate programme variables. If you use this
approach with the previous example, you will get the following code:

.. literalinclude:: pickle_example2.py
   :language: python
   :lines: 1-12
   :lineno-start: 1

You can then output the data from ``c`` with

.. literalinclude:: pickle_example2.py
   :language: python
   :lines: 15-19
   :lineno-start: 15

.. code-block:: python

   {False, None, True}

In addition to :py:func:`pickle.dump` and :py:func:`pickle.load`, there are also
the functions :py:func:`pickle.dumps` and :py:func:`pickle.loads`. The appended
s indicates that these functions process strings.

.. warning::
   Although using a pickled object in the previous scenario can make sense, you
   should also be aware of the disadvantages of pickling:

   * Pickling is neither particularly fast nor space-saving as a means of
     serialisation. Even using :doc:`json <python3:library/json>` to store
     serialised objects is faster and results in smaller files on disk.
   * Pickling is not secure, and loading a pickle with malicious content can
     lead to the execution of arbitrary code on your machine. Therefore, you
     should avoid pickling if there is a possibility that the pickle file is
     accessible to someone who could modify it.
   * Pickle versions are not always backwards compatible.

.. seealso::
   * :doc:`Python-Module-Dokumentation <python3:library/pickle>`
   * `Using Pickle <https://wiki.python.org/moin/UsingPickle>`_
