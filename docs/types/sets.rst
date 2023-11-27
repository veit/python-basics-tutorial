Sets
====

A set in Python is an unordered collection of objects used in situations where
membership and uniqueness to the set are the most important information of the
object. The ``in`` operator runs faster with sets than with :doc:`lists`:

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
    You can create a set by applying ``set`` to a sequence like a :doc:`list
    <lists>`.
Line 3
    When a sequence is made into a set, duplicates are removed.
Line 4 and 6
    The keyword is used to check whether an object belongs to a set.

Sets behave like collections of :doc:`Dictionary <dicts>` keys without
associated values.

However, the speed advantage also comes at a price: sets do not keep the
elements elements in the correct order, whereas :doc:`lists` and :doc:`tuples`
do. If the order is important to you, you should use a data structure that
remembers the order.

Summary
-------

+---------------+---------------+---------------+---------------+---------------+
| data type     | mutable       | ordered       | indexed       | duplicates    |
+===============+===============+===============+===============+===============+
| set           | ✅            | ❌            | ❌            | ❌            |
+---------------+---------------+---------------+---------------+---------------+
