Dictionaries
============

Python’s built-in dictionary data type provides associative array functionality
implemented using hash tables. The built-in ``len`` function returns the number
of key-value pairs in a dictionary. The ``del`` statement can be used to delete
a key-value pair. As with :doc:`lists`, several dictionary methods (``clear``,
``copy``, ``get``, ``items``, ``keys``, ``update`` and ``values``) are
available.

.. code-block:: python

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

Keys must be of immutable type, including :doc:`numbers`, :doc:`strings` and
:doc:`tuples`. Values can be all types of objects, including mutable types such
as :doc:`lists` and :doc:`dicts`. If you try to access the value of a key that
is not in the dictionary, a ``KeyError`` exception is thrown. To avoid this
error, the dictionary method ``get`` optionally returns a custom value if a key
is not contained in a dictionary.
