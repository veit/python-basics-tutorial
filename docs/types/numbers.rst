Numbers
=======

Python’s four number types are integers, floating point numbers, complex numbers
and Boolean numbers:

+-----------------------+-----------------------------------------------+
| Type                  | Examples                                      |
+=======================+===============================================+
| Integers              | ``-1``, ``42``, ``90000000``                  |
+-----------------------+-----------------------------------------------+
| Floats                | ``90000000.0``, ``-0.005``, ``9e7``, ``-5e-3``|
+-----------------------+-----------------------------------------------+
| Complex numbers       | ``3 + 2j``, ``-4- 2j``, ``4.2 + 6.3j``        |
+-----------------------+-----------------------------------------------+
| Boolean numbers       | ``True``, ``False``                           |
+-----------------------+-----------------------------------------------+

They can be manipulated with the arithmetic operators:

+-----------------------+-----------------------------------------------+
| Operator              | Description                                   |
+=======================+===============================================+
| ``+``                 | Addition                                      |
+-----------------------+-----------------------------------------------+
| ``-``                 | Subtraction                                   |
+-----------------------+-----------------------------------------------+
| ``*``                 | Multiplication                                |
+-----------------------+-----------------------------------------------+
| ``/``, ``//``         | Division [#]_                                 |
+-----------------------+-----------------------------------------------+
| ``**``                | Exponentiation                                |
+-----------------------+-----------------------------------------------+
| ``%``                 | Modulus                                       |
+-----------------------+-----------------------------------------------+

.. [#] Dividing integers with ``/`` results in a float, and dividing integers
       with ``//`` results in an integer that is truncated.

.. note::
   Integers can be unlimited in size, limited only by the available memory.

Examples:

.. code-block:: python

    >>> 8 + 3 - 5 * 3
    -4
    >>> 8 / 3
    2.6666666666666665
    >>> 8 // 3
    2
    >>> x = 4.2 ** 3.4
    >>> x
    131.53689544409096
    >>> 9e7 * -5e-3
    -450000.0
    >>> -5e-3 ** 3
    -1.2500000000000002e-07

The following examples use complex numbers:

.. code-block:: python

    >>> (5+3j) ** (3+5j)
    (-7.04464115622119-11.276062812695923j)

.. code-block:: python

    >>> x = (5+3j) * (6+8j)
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

Built-in numerical functions
----------------------------

Several built-in functions can work with numbers:

:func:`python3:abs`
    returns the absolute value of a number. Here, as argument can be an integer,
    a floating point number or an object that implements ``__abs__()``. With
    complex numbers as arguments, their absolute value is returned.
:func:`python3:divmod`
    takes two (non-complex) numbers as arguments and returns a pair of numbers
    consisting of their quotient and the remainder if integer division is used.
:class:`python3:float`
    returns a floating point number formed from a number or string ``x``.
:func:`python3:hex`
    converts an integer number to a lowercase hexadecimal string with the
    prefix ``0x``.
:class:`python3:int`
    returns an integer object constructed from a number or string ``x``, or
    ``0`` if no arguments are given.
:func:`python3:max`
    returns the largest element in an :term:`python3:iterable` or the largest of
    two or more arguments.
:func:`python3:min`
    returns the smallest element in an iterable or the smallest of two or more
    arguments.
:func:`python3:oct`
    converts an integer number to an octal string with the prefix ``0o``. The
    result is a valid Python expression. If ``x`` is not a Python :func:`int`
    object, it must define an ``__index__()`` method that returns an integer.
:func:`python3:pow`
    returns *base* as a power of *exp*.
:func:`python3:round`
    returns a number rounded to *ndigits* after the decimal point. If *ndigits*
    is omitted or is *None*, the nearest integer to the input is returned.

Boolean values
--------------

Boolean values are used in the following examples:

.. code-block:: python

    >>> x = False
    >>> x
    False
    >>> not x
    True

.. code-block:: python

    >>> y = True * 2
    >>> y
    2

Apart from their representation as ``True`` and ``False``, Boolean values
behave like the numbers ``1`` (``True``) and ``0`` (``False``).

Advanced numerical functions
----------------------------

More advanced numerical functions such as trigonometry, as well as some useful
constants, are not built into Python, but are provided in a standard module
called :doc:`math <python3:library/math>`. Modules will be explained in more
detail later. For now, suffice it to say that you need to make the maths
functions available in this section by importing everything from ``math``:

.. code-block:: python

    from math import *

Built-in functions are always available and are called using standard function
call syntax. In the following code, ``round`` is called with a float as the
input argument.

.. code-block:: python

    >>> round(1.49)
    1

With ``ceil`` from the standard library ``math`` and the attribute notation
:samp:`MODUL.FUNKTION(ARGUMENT)` is rounded up:

.. code-block:: python

    >>> import math
    >>> math.ceil(1.49)
    2

The ``math`` module provides, among other things

* the number theoretic and representation functions :func:`python3:math.ceil`,
  :func:`python3:math.modf`, :func:`python3:math.frexp` and
  :func:`python3:math.ldexp`,
* the power and logarithmic functions :func:`python3:math.exp`,
  :func:`python3:math.log`, :func:`python3:math.log10`, :func:`python3:math.pow`
  and :func:`python3:math.sqrt`,
* the trigonometric functions :func:`python3:math.acos`,
  :func:`python3:math.asin`, :func:`python3:math.atan`,
  :func:`python3:math.atan2`, :func:`python3:math.ceil`,
  :func:`python3:math.cos`, :func:`python3:math.hypot` and
  :func:`python3:math.sin`,
* the hyperbolic functions :func:`python3:math.cosh`,
  :func:`python3:math.sinh` and :func:`python3:math.tanh`
* and the constants :data:`python3:math.e` und :data:`python3:math.pi`.

There is also the library module :doc:`cmath <python3:library/cmath>` which
contains functions for complex numbers.

Numerical calculations
----------------------

The standard Python installation is not well suited for intensive numerical
calculations due to speed limitations. But the powerful Python extension
:doc:`jupyter-tutorial:workspace/numpy/index` provide highly efficient
implementations of many advanced numerical operations. The focus is on array
operations, including multi-dimensional matrices and advanced functions such as
the fast Fourier transform.
