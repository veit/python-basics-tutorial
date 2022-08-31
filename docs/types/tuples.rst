Tuples
======

Tuples are similar to lists but are immutable, so they cannot be changed once
they have been created. The operators (``in``, ``+`` and ``*``) and built-in
functions (``len``, ``max`` and ``min``) work with them in the same way as with
lists, as none of these functions change the original. The index and slice
notations work in the same way to get elements or slices, but cannot be used to
add, remove or replace elements. Also, there are only two tuple methods:
``count`` and ``index``. An important purpose of tuples is to be used as keys
for dictionaries. They are also more efficient to use when you don’t need a
change facility.

.. code-block:: python
    :linenos:

    ()
    (1,)
    (1, 2, 3, 5)
    (1, "2.", 3.0, ["4a", "4b"], (5.1,5.2))

Line 2
    A tuple with one element requires a comma.
Line 4
    A tuple, like a :doc:`Liste <lists>`, can contain a mixture of other types
    as elements, including any :doc:`numbers`, :doc:`strings`, :doc:`tuples`,
    :doc:`lists`, :doc:`dicts`, :doc:`files` and functions.

A list can be converted to a tuple using the built-in ``tuple`` function:

.. code-block:: python

    >>> x = [1, 2, 3, 5]
    >>> tuple(x)
    (1, 2, 3, 5)

Conversely, a tuple can be converted into a list using the built-in list
function:

.. code-block:: python

    >>> x = (1, 2, 3, 4)
    >>> list(x)
    [1, 2, 3, 4]

The advantages of tuples over :doc:`lists` are:

* Tuples are faster than lists.

  If you want to define a constant set of values and just cycle through them,
  you should use a tuple instead of a list.

* Tuples can not be modified and are therefore *write-protected*.

* Tuples can be used as keys in :doc:`dicts` and values in :doc:`sets`.
