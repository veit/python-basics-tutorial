Tuples
======

Tuples are similar to :doc:`lists`, but can only be created and not changed.
Tuples have the important task of efficiently creating keys for :doc:`../dicts`,
for example.

Tuples are created in a similar way to lists: a sequence of values is assigned
to a variable, but these are enclosed in round brackets rather than square
brackets:

.. code-block:: pycon

   >>> x = (1, "2.", 3.0, ["4a", "4b"], (5.1, 5.2))

This line creates a tuple with five elements. Once a tuple has been created, it
can be used in a similar way to a list:

.. code-block:: pycon

   >>> x[1]
   '2.'
   >>> x[1:]
   ('2.', 3.0, ['4a', '4b'], (5.1, 5.2))
   >>> len(x)
   5
   >>> max(x[:3:2])
   3.0
   >>> min(x[:3:2])
   1
   >>> 1 in x
   True
   >>> 5.1 not in x
   True

The operators (:ref:`in, not in <python3:in>`, ``+`` and ``*``) and the built-in
functions (``len``, ``max`` and ``min``) work with tuples in the same way as
with :doc:`lists`, as none of these functions change the original. However,
there are only two tuple methods: ``count`` and ``index``.

You can use the ``+``- and ``*`` operators to create tuples from existing
tuples:

.. code-block:: pycon

   >>> x + x
   (1, '2.', 3.0, ['4a', '4b'], (5.1, 5.2), 1, '2.', 3.0, ['4a', '4b'], (5.1, 5.2))
   >>> 2 * x
   (1, '2.', 3.0, ['4a', '4b'], (5.1, 5.2), 1, '2.', 3.0, ['4a', '4b'], (5.1, 5.2))

A copy of a tuple can be created in the same way as for lists:

.. code-block:: pycon

   >>> x[:]
   (1, '2.', 3.0, ['4a', '4b'], (5.1, 5.2))
   >>> x * 1
   (1, '2.', 3.0, ['4a', '4b'], (5.1, 5.2))
   >>> x + ()
   (1, '2.', 3.0, ['4a', '4b'], (5.1, 5.2))

However, an attempt to change a tuple results in an error message:

.. code-block:: pycon

   >>> x[1] = "zweitens"
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'tuple' object does not support item assignment

One-element tuple
-----------------

However, there is a small syntactical difference to lists: while ``[1]`` creates
a list with one element, ``(1)`` is an integer and not a tuple. The background
to this is that round brackets are also used to group elements in expressions in
order to enforce a certain evaluation order. Therefore, each tuple with one or
more elements contains one or more commas:

.. blacken-docs:off

.. code-block:: pycon

   >>> y = ()
   >>> type(y)
   <class 'tuple'>
   >>> z = (1 + 3.0)
   >>> type(z)
   <class 'float'>
   >>> z = (1 + 3.0,)
   >>> type(z)
   <class 'tuple'>

.. blacken-docs:on

Packing and unpacking tuples
----------------------------

Tuples can appear on the left-hand side of an assignment operator. In this case,
the variables in the tuple receive the corresponding values from the tuple on
the right-hand side of the assignment operator. Here is a simple example:

.. code-block:: pycon

   >>> (v, w, x, y, z) = (1, "2.", 3.0, ["4a", "4b"], (5.1, 5.2))
   >>> v
   1
   >>> w
   '2.'

This example can be simplified even further, as Python recognises tuples in an
assignment context even without the round brackets:

.. code-block:: pycon

   >>> v, w, x, y, z = 1, "2.", 3.0, ["4a", "4b"], (5.1, 5.2)
   >>> y
   ['4a', '4b']
   >>> z
   (5.1, 5.2)

With ``*`` the unpacking is extended to include any number of elements that do
not match the other elements:

.. code-block:: pycon

   >>> x = (1, "2.", 3.0, ["4a", "4b"], (5.1, 5.2))
   >>> a, b, *c = x
   >>> a, b, c
   (1, '2.', [3.0, ['4a', '4b'], (5.1, 5.2)])
   >>> a, *b, c = x
   >>> a, b, c
   (1, ['2.', 3.0, ['4a', '4b']], (5.1, 5.2))
   >>> a, *b, c, d, e, f = x
   >>> a, b, c, d, e, f
   (1, [], '2.', 3.0, ['4a', '4b'], (5.1, 5.2))

.. note::
   The element marked with ``*`` receives all surplus elements as a list and, if
   there are no surplus elements, an empty list.

Converting between lists and tuples
-----------------------------------

A list can be converted into a tuple using the built-in ``tuple`` function:

.. code-block:: pycon

   >>> dates = [
   ...     "2025-11-09",
   ...     "2025-11-10",
   ...     "2025-11-11",
   ...     "2025-11-12",
   ... ]
   >>> tuple(dates)
   ('2025-11-09', '2025-11-10', '2025-11-11', '2025-11-12')

Conversely, a tuple can be converted into a list using the built-in ``list``
function:

.. code-block:: pycon

   >>> dates = (
   ...     "2025-11-09",
   ...     "2025-11-10",
   ...     "2025-11-11",
   ...     "2025-11-12",
   ... )
   >>> list(dates)
   ['2025-11-09', '2025-11-10', '2025-11-11', '2025-11-12']

The advantages of tuples over :doc:`lists <lists>` are:

* Tuples are faster than lists.

  If you want to define a constant set of values and just iterate through them,
  you should use a tuple instead of a list.

* Tuples can not be modified and are therefore *write-protected*.

* Tuples can be used as keys in :doc:`../dicts` and values in :doc:`sets`.

Checks
------

* Explain why the following operations cannot be applied to the tuple ``t``:

  * ``t.append(1)``
  * ``t[2] = 2``
  * ``del t[3]``

* How can you sort the elements of a tuple?
