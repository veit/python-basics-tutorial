Decorators
==========

Functions can also be passed as arguments to other functions and return the
results of other functions. For example, it is possible to write a Python
function that takes another function as a :term:`parameter`, embeds it in
another function that does something similar, and then returns the new function.
This new combination can then be used instead of the original function:

.. code-block:: pycon
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

The decorator function should take a function as a :term:`parameter` and return
a function, as follows:

.. code-block:: pycon
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

``functools``
-------------

The Python :mod:`functools` module is intended for higher-order functions, for
example functions that act on or return other functions. Mostly you can use them
as decorators, such as:

:func:`functools.cache`
    Simple, lightweight, function cache as of Python ≥ 3.9, sometimes called
    *memoize*. It returns the same as :func:`functools.lru_cache` with the
    :term:`parameter` ``maxsize=None``, additionally creating a
    :doc:`/types/dicts` with the function arguments. Since old values never
    need to be deleted, this function is then also smaller and faster. Example:

    .. code-block:: pycon
       :linenos:

       >>> import timeit
       ... from functools import cache
       ... @cache
       ... def factorial(n):
       ...     return n * factorial(n - 1) if n else 1
       ... timeit.timeit("factorial(8)", globals=globals())
       0.02631620899774134

    Line 1
        imports the :mod:`timeit` module for measuring execution time.
    Line 2
        imports :func:`functools.cache`.
    Line 5
        The ``@cache`` decorator is used to store intermediate results, which
        can then be reused. In our case, the execution speed is increased
        approximately tenfold.
    Line 10
        :func:`timeit.timeit` measures the time of a call. Unless otherwise
        specified, the call is made one million times.

:func:`functools.wraps`
    This decorator makes the wrapper function look like the original function
    with its name and properties.

    .. code-block:: pycon

       >>> from functools import wraps
       >>> def my_decorator(f):
       ...     @wraps(f)
       ...     def wrapper(*args, **kwargs):
       ...         """Wrapper docstring"""
       ...         print("Call decorated function")
       ...         return f(*args, **kwargs)
       ...     return wrapper
       ...
       >>> @my_decorator
       ... def example():
       ...     """Example docstring"""
       ...     print("Call example function")
       ...
       >>> example.__name__
       'example'
       >>> example.__doc__
       'Example docstring'

    Without ``@wraps`` decorator, the name and docstring of the wrapper method
    would have been returned instead:

    .. code-block:: pycon

       >>> example.__name__
       'wrapper'
       >>> example.__doc__
       'Wrapper docstring'

.. tip::
   `cusy seminar: Advanced Python
   <https://cusy.io/en/our-training-courses/advanced-python.html>`_
