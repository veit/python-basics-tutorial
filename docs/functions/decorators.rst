Decorators
==========

Functions can also be passed as arguments to other functions and return the
results of other functions. For example, it is possible to write a Python
function that takes another function as a parameter, embeds it in another
function that does something similar, and then returns the new function. This
new combination can then be used instead of the original function:

.. code-block:: python
   :linenos:

    >>> def inf(func):
    ...     print("Information about", func.__name__)
    ...     def details(*args):
    ...         print("Execute function", func.__name__, "with the argument(s)")
    ...         return func(*args)
    ...     return details
    ...
    >>> def my_func(*params):
    ...     print(params)
    ...
    >>> my_func = inf(my_func)
    Information about my_func
    >>> my_func("Hello", "Pythonistas!")
    Execute function my_func with the argument(s)
    ('Hello', 'Pythonistas!')

Line 2
    The ``inf`` function outputs the name of the function it wraps.
Line 6
    When finished, the ``inf`` function returns the wrapped function.

A decorator is `syntactic sugar
<https://en.wikipedia.org/wiki/Syntactic_sugar>`_ for this process and allows
you to wrap one function inside another with a one-line addition. You still get
exactly the same effect as with the previous code, but the resulting code is
much cleaner and easier to read. Using a decorator simply consists of two parts:

#. the definition of the function to wrap or *decorate* other functions, and
#. the use of an ``@`` followed by the decorator just before the wrapped
   function is defined.

The decorator function should take a function as a parameter and return a
function, as follows:

.. code-block:: python
   :linenos:

    >>> @inf
    ... def my_func(*params):
    ...     print(params)
    ...
    Information about my_func
    >>> my_func("Hello", "Pythonistas!")
    Execute function my_func with the argument(s)
    ('Hello', 'Pythonistas!')

Line 1
    The function ``my_func`` is decorated with ``@inf``.
Line 7
    The wrapped function is called after the decorator function is finished.
