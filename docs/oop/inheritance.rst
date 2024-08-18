RClasses and inheritance
========================

Inheritance in Python is simpler and more flexible than inheritance in compiled
languages such as Java and C++ because the dynamic nature of Python does not
impose as many restrictions on the language.

To see how inheritance is used in Python, let’s start with the ``Square`` and
``Circle`` classes we discussed earlier and generalise them.

If we now want to use these classes in a drawing program, we need to define
where on the drawing surface an instance should be located. We can do this by
defining ``x`` and ``y`` coordinates for each instance:

.. code-block:: pycon
    :linenos:

    >>> class Square:
    ...     def __init__(self, length=1, x=0, y=0):
    ...         self.length = length
    ...         self.x = x
    ...         self.y = y
    ...
    >>> class Circle:
    ...     def __init__(self, diameter=1, x=0, y=0):
    ...         self.diameter = diameter
    ...         self.x = x
    ...         self.y = y
    ...

This approach works, but leads to a lot of repetitive code when you increase the
number of shape classes, as you probably want every shape to have this
positional information. This is a standard situation for using inheritance in
object-oriented languages. Instead of defining the ``x`` and ``y`` variables in
each shape class, you can abstract them into a general shape class and have each
class that defines a particular shape inherit from that general class. In
Python, this technique looks like this:

.. code-block:: pycon
    :linenos:

    >>> class Form:
    ...     def __init__(self, x=0, y=0):
    ...         self.x = x
    ...         self.y = y
    ...
    >>> class Square(Form):
    ...     def __init__(self, length=1, x=0, y=0):
    ...         super().__init__(x, y)
    ...         self.length = length
    ...
    >>> class Circle(Form):
    ...     def __init__(self, diameter=1, x=0, y=0):
    ...         super().__init__(x, y)
    ...         self.diameter = diameter
    ...

Lines 6 and 11
    ``Square`` and ``Circle`` inherit from the ``Form`` class.
Lines 8 and 13
    call the ``__init__`` method of the ``Form`` class.

There are generally two requirements when using an inherited class in Python,
both of which you can see in the code of the ``Circle`` and ``Square`` classes:

#. The first requirement is to define the inheritance hierarchy, which you do by
   specifying the classes that are inherited from in parentheses immediately
   after the name of the class, which is defined with the class keyword:
   ``Circle`` and ``Square`` both inherit from ``Form``.
#. The second element is the explicit call to the ``__init__`` method of the
   inherited class. This is not done automatically in Python, but mostly through
   the ``super`` function, more precisely through the lines
   ``super().__init__(x,y)``. This code calls the initialisation function of
   ``Form`` with the instance to be initialised and the corresponding arguments.
   Otherwise, the instance variables ``x`` and ``y`` would not be set for the
   instances of ``Circle`` and ``Square``.

Inheritance also comes into play when you try to use a method that is not
defined in the base classes but in the superclass. To see this effect, define
another method in the ``Form`` class called ``move`` that moves a shape in the
``x`` and ``y`` coordinates. The definition for ``Form`` is now:

.. code-block:: pycon
    :linenos:
    :emphasize-lines: 5-7

    >>> class Form:
    ...     def __init__(self, x=0, y=0):
    ...         self.x = x
    ...         self.y = y
    ...     def move(self, delta_x, delta_y):
    ...         self.x = self.x + delta_x
    ...         self.y = self.y + delta_y
    ...

..
    .. code-block:: pycon

        >>> class Circle(Form):
        ...     def __init__(self, diameter=1, x=0, y=0, delta_x=0, delta_y=0):
        ...         super().__init__(x, y)
        ...         self.diameter = diameter
        ...

If you take the parameters ``delta_x`` and ``delta_y`` of the method ``move`` in
the ``__init__`` methods of ``Circle`` and ``Square``, you can for example
execute the following interactive session:

.. code-block:: pycon

    >>> c = Circle(3)
    >>> c.move(4, 5)
    >>> c.x
    4
    >>> c.y
    5

The class ``Circle`` in the example does not have a ``move`` method defined
directly in itself, but since it inherits from a class that implements ``move``,
all instances of ``Circle`` can use the ``move`` method. In OOP terms, one could
say that all Python methods are virtual – that is if a method does not exist in
the current class, the list of superclasses is searched for the method and the
first one found is used.

Checks
------

* Rewrites the code for a :class:`Triangle` class so that it inherits from
  :class:`Form`.

* How would you write the code to add an :func:`area` method for the
  :class:`Triangle` class? Should the :func:`area` method be moved to the
  :class:`Form` base class and inherited by :class:`Circle`, :class:`Square` and
  :class:`Triangle`? What problems would this change cause?
