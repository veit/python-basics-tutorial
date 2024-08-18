Methods
=======

A method is a function associated with a particular class. You have already seen
the special ``__init__`` method that is called when a new instance is created.
In the following example, you define another method, ``circumference``, for the
class ``Square``; this method can be used to calculate and return the
circumference for any ``Square`` instance. Like most custom methods,
``circumference`` is called with a syntax similar to accessing instance
variables:

.. code-block:: pycon

    >>> class Square:
    ...     def __init__(self):
    ...         self.length = 1
    ...     def circumference(self):
    ...         return 4 * self.length
    ...
    >>> s = Square()
    >>> s.length = 5
    >>> print(s.circumference())
    20

The syntax for method calls consists of an instance followed by a dot followed
by the method to be called on the instance. If a method is called in this way,
it is a bound method call. However, a method can also be called as an unbound
method by accessing it through its containing class. This practice is less
practical and is almost never used because the first argument of a method called
in this way must be an instance of the class in which the method is defined and
is less clear:

.. code-block:: pycon

    >>> print(Square.circumference(s))
    20

Like ``__init__``, the ``circumference`` method is defined as a function within
the class. The first argument of each method is the instance from which or on
which it was called, by convention called ``self``. In many languages, the
instance is called ``this`` and is never explicitly passed.

Methods can be called with arguments if the method definitions accept those
arguments. This version of ``Square`` adds an argument to the ``__init__``
method so that you can create squares with a specific edge length without having
to set the edge length after creating a square:

.. code-block:: pycon

    >>> class Square:
    ...     def __init__(self, length):
    ...         self.length = length
    ...     def circumference(self):
    ...         return 4 * self.length
    ...

.. warning::

    ``self.length`` and ``length`` are not the same!

    * ``self.length`` is the instance variable called ``length``
    * ``length`` is the local function parameter

    In practice, you would probably refer to the local function parameter as
    ``lng`` or ``l`` to avoid confusion.

With this definition of ``Square``, you can create squares with arbitrary edge
lengths with a call to the ``Square`` class. In the following, a square with
edge length ``3`` is created:

.. code-block:: pycon

    s = Square(3)

All of Python’s standard functions – standard arguments, additional arguments,
keyword arguments, :abbr:`etc. (et cetera)` – can be used with methods. You
could have defined the first line of ``__init__`` as follows:

.. code-block:: pycon

    ...     def __init__(self, length=1):

Then the call to ``Square`` would work with or without an additional argument;
``Square()`` would return a square with edge length ``1`` and ``Square(3)``
would return a square with edge length ``3``.

For a method call ``instance.method(arg1, arg2, …)``, Python converts it to a
normal function call by applying the following rules:

#. Search for the method name in the instance namespace. If a method has been
   changed or added for this instance, it is called in preference to methods in
   the class.
#. If the method is not found in the instance namespace, the method is searched
   in the class. In the previous examples, ``class`` is the ``Square`` type of
   the instance ``s``.
#. If the method is still not found, it is searched for in a superclass, see
   also :doc:`inheritance`.
#. If the method is found, it is called as a normal Python function, using
   instance as the first argument of the function and shifting all other
   arguments in the method call one space to the right. Thus
   ``instance.method(arg1, arg2, …)`` becomes
   ``class.method(instance, arg1, arg2, …)``.

Static methods
--------------

Just like in Java, you can call static methods even if no instance of that class
has been created. To create a static method, use the :func:`@staticmethod
<python3:staticmethod>` :doc:`decorator </functions/decorators>`:

.. literalinclude:: circle.py
    :linenos:

Line 11
    defines the class variable ``circles`` as an initially empty list of all
    ``Circle`` instances.
Line 14
    adds initialised ``Circle`` instances to the ``circles`` list.

.. code-block:: pycon

    >>> import circle
    >>> c1 = circle.Circle(1)
    >>> c2 = circle.Circle(2)
    >>> circle.Circle.circumferences()
    9.424769999999999
    >>> c2.diameter = 3
    >>> circle.Circle.circumferences()
    12.56636

Class methods
-------------

:func:`Class methods <classmethod>` are similar to static methods in that they
can be called before an object of the class has been instantiated. However, the
class to which they belong is implicitly passed to the class methods as the
first parameter:

.. literalinclude:: circle_cm.py
    :language: python
    :linenos:
    :lines: 23-
    :lineno-start: 23

Line 23
    The ``@classmethod`` decorator is used before the ``def`` method.
Line 24
    The class parameter is traditionally ``cls``.
Line 27
    You can use ``cls`` instead of ``self.__class__``.

    By using a class method instead of a static method, you don’t have to
    hardcode the class name in ``circumferences``.

.. code-block:: pycon

    >>> import circle_cm
    >>> c1 = circle_cm.Circle(1)
    >>> c2 = circle_cm.Circle(2)
    >>> circle_cm.Circle.circumferences()
    9.424769999999999

Checks
------

* Writes a class method that is similar to :func:`circumferences`, but returns
  the total area of all circles.
