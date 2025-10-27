Dictionaries
============

Dictionaries consist of key-value pairs. Keys must be of invariant type,
including numbers, :doc:`strings/index` and :doc:`sequences-sets/tuples`.

.. warning::
   Even if you can use different key types in a dictionary, you should avoid
   doing so, as this not only makes it more difficult to read, but also to sort.

Values can be any type of object, including mutable types such as
:doc:`sequences-sets/lists` and :doc:`dicts`.

.. code-block:: pycon

   >>> timeseries = {
   ...     "2022-01-31": -0.751442,
   ...     "2022-02-01": 0.816935,
   ...     "2022-02-02": -0.272546,
   ... }
   >>> timeseries["2022-02-03"] = -0.268295

If you try to access the value of a key that is not contained in the dictionary,
a ``KeyError`` :doc:`/control-flow/exceptions` is thrown. To avoid this error,
the dictionary method ``get`` optionally returns a user-defined value if a key
is not contained in a dictionary.

.. code-block:: pycon

   >>> timeseries["2022-02-03"]
   -0.268295
   >>> timeseries["2022-02-04"]
   Traceback (most recent call last):
     File "<python-input-15>", line 1, in <module>
       timeseries["2022-02-04"]
       ~~~~^^^^^^^^^^^^^^
   KeyError: '2022-02-04'
   >>> timeseries.get("2022-02-03", "Messwert nicht vorhanden")
   -0.268295
   >>> timeseries.get("2022-02-04", "Messwert nicht vorhanden")
   'Messwert nicht vorhanden'

Other Dict methods
------------------

The :func:`len` function built into Dicts returns the number of key-value pairs.
The ``del`` statement can be used to delete a key-value pair. As with
:doc:`sequences-sets/lists`, several dictionary methods ((:py:meth:`clear
<dict.clear>`, :py:meth:`copy <dict.copy>`, :py:meth:`get <dict.get>`,
:py:meth:`items <dict.items>`, :py:meth:`keys <dict.keys>`, :py:meth:`update
<dict.update>` and :py:meth:`values <dict.values>`) are available.

The :py:meth:`keys <dict.keys>`, :py:meth:`values <dict.values>` and
:py:meth:`items <dict.items>` methods do not return lists, but dictionary view
objects that behave like sequences, but are updated dynamically when the
dictionary changes. For this reason, you must use the :func:`list` function so
that they become a list in these examples:

.. code-block:: pycon

   >>> list(timeseries.keys())
   ['2022-01-31', '2022-02-01', '2022-02-02', '2022-02-03']

As of Python 3.6, dictionaries retain the order in which the keys were created,
and they are also returned in this order with  :py:meth:`keys <dict.keys>`.

Merging dictionaries
~~~~~~~~~~~~~~~~~~~~

You can use the :py:meth:`dict.update` method to merge two dictionaries into a
single dictionary:

.. code-block:: pycon

   >>> titles = {7.0: "Data Types", 7.1: "Lists", 7.2: "Tuples"}
   >>> new_titles = {7.0: "Data types", 7.3: "Sets"}
   >>> titles.update(new_titles)
   >>> titles
   {7.0: 'Data types', 7.1: 'Lists', 7.2: 'Tuples', 7.3: 'Sets'}

.. note::
   The order of the operands is important, as ``7.0`` is duplicated and the
   value of the last key overwrites the previous one.

``setdefault``
~~~~~~~~~~~~~~

:py:meth:`setdefault <dict.setdefault>` can be used to provide counters for the
keys of a dict, for example:

.. code-block:: pycon

   >>> titles = ["Data types", "Lists", "Sets", "Lists"]
   >>> for title in titles:
   ...     titles_count.setdefault(title, 0)
   ...     titles_count[title] += 1
   ...
   >>> titles_count
   {'Data types': 1, 'Lists': 2, 'Sets': 1}

.. note::
   Such counting operations quickly became widespread, so the
   :py:class:`collections.Counter` class was later added to the Python standard
   library. This class can perform the above-mentioned operations much more
   easily:

   .. code-block:: pycon

      >>> collections.Counter(titles)
      Counter({'Lists': 2, 'Data types': 1, 'Sets': 1})

Extensions
----------

`python-benedict <https://github.com/fabiocaccamo/python-benedict>`_
    ``dict`` subclass with keylist/keypath/keyattr support and I/O shortcuts.
:doc:`pandas <Python4DataScience:workspace/pandas/python-data-structures>`
    can convert dicts into series and DataFrames.

Checks
------

* Suppose you have the two dictionaries ``x = {"a": 1, "b": 2, "c": 3, "d": 4}``
  and ``y = {"a": 5, "e": 6, "f": 7}``. What would be the content of ``x`` after
  the following code snippets have been executed?

  .. code-block:: pycon

     >>> del x["b"]
     >>> z = x.setdefault("e", 8)
     >>> x.update(y)

* Which of the following expressions can be a key of a dictionary?
  ``1``; ``"Veit"``; ``("Veit", [1])``; ``[("Veit", [1])]``; ``["Veit"]``;
  ``("Veit", "Tim", "Monique")``

* You can use a :doc:`dictionary </types/dicts>`  and use it like a spreadsheet
  by using :doc:`tuples </types/sequences-sets/tuples>` as key row and column
  values. Write sample code to add and retrieve values.

* How can you remove all duplicates from a list without changing the order of the
  elements in the list?
