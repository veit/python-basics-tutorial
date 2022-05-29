Sets
====

A set in Python is an unordered collection of objects used in situations where
membership and uniqueness to the set are the most important information of the
object. Sets behave like collections of :doc:`Dictionary <dicts>` keys without
associated values:

.. code-block:: python
   :linenos:

    >>> x = set([1, 2, 3, 2, 4])
    >>> x
    {1, 2, 3, 4}
    >>> 1 in x
    True
    >>> 5 in x
    False

Line 1
    You can create a set by applying ``set`` to a sequence like a
    :doc:`Liste <lists>`.
Line 3
    When a sequence is made into a set, duplicates are removed.
Line 4 and 6
    The keyword is used to check whether an object belongs to a set.
