Boolean values and expressions
==============================

In Python, there are several ways to express Boolean values; the Boolean
constant ``False``, ``0``, the Python value ``None``, and empty values (for
example, the empty list ``[]`` or the empty string ``""``) are all considered
``False``. The Boolean constant ``True`` and everything else is considered
``True``.

``<``, ``<=``, ``==``, ``>``, ``>=``
    compares values.
``is``, ``is not``, ``in``, ``not in``
    checks the identity.
``and``, ``not``, ``or``
    are logical operators that can be used to link the above checks.

.. code-block:: pycon

   >>> x = 3
   >>> y = 3.0
   >>> z = [3, 4, 5]
   >>> x == y
   True
   >>> x is y
   False
   >>> x is not y
   True
   >>> x in z
   True
   >>> id(x)
   4375911432
   >>> id(y)
   4367574480
   >>> id(z[0])
   4375911432

If ``x`` and ``z[0]`` have the same ID in memory, this means that we are
referring to the same object in two places.

Most frequently, ``is`` and ``is not`` are used in conjunction with
:doc:`../types/none`:

.. code-block:: pycon

    >>> x is None
    False
    >>> x is not None
    True

The Python style guide in :pep:`8` says that you should use identity to compare
with :doc:`../types/none`. So you should never use ``x == None``, but enter ``x
is None`` instead.

However, you should never compare calculated floating point numbers with each
other:

.. code-block:: pycon

    >>> u = 0.6 * 7
    >>> v = 0.7 * 6
    >>> u == v
    False
    >>> u
    4.2
    >>> v
    4.199999999999999
