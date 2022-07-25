Summary
=======

The points made so far, are the basics of using classes and objects in Python. I
will now summarise these basics in a single example:

#. First, we create a base class:

    .. literalinclude:: form.py
        :language: python
        :linenos:
        :lines: 1-9
        :lineno-start: 1

    Line 4
        The ``__init__`` method requires one instance (``self``) and two
        parameters.
    Lines 5 and 6
        The two instance variables ``x`` and ``y``, which are accessed via
        ``self``.
    Line 7
        The ``move`` method requires one instance (``self``) and two parameters.
    Lines 8 and 9
        Instance variables that are set in the ``move`` method.

#. Next, create a subclass that inherits from the base class ``Form``:

    .. literalinclude:: form.py
        :language: python
        :linenos:
        :lines: 11-17
        :lineno-start: 11

    Line 11
        The class ``Square`` inherits from the class ``Form``.
    Line 13
        ``Square``’s ``__init__`` takes one instance (``self``) and three
        parameters, all with defaults.
    Line 14
        ``Circle``’s ``__init__`` uses ``super()`` to call ``Form``’s
        ``__init__``.

#. Finally, we create another subclass that also contains a static method:

    .. literalinclude:: form.py
        :language: python
        :linenos:
        :lines: 19-35
        :lineno-start: 19

    Lines 21 and 22
        ``pi`` and ``circles`` are class variables for ``Circle``.
    Line 26
        In the ``__init__`` method, the instance inserts itself into the
        ``circles`` list.
    Lines 29 and 30
        ``circumferences`` is a class method and takes the class itself
        (``cls``) as a parameter.
    Line 33
        uses the parameter ``cls`` to access the class variable ``circles``.

Now you can create some instances of the class ``Circle`` and analyse them.
Since the ``__init__`` method of ``Circle`` has default parameters, you can
create a circle without specifying any parameters:

    .. code-block:: python

        >>> import form
        >>> c1 = form.Circle()
        >>> c1.diameter, c1.x, c1.y
        (1, 0, 0)

If you specify parameters, they are used to set the values of the instance:

    .. code-block:: python

        >>> c2 = form.Circle(2, 3, 4)
        >>> c2.diameter, c2.x, c2.y
        (2, 3, 4)

When you call the ``move()`` method, Python does not find a ``move()`` method in
the ``Circle`` class, so it goes up the inheritance hierarchy and uses the
``move()`` method of ``Form``:

    .. code-block:: python

        >>> c2.move(5, 6)
        >>> c2.diameter, c2.x, c2.y
        (2, 8, 10)

You can also call the class method ``circumferences()`` of the class ``Circle``,
either through the class itself or through an instance:

    .. code-block:: python

        >>> form.Circle.circumferences()
        9.424769999999999
        >>> c2.circumferences()
        9.424769999999999
