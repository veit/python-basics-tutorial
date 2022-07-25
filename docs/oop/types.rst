Data types as objects
=====================

By now you have learned the basic Python :doc:`data types <../types/index>` and
know how to create your own data types using :doc:`classes`. Note that Python is
dynamically typed, which means that the types are determined at runtime, not
compile time. This is one of the reasons why Python is so easy to use. You can
simply try the following:

.. code-block:: python

    >>> type(3)
    <class 'int'>
    >>> type('Hello')
    <class 'str'>
    >>> type(['Hello', 'Pythonistas'])
    <class 'list'>

In these examples you can see the built-in :class:`type` function in Python. It
can be applied to any Python object and returns the type of the object. In this
example, the function tells you that ``3`` is an ``int`` (integer), that
``'Hello'`` is a ``str`` (string) and that ``['Hello', 'Pythonistas']`` is a
``list``.

Of greater interest, however, may be the fact that Python returns objects in
response to calls to :class:`type`; ``<<class 'int'>``, ``<<class 'str'>`` and
``<<class 'list'>`` are the screen representations of the returned objects. So
you can compare these Python objects with each other:

.. code-block:: python

    >>> type('Hello') == type('Pythonistas!')
    True
    >>> type('Hello') == type('Pythonistas!') == type(['Hello', 'Pythonistas'])
    False

With this technique you can, among other things, perform a type check in your
function and method definitions. However, the most common question about the
types of objects is whether a particular object is an instance of a class. An
example with a simple inheritance hierarchy makes this clearer:

#. First, we define two classes with an inheritance hierarchy:

    .. code-block:: python

        >>> class Form:
        ...     pass
        ...
        >>> class Square(Form):
        ...     pass
        ...
        >>> class Circle(Form):
        ...     pass

#. Now you can create an instance ``c1`` of the class ``Circle``:

    .. code-block:: python

        >>> c1 = Circle()

#. As expected, the ``type`` function on ``c1`` outputs that ``c1`` is an
   instance of the class ``Circle`` defined in your current ``__main__``
   namespace:

    .. code-block:: python

        >>> type(c1)
        <class '__main__.Circle'>

#. You can also get exactly the same information by accessing the ``__class__``
   attribute of the instance:

    .. code-block:: python

        >>> c1.__class__
        <class '__main__.Circle'>

#. You can also explicitly check whether the two class objects are identical:

    .. code-block:: python

        >>> c1.__class__ == Circle
        True

#. However, two built-in functions provide a more user-friendly way of obtaining
   most of the information normally required:

   :func:`python3:isinstance`
        determines whether, for example, a class passed to a function or method
        is of the expected type.
   :func:`python3:issubclass`
        determines whether one class is the subclass of another.

    .. code-block:: python

        >>> issubclass(Circle, Form)
        True
        >>> issubclass(Square, Form)
        True
        >>> isinstance(c1, Form)
        True
        >>> isinstance(c1, Square)
        False
        >>> isinstance(c1, Circle)
        True
        >>> issubclass(c1.__class__, Form)
        True
        >>> issubclass(c1.__class__, Square)
        False
        >>> issubclass(c1.__class__, Circle)
        True

Duck typing
-----------

The use of :class:`python3:type`, :func:`python3:isinstance` and
:func:`python3:issubclass` makes it fairly easy to correctly determine the
inheritance hierarchy of an object or class. However, Python also has a feature
that makes using objects even easier: duck typing – *„If it walks like a duck
and it quacks like a duck, then it must be a duck“*. This refers to Python’s way
of determining whether an object is the required type for an operation, focusing
on the interface of an object. In short, in Python you don’t have to worry about
type-checking function or method arguments and the like, but instead rely on
readable and documented code in conjunction with tests to ensure that an object
„quacks like a duck when needed.“

Duck typing can increase the flexibility of well-written code and, in
combination with advanced object-oriented functions, gives you the ability to
create classes and objects that cover almost any situation. Such :ref:`special
methods <python3:specialnames>` are attributes of a class with special meaning
for Python. While they are defined as methods, they are not intended to be
called directly; instead, they are called automatically by Python in response to
a request to an object of that class.

One of the simplest examples of a special method is :meth:`object.__str__`. When
defined in a class, the ``__str__`` method attribute is called whenever an
instance of that class is used and Python requires a user-readable string
representation of that instance. To see this attribute in action, we again use
our ``Form`` class with the standard ``__init__`` method to initialise instances
of the class, but also a ``__str__`` method to return strings representing
instances in a readable format:

.. code-block:: python

    >>> class Form:
    ...     def __init__(self, x, y):
    ...         self.x = x
    ...         self.y = y
    ...     def __str__(self):
    ...         return "Position: x={0}, y={1}".format (self.x, self.y)
    ...
    >>> f = Form(2,3)
    >>> print(f)
    Position: x=2, y=3

Even though our special ``__str__`` method attribute was not explicitly called
by our code, it could still be used by Python because Python knows that the
``__str__`` attribute, if present, defines a method for converting objects into
user-readable strings. And this is exactly what distinguishes the special method
attributes. For example, it is often a good idea to define the ``__str__``
attribute for a class so that you can call ``print(instance)`` in debugging code
and get an informative statement about your object.

Conversely, however, it may be surprising that an object type reacts differently
to special method attributes. Therefore, I usually use special method attributes
only in one of the following two cases:

* in a commonly used class, usually for sequences, that behaves similarly to a
  Python built-in type, and which is made more useful by special method
  attributes.
* in a class that behaves almost identically to a built-in class, for example
  lists implemented as balanced trees to speed up insertion, I can define the
  special method attributes.
