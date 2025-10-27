Parameters
==========

Python offers flexible mechanisms for passing :term:`arguments <argument>` to
:term:`functions <function>`:

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
    >>> def func3(u, v=1, w=1, *args):
    ...     print((u, v, w) + args)
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
    Function :term:`parameters <Parameter>` can be defined with default values
    that will be used if a function call omits them.
Line 18
    A special :term:`parameter` can be defined that combines all additional
    positional arguments in a function call into one tuple.
Line 25
    Similarly, a special :term:`parameter` can be defined that summarises all
    additional keyword arguments in a function call in a dictionary.

Options for function parameters
-------------------------------

Most functions need :term:`parameters <Parameter>`. Python offers three options
for defining function parameters.

Positional parameters
~~~~~~~~~~~~~~~~~~~~~

The simplest way to pass :term:`parameters <Parameter>` to a function in Python
is to pass them at the position. On the first line of the function, you specify
the variable name for each parameter; when the function is called, the
parameters used in the calling code are assigned to the function’s parameter
variables based on their order. The following function calculates ``x`` as a
power of ``y``:

.. code-block:: pycon

    >>> def power(x, y):
    ...     p = 1
    ...     while y > 0:
    ...         p = p * x
    ...         y = y - 1
    ...     return p
    ...
    >>> power(2, 5)
    32

This method requires that the number of :term:`parameters <Parameter>` used by
the calling code exactly matches the number of parameters in the function
definition; otherwise, a type error exception is thrown:

.. code-block:: pycon

    >>> power(2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: power() missing 1 required positional argument: 'y'

Function :term:`parameters <Parameter>` can have default values, which you can
declare by assigning a default value in the first line of the function
definition, like this:

.. code-block:: pycon

    def function_name(param1, param2=Standardwert2, param3=Standardwert3, ...)

Any number of :term:`parameters <Parameter>` can be given default values, but
parameters with default values must be defined as the last in the parameter
list.

The following function also calculates ``x`` as a power of ``y``. However, if
``y`` is not specified in a function call, the default value ``5`` is used:

.. code-block:: pycon

    >>> def power(x, y=5):
    ...     p = 1
    ...     while y > 0:
    ...         p = p * x
    ...         y = y - 1
    ...     return p
    ...

You can see the effect of the standard argument in the following example:

.. code-block:: pycon

    >>> power(3, 6)
    729
    >>> power(3)
    243

Parameter names
~~~~~~~~~~~~~~~

You can also pass arguments to a function by using the name of the corresponding
function :term:`parameter` rather than its position. Similar to the previous example,
you can enter the following:

.. code-block:: pycon

    >>> power(y=6, x=2)
    64

Since the arguments for the power are named ``x`` and ``y`` in the last call,
their order is irrelevant; the arguments are linked to the :term:`parameters
<Parameter>` of the same name in the definition of the power, and you get back
``2^6``. This type of argument passing is called keyword passing. Keyword
passing can be very useful in combination with the default arguments of Python
functions when you define functions with a large number of possible arguments,
most of which have common default values.

Variable number of arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python functions can also be defined to handle a variable number of arguments.
This is possible in two ways. One method collects an unknown number of arguments
in a :doc:`list </types/sequences-sets/lists>`. The other method can collect an
arbitrary number of arguments passed with a keyword that has no correspondingly
named :term:`parameter` in the function parameter list in a :doc:`dict
</types/dicts>`.

For an indeterminate number of positional arguments, prefixing the function’s
final :term:`parameter` name with a ``*`` causes all excess non-keyword
arguments in a function call, that is, the positional arguments that are not
assigned to any other parameter, to be collected and assigned as a tuple to the
specified parameter. This is, for example, a simple way to implement a function
that finds the mean in a list of numbers:

.. code-block:: pycon

    >>> def mean(*numbers):
    ...     if len(numbers) == 0:
    ...         return None
    ...     else:
    ...         m = sum(numbers) / len(numbers)
    ...     return m
    ...

Now you can test the behaviour of the function, for example with:

.. code-block:: pycon

    >>> mean(3, 5, 2, 4, 6)
    4.0

Any number of keyword arguments can also be processed if the last
:term:`parameter` in the parameter list is prefixed with ``**``. Then all
arguments passed with a keyword are collected in a :doc:`dict </types/dicts>`.
The key for each entry in the dict is the keyword (parameter name) for the
argument. The value of this entry is the argument itself. An argument passed by
keyword is superfluous in this context if the keyword with which it was passed
does not match one of the parameter names in the function definition, for
example:

.. code-block:: pycon

    >>> def server(ip, port, **other):
    ...     print(
    ...         "ip: {0}, port: {1}, keys in 'other': {2}".format(
    ...             ip, port, list(other.keys())
    ...         )
    ...     )
    ...     total = 0
    ...     for k in other.keys():
    ...         total = total + other[k]
    ...     print("The sum of the other values is {0}".format(total))
    ...

Trying out this function shows that it can add the arguments passed under the
keywords ``foo``, ``bar`` and ``baz``, even though ``foo``, ``bar`` and ``baz``
are not :term:`parameter` names in the function definition:

.. code-block:: pycon

    >>> server("127.0.0.1", port="8080", foo=3, bar=5, baz=2)
    ip: 127.0.0.1, port: 8080, keys in 'other': ['foo', 'bar', 'baz']
    The sum of the other values is 10

Mixing argument passing techniques
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to use all the argument passing techniques of Python functions at
the same time, although this can be confusing if you don’t do it carefully.
Positional arguments should come first, then named arguments, followed by
indefinite positional arguments with a simple ``*``, and finally indefinite
keyword arguments with ``**``.

Mutable objects as arguments
----------------------------

Arguments are passed by object reference. The :term:`parameter` becomes a new
reference to the object. With :term:`immutable` objects such as
:doc:`/types/sequences-sets/tuples`, :doc:`/types/strings/index` and
:doc:`/types/numbers/index`, what is done with a parameter has no effect outside
the function. However, if you pass a mutable object, such as a
:doc:`/types/sequences-sets/lists`, a :doc:`/types/dicts` or a class instance,
any change to the object changes what the argument refers to outside the
function. Reassigning the parameter has no effect on the argument.

.. code-block:: pycon

    >>> def my_func(n, l):
    ...     l.append(1)
    ...     n = n + 1
    ...
    >>> x = 5
    >>> y = [2, 4, 6]
    >>> my_func(x, y)
    >>> x, y
    (5, [2, 4, 6, 1])

The variable ``x`` is not changed because it is :term:`immutable`. Instead, the
function :term:`parameter` ``n`` is set so that it refers to the new value
``6``. However, there is a change in ``y`` because the list it refers to has
been changed.

Checks
------

* Write a function that can take any number of unnamed arguments and output
  their values in reverse order?
