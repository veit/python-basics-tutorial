Dictionaries
============

Python’s built-in dictionary data type provides associative array functionality
implemented using hash tables. The built-in ``len`` function returns the number
of key-value pairs in a dictionary. The ``del`` statement can be used to delete
a key-value pair. As with :doc:`lists` , several dictionary methods
(:py:meth:`clear <dict.clear>`, :py:meth:`copy <dict.copy>`, :py:meth:`get
<dict.get>`, :py:meth:`items <dict.items>`, :py:meth:`keys <dict.keys>`,
:py:meth:`update <dict.update>` and :py:meth:`values <dict.values>`) are
available.

.. code-block:: pycon

    >>> x = {1: "eins", 2: "zwei"}
    >>> x[3] = "drei"
    >>> x["viertes"] = "vier"
    >>> list(x.keys())
    [1, 2, 3, 'viertes']
    >>> x[1]
    'eins'
    >>> x.get(1, "nicht vorhanden")
    'eins'
    >>> x.get(5, "nicht vorhanden")
    'nicht vorhanden'

Keys must be of immutable type, including :doc:`numbers`, :doc:`strings/index`
and :doc:`tuples`.

.. warning::
   Even if you can use different key types in a dictionary, you should avoid
   this, as it not only makes it more difficult to read, but also sorting is
   also made more difficult.

Values can be any type of object, including mutable types such as :doc:`lists`
and :doc:`dicts`. If you try to access the value of a key that is not in the
dictionary, a ``KeyError`` exception is thrown. To avoid this error, the
dictionary method ``get`` optionally returns a custom value if a key is not
contained in a dictionary.

``setdefault``
--------------

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

Merging dictionaries
--------------------

You can merge two dictionaries into a single dictionary using the
:py:meth:`dict.update` method:

.. code-block:: pycon

   >>> titles = {7.0: "Data Types", 7.1: "Lists", 7.2: "Tuples"}
   >>> new_titles = {7.0: "Data types", 7.3: "Sets"}
   >>> titles.update(new_titles)
   >>> titles
   {7.0: 'Data types', 7.1: 'Lists', 7.2: 'Tuples', 7.3: 'Sets'}

.. note::
   The order of the operands is important, as ``7.0`` is duplicated and the
   value of the last key overwrites the previous one.

Extensions
----------

`python-benedict <https://github.com/fabiocaccamo/python-benedict>`_
    ``dict`` subclass with keylist/keypath/keyattr support and I/O shortcuts.
:doc:`pandas <Python4DataScience:workspace/pandas/python-data-structures>`
    can convert Dicts into Series and DataFrames.

Checks
------

* Suppose you have the two dictionaries ``x = {"a":1, "b":2, "c":3, "d":4}`` and
  ``y = {"a":5, "e":6, "f":7}``. What would be the content of ``x`` after the
  following code snippets have been executed?

  .. code-block:: pycon

     >>> del x["b"]
     >>> z = x.setdefault("e", 8)
     >>> x.update(y)

  .. code-block:: pycon

     >>> x = {"a": 1, "b": 2, "c": 3, "d": 4}
     >>> y = {"a": 5, "e": 6, "f": 7}
     >>> del x["b"]
     >>> z = x.setdefault("e", 8)
     >>> x.update(y)
     >>> x
     {'a': 5, 'c': 3, 'd': 4, 'e': 6, 'f': 7}

* Which of the following expressions can be a key of a dictionary:  ``1``;
  ``"Veit"``; ``("Veit", [1])``; ``[("Veit", [1])]``; ``["Veit"]``; ``("Veit",
  "Tim", "Monique")``

  .. code-block:: pycon

     >>> d = {}
     >>> d[1] = None
     >>> d["Veit"] = None
     >>> d[("Veit", [1])]
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     TypeError: unhashable type: 'list'
     >>> d[["Veit"]] = None
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     TypeError: unhashable type: 'list'
     >>> d[("Veit", "Tim", "Monique")] = None

* You can use a :doc:`Dictionary </types/dicts>` like a spreadsheet table by
  using :doc:`/types/tuples` as key row and column values. Write sample code to
  add and retrieve values.

  .. code-block:: pycon

     >>> sheet = {}
     >>> sheet[("A", 0)] = 1
     >>> sheet[("A", 1)] = 2
     >>> sheet[("B", 0)] = 3
     >>> sheet[("B", 1)] = 4
     >>> print(sheet[("A", 1)])
     2
