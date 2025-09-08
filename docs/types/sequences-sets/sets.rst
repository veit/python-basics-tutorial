Sets
====

Sets in Python are an unordered collection of objects used in situations where
membership and uniqueness to the set are the most important information of the
object. The ``in`` operator runs faster with sets than with :doc:`lists`:

.. _set:

``set``
-------

Create sets
~~~~~~~~~~~

You can create sets by applying  :class:`set` to a sequence, for example to a
:doc:`list <lists>`.

.. code-block:: pycon

   >>> sequences = set(["list", "tuple", "tuple"])
   >>> sequences
   {'tuple', 'list'}

If a sequence is made into a set, duplicates are removed, but the order is then
also lost.

Individual elements cannot be selected with slicing either:

.. code-block:: pycon

   >>> sequences[0]
   Traceback (most recent call last):
     File "<python-input-27>", line 1, in <module>
       sequences[0]
       ~~~~~~~~~^^^
   TypeError: 'set' object is not subscriptable

Check values
~~~~~~~~~~~~

The keyword ``in`` is used to check whether an object belongs to a set.

.. code-block:: pycon

   >>> "list" in sequences
   True
   >>> "set" in sequences
   False

Add and delete values
~~~~~~~~~~~~~~~~~~~~~

You can add and delete values with ``add`` and ``remove``.

.. code-block:: pycon

   >>> quantities = sequences.add("set")
   >>> quantities
   {'list', 'tuple', 'set'}
   >>> quantities.remove("set")
   >>> quantities
   {'list', 'tuple'}

The elements are unordered, which means that the values within a sequence can
shift when new elements are added.

Set formation
~~~~~~~~~~~~~

Union set
   .. code-block:: pycon

      x = {4, 2, 3, 2, 1}
      y = {3, 4, 5}
      >>> x.union(y)
      {1, 2, 3, 4, 5}

Intersection
   .. code-block:: pycon

      >>> x.intersection(y)
      {3, 4}

Difference or remainder set

   .. code-block:: pycon

      >>> x.difference(y)
      {1, 2}

.. _frozenset:

``frozenset``
-------------

In addition to ``set``, there is also ``frozenset``, an :term:`immutable` data
type. This means that they can also be members of other sets:

.. code-block:: pycon
   :linenos:

   >>> sequences = frozenset(["list", "tuple", "set", "tuple"])
   >>> sequences
   frozenset({'list', 'tuple', 'set'})
   >>> dicts = {"dict"}
   >>> sequences.add(dicts)
   Traceback (most recent call last):
     File "<python-input-18>", line 1, in <module>
       sequences.add(dicts)
       ^^^^^^^^^^^^^
   AttributeError: 'frozenset' object has no attribute 'add'
   >>> dicts.add(sequences)
   >>> dicts
   {frozenset({'list', 'tuple', 'set'}), 'dict'}

Performance
-----------

Sets are very fast when checking whether elements are contained in a set. The set
arithmetic of sets is also well suited to finding common and unique values of two
sets. For this purpose, it can be useful to convert :doc:`lists` or :doc:`tuples`
into sets.

Order
-----

However, the speed advantage also comes at a price: sets do not keep the elements
in the correct order, whereas :doc:`lists` and :doc:`tuples` do. If the order is
important to you, you should only convert the elements into a set for certain
operations, for example to check whether the elements of a list are unique with

.. code-block:: pycon

   >>> sequences = ["list", "tuple", "set", "tuple"]
   >>> len(sequences) == len(set(sequences))
   False

Checks
------

* How many elements does a set have if it is formed from the following list ``[4,
  2, 3, 2, 1]``?
