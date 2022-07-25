Namespaces
==========

If you are in the method of a class, you have direct access

#. to the **local namespace** with the parameters and variables declared in this
   method,
#. the **global namespace** with functions and variables declared at module
   level, and
#. the **built-in namespace** with the built-in functions and built-in
   exceptions.

These three namespaces are searched in this order.

To explain the different namespaces in more detail in our example, we have
extended our existing module to make it clear what can be accessed within a
method: :download:`form_ns.py`.

You can get an overview of the methods that are available in a namespace with

.. literalinclude:: form_ns.py
    :language: python
    :linenos:
    :lines: 48-53
    :lineno-start: 48

.. code-block:: python

    >>> import form_ns
    >>> c1 = form_ns.Circle()
    >>> c1.namespaces()
    Global namespace: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'Form', 'Square', 'Circle']
    Superclass namespace: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'move']
    Class namespace: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'circles', 'circumference', 'circumferences', 'diameter', 'instance_variables', 'move', 'namespaces', 'pi']
    Instance namespace: ['_Circle__diameter', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'circles', 'circumference', 'circumferences', 'diameter', 'instance_variables', 'move', 'namespaces', 'pi', 'x', 'y']
    Local namespace: ['self']

Via the ``self`` variable you also have access to

#. the **namespace of the instance** with

   * instance variables
   * private instance variables and
   * instance variables of the superclass,


#. the **namespace of the class** with

   * methods,
   * class variables,
   * private methods and
   * private class variables and

#. the **namespace of the superclass** with

   * methods of the superclass and
   * class variables of the superclass.

These three namespaces are also searched in this order.

You can now analyse the namespace of the instance with the method
``instance_variables``, for example:

.. literalinclude:: form_ns.py
    :language: python
    :linenos:
    :lines: 54-56
    :lineno-start: 54

.. code-block:: python

    >>> import form_ns
    >>> c1 = form_ns.Circle()
    >>> c1.instance_variables()
    Instance variables self.__diameter, self.x, self.y: 1 0 0

.. note::

    While you can access the ``move`` method of the superclass ``form`` with
    ``self``, private instance variables, private methods and private class
    variables of the superclass are not accessible in this way.
