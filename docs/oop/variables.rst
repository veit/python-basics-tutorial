Variables
=========

Instance variables
------------------

In the previous example, ``length`` is an instance variable of ``Square``
instances, which means that each instance of the class ``Square`` has its own
copy of ``length``, and the value stored in this copy may be different from the
values stored in the ``length`` variable in other instances. In Python, you can
create instance variables as needed by assigning them to the field of a class
instance. If the variable does not already exist, it will be created
automatically.

All uses of instance variables, both assignment and access, require explicit
mention of the instance they contain, that is, ``instance.variable``. A
reference to a variable in itself is not a reference to an instance variable,
but to a local variable in the executing method. This is different from C++ and
Java, where instance variables are referenced in the same way as local function
variables of the method. Python requires explicit mention of the contained
instance here, and this enables a clear distinction between instance variables
and local function variables.

Class variables
---------------

A class variable is a variable associated with a class, not an instance of a
class, that can be accessed by all instances of the class. A class variable can
be used to store some class-level information, such as how many instances of the
class were created at a particular time. Python provides class variables,
although using them requires a little more effort than in most other languages.
You also need to be aware of an interaction between class and instance
variables.

A class variable is created by an assignment in the class, but outside the
``__init__`` function. After it is created, it can be seen by all instances of
the class. You can use a class variable to make a value for ``pi`` accessible to
all instances of the ``Circle`` class:

.. code-block:: pycon

   >>> class Circle:
   ...     pi = 3.14159
   ...     def __init__(self, diameter):
   ...         self.diameter = diameter
   ...     def circumference(self):
   ...         return self.diameter * Circle.pi
   ...

Once you have entered this definition, you can query ``pi`` with:

.. code-block:: pycon

   >>> Circle.pi
   3.14159

.. note::

   The class variable is linked to and contained within the class that defines
   it. You access ``Circle.pi`` in this example before any ``Circle`` instances
   have been created. It is obvious that ``Circle.pi`` exists independently of
   specific instances of the ``Circle`` class.

You can also access a class variable from a method of a class using the class
name. You do this in the definition of ``Circle.circumference``, where the
``circumference`` function contains a special reference to ``Circle.pi``:

.. code-block:: pycon

   >>> c = Circle(3)
   >>> c.circumference()
   9.424769999999999

However, it is unpleasant that the class name ``Circle`` is used in the
``circumference`` method to address the class variable ``pi``. You can avoid
this by using the special ``__class__`` attribute, which is available for all
Python class instances. This attribute returns the class to which the instance
belongs, for example:

.. code-block:: pycon

   >>> Circle
   <class '__main__.Circle'>
   >>> c.__class__
   <class '__main__.Circle'>

The ``Circle`` class is internally represented by an abstract data structure,
and this data structure is exactly what is obtained by the ``__class__``
attribute of ``c``, an instance of the ``Circle`` class. In this example, you
can retrieve the value of ``Circle.pi`` from ``c`` without explicitly referring
to the name of the ``Circle`` class:

.. code-block:: pycon

   >>> c.__class__.pi
   3.14159

You can use this code internally in the ``circumference`` method to get rid of
the explicit reference to the ``Circle`` class; replace ``Circle.pi`` with
``self.__class__.pi``.

There is a little oddity about class variables that might confuse you if you are
not aware of it.

.. warning::

   If Python searches for an instance variable and does not find an instance
   variable with that name, it will search for and return the value in a class
   variable with the same name. Only if no matching class variable can be found
   does Python return an error. This can be used to efficiently implement
   default values for instance variables; however, this also easily leads to
   accidentally referring to an instance variable instead of a class variable
   without an error being reported.

   First, you can refer to the variable ``c.pi``, even though ``c`` has no
   associated instance variable called ``pi``. Python first tries to find such
   an instance variable and only when it cannot find an instance variable does
   it look for a class variable ``pi`` in ``Circle``:

   .. code-block:: pycon

      >>> c1 = Circle(1)
      >>> c1.pi
      3.14159

   If you now find that your specification for ``pi`` has been rounded too early
   and you want to replace it with a more precise specification, you might be
   inclined to change it as follows:

   .. code-block:: pycon

      >>> c1.pi = 3.141592653589793
      >>> c1.pi
      3.141592653589793

   However, you have now only added a new instance variable ``pi`` to ``c1``.
   The class variable ``Circle.pi`` and all other instances derived from it
   still have only five decimal places:

   .. code-block:: pycon

      >>> Circle.pi
      3.14159
      >>> c2 = Circle(2)
      >>> c1.pi
      3.14159
