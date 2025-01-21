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

.. code-block:: pycon

    >>> 8 + 3 - 5 * 3
    -4
    >>> 8 / 3
    2.6666666666666665
    >>> 8 // 3
    2
    >>> x = 4.2**3.4
    >>> x
    131.53689544409096
    >>> 9e7 * -5e-3
    -450000.0
    >>> -(5e-3**3)
    -1.2500000000000002e-07

.. seealso::
   * Julia Evans: `Examples of floating point problems
     <https://jvns.ca/blog/2023/01/13/examples-of-floating-point-problems/>`_
   * David Goldberg: `What Every Computer Scientist Should Know About
     Floating-Point Arithmetic
     <https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html>`_

.. toctree::
   :titlesonly:
   :hidden:

   complex
   bool

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

Advanced numerical functions
----------------------------

More advanced numerical functions such as trigonometry, as well as some useful
variables, are not built into Python, but are provided in a standard module
called :doc:`math <python3:library/math>`. :doc:`Module </modules/index>` will
be explained in more detail later. For now, suffice it to say that you need to
make the maths functions available in this section by importing ``math``:

.. code-block:: python

    import math

Built-in functions are always available and are called using standard function
call syntax. In the following code, ``round`` is called with a float as the
input argument.

.. code-block:: pycon

    >>> round(2.5)
    2

With ``ceil`` from the standard library ``math`` and the attribute notation
:samp:`MODULE.FUNCTION(ARGUMENT)` is rounded up:

.. code-block:: pycon

    >>> math.ceil(2.5)
    3

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
* and the variables :data:`python3:math.e` and :data:`python3:math.pi`.

Rounding half to even
---------------------

Usually Python calculates floating point numbers according to the `IEEE 754
<https://en.wikipedia.org/wiki/IEEE_754>`_ standard, rounding down numbers in
the middle half of the time and rounding up in the other half to avoid
statistical drift in longer calculations. :class:`Decimal
<python3:decimal.Decimal>` and :data:`ROUND_HALF_UP
<python3:decimal.ROUND_HALF_UP>` from the decimal module are therefore needed
for `rounding half to even
<https://en.wikipedia.org/wiki/Rounding#Rounding_half_to_even>`_:

.. code-block:: pycon

    >>> import decimal
    >>> num = decimal.Decimal("2.5")
    >>> rounded = num.quantize(decimal.Decimal("0"), rounding=decimal.ROUND_HALF_UP)
    >>> rounded
    Decimal('3')

Built-in modules for numbers
----------------------------

The Python standard library contains a number of built-in modules that you can
use to manage numbers:

.. _number-modules:

+-----------------------+-------------------------------------------------------------------------------+
| Module                | Description                                                                   |
+=======================+===============================================================================+
| :py:mod:`numbers`     | for numeric abstract base classes                                             |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`math`,       | for mathematical functions for real and complex numbers                       |
| :py:mod:`cmath`       |                                                                               |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`decimal`     | for decimal fixed-point and floating-point arithmetic                         |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`statistics`  | for functions for calculating mathematical statistics                         |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`fractions`   | for rational numbers                                                          |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`random`      | for generating pseudo-random numbers and selections and for shuffling         |
|                       | sequences                                                                     |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`itertools`   | for functions that create iterators for efficient loops                       |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`functools`   | for higher-order functions and operations on callable objects                 |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`operator`    | for standard operators as functions                                           |
+-----------------------+-------------------------------------------------------------------------------+

.. _end-number-modules:

.. seealso::
   * :doc:`Python4DataScience:workspace/numpy/index`

Checks
------

* Create some number variables (integers, floating point numbers and complex
  numbers). Experiment a little with what happens when you perform operations
  with them, even across types.
