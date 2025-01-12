Sets
====

Sets in Python are an unordered collection of objects that are used in
situations where membership and uniqueness to the set are the most important
information of the object. The ``in`` operator runs faster with sets than with
:doc:`lists`:

.. _set:

``set``
-------

.. code-block:: pycon
   :linenos:

   >>> x = set([1, 2, 3, 2, 4])
   >>> x
   {1, 2, 3, 4}
   >>> 1 in x
   True
   >>> 5 in x
   False
   >>> x.add(0)
   >>> x
   {0, 1, 2, 3, 4}
   >>> x.remove(4)
   >>> x
   {0, 1, 2, 3}
   >>> y = set([3, 4, 5])
   >>> x | y
   {0, 1, 2, 3, 4, 5}
   >>> x & y
   {3}
   >>> x ^ y
   {0, 1, 2, 4, 5}
   >>> x.update(y)
   >>> x
   {0, 1, 2, 3, 4, 5}

Line 1
    You can create a set by applying ``set`` to a sequence, for example to a
    :doc:`list <lists>`.
Line 3
    When a sequence is made into a set, duplicates are removed.
Lines 4–7
    The keyword ``in`` is used to check whether an object belongs to a set.
Lines 8–13
    With ``add`` and ``remove`` you can change the elements in set.
Line 15
    ``|`` is used to get the union or combination of two sets.
Line 17
    ``&`` is used to get the intersection.
Line 19
    ``^`` is used to find the symmetrical difference, meaning elements that are
    contained in one or the other set, but not in both.

.. _frozenset:

``frozenset``
-------------

In addition to ``set``, there is also ``frozenset``, which is immutable. This
means that they can also be members of other sets:

.. code-block:: pycon
   :linenos:

   >>> x = set([4, 2, 3, 2, 1])
   >>> z = frozenset(x)
   >>> z
   frozenset({1, 2, 3, 4})
   >>> z.add(5)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   AttributeError: 'frozenset' object has no attribute 'add'
   >>> x.add(z)
   >>> x
   {1, 2, 3, 4, frozenset({1, 2, 3, 4})}

Order
-----

However, the speed advantage also comes at a price: sets do not keep the
elements in the correct order, whereas :doc:`lists` and :doc:`tuples` do. If the
order is important to you, you should use a data structure that remembers the
order.

Checks
------

* How many elements does a set have if it is formed from the following list
  ``[4, 2, 3, 2, 1]``?
