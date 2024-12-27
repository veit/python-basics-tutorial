Complex numbers
===============

Complex numbers consist of a real part and an `imaginary part
<https://en.wikipedia.org/wiki/Imaginary_number>`_, which is given the suffix
``j`` in Python.

.. code-block:: pycon

    >>> 7 + 2j
    (7+2j)

.. note::

    Python expresses the resulting complex number in parentheses to indicate
    that the output represents the value of a single object:

.. code-block:: pycon

    >>> (5 + 3j) ** (3 + 5j)
    (-7.04464115622119-11.276062812695923j)

.. code-block:: pycon

    >>> x = (5 + 3j) * (6 + 8j)
    >>> x
    (6+58j)
    >>> x.real
    6.0
    >>> x.imag
    58.0

Complex numbers consist of a real part and an imaginary part with the suffix
``j``. In the preceding code, the variable ``x`` is assigned to a complex
number. You can get its „real“ part with the attribute notation ``x.real`` and
the „imaginary“ part with ``x.imag``.

Advanced functions
------------------

The functions in the :doc:`math <python3:library/math>` module are not
applicable to complex numbers; one of the reasons for this is probably that the
square root of ``-1`` is supposed to produce an error. Therefore, similar
functions for complex numbers have been provided in the :doc:`cmath
<python3:library/cmath>` module:

:func:`python3:cmath.acos`, :func:`python3:cmath.acosh`, :func:`python3:cmath.asin`, :func:`python3:cmath.asinh`, :func:`python3:cmath.atan`, :func:`python3:cmath.atanh`, :func:`python3:cmath.cos`, :func:`python3:cmath.cosh`, :func:`python3:cmath.e`, :func:`python3:cmath.exp`, :func:`python3:cmath.log`, :func:`python3:cmath.log10`, :func:`python3:cmath.pi`, :func:`python3:cmath.sin`, :func:`python3:cmath.sinh`, :func:`python3:cmath.sqrt`, :func:`python3:cmath.tan`, :func:`python3:cmath.tanh`.

To make it clear in the code that these functions are special functions for
complex numbers, and to avoid name conflicts with the more normal equivalents,
it is recommended to simply import the module to explicitly refer to the
``cmath`` package when using the function, for example:

.. code-block:: pycon

    >>> import cmath
    >>> cmath.sqrt(-2)
    1.4142135623730951j

.. warning::

    Now it becomes clearer why we do not recommend importing all functions of a
    module with :samp:`from {MODULE} import \*`. If you would import the module
    ``math`` first and then the module ``cmath``, the functions in ``cmath``
    would have priority over those of ``math``. Also, when understanding the
    code, it is much more tedious to find out the source of the functions used.

Checks
------

* Load the :mod:`math` module and try out some of the functions. Then load the
  :mod:`cmath` module and do the same.

* How can you restore the functions of the :mod:`math` module?
