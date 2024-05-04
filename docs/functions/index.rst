Functions
=========

Basic function definitions
--------------------------

The basic syntax for a Python function definition is

.. code-block:: python

    def function_name(param1, param2):
        body

As with :doc:`control streams </control-flows/index>`, Python uses indentation
to separate the function from the function definition. The following simple
example inserts the code into a function so that you can call it to get the
`factorial <https://en.wikipedia.org/wiki/Factorial>`_ of a number:

.. code-block:: pycon
   :linenos:

    >>> def fact(n):
    ...     """Return the factorial of the given number."""
    ...     f = 1
    ...     while n > 0:
    ...         f = f * n
    ...         n = n - 1
    ...     return f
    ...

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
    functions that have no return statement and return :doc:`/types/none`, and
    when ``return arg`` is executed, the value ``arg`` is returned.

Although all Python functions return values, it is up to you how the return
value of a function is used:

.. code-block:: pycon
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

Parameters
----------

Python offers flexible mechanisms for passing arguments to functions:

.. code-block:: pycon
    :linenos:

    >>> x, y = 2, 3
    >>> def func1(u, v, w):
    ...     value = u + 2 * v + w**2
    ...     if value > 0:
    ...         return u + 2 * v + w**2
    ...     else:
    ...         return 0
    ...
    >>> func1(x, y, 2)
    12
    >>> func1(x, w=y, v=2)
    15
    >>> def func2(u, v=1, w=1):
    ...     return u + 4 * v + w**2
    ...
    >>> func2(5, w=6)
    45
    >>> def func3(u, v=1, w=1, *tup):
    ...     print((u, v, w) + tup)
    ...
    >>> func3(7)
    (7, 1, 1)
    >>> func3(1, 2, 3, 4, 5)
    (1, 2, 3, 4, 5)
    >>> def func4(u, v=1, w=1, **kwargs):
    ...     print(u, v, w, kwargs)
    ...
    >>> func4(1, 2, s=4, t=5, w=3)
    1 2 3 {'s': 4, 't': 5}

Line 2
    Functions are defined with the ``def`` statement.
Line 5
    The ``return`` statement is used by a function to return a value. This value
    can be of any type. If no ``return`` statement is found, the value ``None``
    is returned by Python.
Line 11
    Function arguments can be entered either by position or by name (keyword).
    ``z`` and ``y`` are specified by name in our example.
Line 13
    Function parameters can be defined with default values that will be used if
    a function call omits them.
Line 18
    A special parameter can be defined that combines all additional positional
    arguments in a function call into one tuple.
Zeile 25
    Similarly, a special parameter can be defined that summarises all additional
    keyword arguments in a function call in a dictionary.

.. toctree::
   :titlesonly:
   :hidden:

   params
   variables
   decorators
   lambda
