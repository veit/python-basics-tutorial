Functions
=========

Basic function definitions
--------------------------

The basic syntax for a Python function definition is

.. code-block:: python

    def function_name(param1, param2, ...):
        body

As with :doc:`control streams <control-flows/index>`, Python uses indentation to
separate the function from the function definition. The following simple example
inserts the code into a function so that you can call it to get the `factorial
<[200~https://en.wikipedia.org/wiki/Factorial>`_ of a number:

.. code-block:: python
   :linenos:

    >>> def fact(n):
    ...     """Return the factorial of the given number."""
    ...     f = 1
    ...     while n > 0:
    ...         f = f * n
    ...         n = n - 1
    ...     return f

Line 2
    This is an optional documentation string, or ``docstring``. You can get its
    value by calling ``fact.__doc__``. The purpose of docstrings is to describe
    the behaviour of a function and the parameters it takes, while comments are
    to document internal information about how the code works. Docstrings are
    :doc:`/types/strings` that immediately follow the first line of a function
    definition and are usually enclosed in triple quotes to allow for multi-line
    descriptions. For multi-line documentation strings, it is common to give a
    summary of the function on the first line, follow this summary with an empty
    line and end with the rest of the information.

    .. seealso::
        * :ref:`napoleon`

Line 7
    The value is returned after the function is called. You can also write
    functions that have no return statement and return :doc:`types/none`, and
    when ``return arg`` is executed, the value ``arg`` is returned.

Although all Python functions return values, it is up to you how the return
value of a function is used:

.. code-block:: python
   :linenos:

    >>> fact(3)
    6
    >>> x = fact(3)
    >>> x
    6

Line 1
    The return value is not linked to a variable.
Line 2
    The value of the ``fact`` function is only output in the interpreter.
Line 3
    The return value is linked to the variable ``x``.

Options for function parameters
-------------------------------

Most functions need parameters. Python offers three options for defining
function parameters.

Positional parameters
~~~~~~~~~~~~~~~~~~~~~

The simplest way to pass parameters to a function in Python is to pass them at
the position. On the first line of the function, you specify the variable name
for each parameter; when the function is called, the parameters used in the
calling code are assigned to the function’s parameter variables based on their
order. The following function calculates ``x`` as a power of ``y``:

.. code-block:: python

    >>> def power(x, y):
    ...     p = 1
    ...     while y > 0:
    ...             p = p * x
    ...             y = y - 1
    ...     return p
    ...
    >>> power(2, 5)
    32

This method requires that the number of parameters used by the calling code
exactly matches the number of parameters in the function definition; otherwise,
a type error exception is thrown:

.. code-block:: python

    >>> power(2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: power() missing 1 required positional argument: 'y'

Function parameters can have default values, which you can declare by assigning
a default value in the first line of the function definition, like this:

.. code-block:: python

    def function_name(param1, param2=Standardwert2, param3=Standardwert3, ...)

Any number of parameters can be given default values, but parameters with
default values must be defined as the last in the parameter list.

The following function also calculates ``x`` as a power of ``y``. However, if
``y`` is not specified in a function call, the default value ``5`` is used:

.. code-block:: python

    >>> def power(x, y=5):
    ...     p = 1
    ...     while y > 0:
    ...             p = p * x
    ...             y = y - 1
    ...     return p

You can see the effect of the standard argument in the following example:

.. code-block:: python

    >>> power(3, 6)
    729
    >>> power(3)
    243
