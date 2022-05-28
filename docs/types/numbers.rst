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

Several built-in functions can work with numbers. There is also the library
module :doc:`cmath <python3:library/cmath>` (which contains functions for
complex numbers) and the library module :doc:`math <python3:library/math>`
(which contains functions for the other three types):

.. code-block:: python

    >>> round(1.49)
    1

.. code-block:: python

    >>> import math
    >>> math.ceil(1.49)
    2

Built-in functions are always available and are called using standard function
call syntax. In the preceding code, `` is called with a float as the input
argument.

The functions in library modules are made available using the ``import``
instruction. In the last example, the ``math`` library module is imported, and
its ceil function is called with the attribute notation:
:samp:`MODULE.FUNCTION(ARGUMENT)`.

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
