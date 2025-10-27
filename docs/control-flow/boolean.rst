Boolean values and expressions
==============================

In Python, there are several ways to express Boolean values; the Boolean
constant ``False``, ``0``, the Python type :doc:`../types/none` and empty
values (for example the empty list ``[]`` or the empty string  ``""``) are all
considered ``False``. The Boolean constant ``True`` and everything else is
considered ``True``.

``<``, ``<=``, ``==``, ``>``, ``>=``
    compares values:

    .. code-block:: pycon

       >>> x = 3
       >>> y = 3.0
       >>> z = [3, 4, 5]
       >>> x == y
       True

    However, you should never compare calculated floating point numbers with
    each other:

    .. code-block:: pycon

       >>> u = 0.6 * 7
       >>> v = 0.7 * 6
       >>> u == v
       False
       >>> u
       4.2
       >>> v
       4.199999999999999
       >>> round(u, 2) == round(v, 2)
       True

``is``, ``is not``, ``in``, ``not in``
    checks the identity:

    .. code-block:: pycon

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

    The ``is`` operator is mostly used for values that only exist once in
    memory, so-called :term:`singleton objects <Singleton object>`. For example,
    checking for :doc:`../types/none` is the most common use of the ``is``
    operator.

    .. code-block:: pycon

       >>> x is None
       False
       >>> x is not None
       True

    The Python style guide in :pep:`8` also recommends that you should check for
    identity with :doc:`../types/none` and not for values, so never use ``x ==
    None``, but always use ``x is None``  instead.

``and``, ``not``, ``or``
    are logical operators that we can use to link the above checks:

    .. code-block:: pycon

       >>> x is y and x is z[0]
       False
       >>> x is y or x is z[0]
       True
       >>> x is y and not x is z[0]
       False
       >>> x is z[0] and not x is y
       True
