SOLID principles
================

`SOLID <https://en.wikipedia.org/wiki/SOLID>`_ is an acronym for the first five
principles of object-oriented design (OOD) by Robert C. Martin (also known as
`Uncle Bob <https://en.wikipedia.org/wiki/Robert_C._Martin>`_).

These principles set out practices for developing software with a view to
maintainability and extensibility as the project grows. Adopting these
principles can also help to avoid code smells, refactor code and develop agile
or adaptive software.

SOLID stands for:

S – :ref:`single-responsibility`
    A class’s methods should be focused on a single purpose.
O – :ref:`open-closed`
    Objects should be open for extension but closed for modification.
L – :ref:`liskov-substitution`
    Subclasses should be substitutable for their superclasses.
I – :ref:`interface-segregation`
    Objects should not depend on methods they do not use.
D – :ref:`dependency-inversion`
    Abstractions should not depend on details.

.. _single-responsibility:

Single Responsibility Principle
-------------------------------

The `Single Responsibility Principle
<https://en.wikipedia.org/wiki/Single-responsibility_principle>`_ states that
each class should fulfil only one task:

    A class should have one, and only one, reason to change.

– `SRP: The Single Responsibility Principle
<https://web.archive.org/web/20140407020253/http://www.objectmentor.com/resources/articles/srp.pdf>`_ by Robert C. Martin

Let’s take, for example, an application that takes a collection of shapes –
circles and squares – and calculates the sum of the perimeters of all the shapes
in the collection.

First, create the :class:`Form` classes with the necessary parameters. For
squares, this is the side length, and for circles, the diameter:

.. literalinclude:: forms.py
   :language: python
   :lines: 4, 6-8, 13-18, 22-24, 27-29

Now you can create a class called :class:`SquaresAndCircles` containing the
logic for calculating the perimeters of all squares and circles:

.. literalinclude:: forms.py
   :language: python
   :lines: 1-3, 35-46

The :class:`SquaresAndCircles` class handles the logic required to calculate the
perimeters of all squares and circles. This fulfils the Single Responsibility
Principle.

.. _open-closed:

Open-Closed Principle
---------------------

The `Open-Closed Principle
<https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle>`_ states:

    Modules should be both open (for extension) and closed (for modification).

Accordingly, the code would require very little modification to add new
functionality, for example, via a subclass.

Let’s look at the :class:`SquaresAndCircles` class and focus on the
:func:`circumferences` method. Imagine a scenario in which the sum of additional
shapes, such as triangles, pentagons, hexagons, :abbr:`etc. (et cetera)`, needs
to be calculated. You would have to constantly edit this class and add further
``if`` blocks. That would violate the :ref:`open-closed`. One way to improve
this method is to remove the logic for calculating the circumference of each
shape from the :class:`SquaresAndCircles` class and attach it to the classes for
the specific shapes. Here, the circumference calculations are defined in the
:class:`Square` and :class:`Circle` classes:

.. literalinclude:: forms.py
   :language: python
   :lines: 15-32

The sum method :func:`circumferences` in the :class:`CircumferenceFormInstances`
class can then be rewritten as follows:

.. literalinclude:: forms.py
   :language: python
   :lines: 49-

This fulfils the Open-Closed Principle.

.. tip::
   If your code is not yet open to new requirements, you should first reorganise
   (refactor) the existing code so that it is open to the new functionality.
   Only then should you add new code.

       Refactoring refers to the process of modifying a software system in such
       a way that the external behaviour of the code remains unchanged, whilst
       its internal structure is improved.

   – `Refactoring
   <https://www.informit.com/store/refactoring-improving-the-design-of-existing-code-9780134757711>`_
   by Martin Fowler

.. note::
   Safe refactoring relies on :doc:`tests <../index>`. If you are genuinely
   restructuring the code without changing its behaviour, the existing tests
   should continue to pass at every stage. The tests act as a safety net that
   justifies your confidence in the new structure of the code. If they fail,

   * you have inadvertently broken the code,
   * or the existing tests are faulty.

.. _liskov-substitution:

Liskov Substitution Principle
-----------------------------

The `Liskov Substitution Principle
<https://en.wikipedia.org/wiki/Liskov_substitution_principle>`_ states that a
programme which uses objects of the base class must also function correctly with
objects of the subclass. There are two rules of thumb that are helpful for
adhering to the Liskov Substitution Principle:

#. Avoid overriding concrete methods wherever possible.
#. If you do so nonetheless, check whether you can call the overridden method
   from within the overriding method.

Let’s extend the :class:`Form` class so that classes derived from it can be
moved in the x and y directions:

.. literalinclude:: forms.py
   :language: python
   :lines: 4-12
   :emphasize-lines: 7-9

You can then move both squares and circles along the x- and y-axes:

.. code-block:: pycon

   >>> import forms
   >>> s1 = forms.Square()
   >>> c1 = forms.Circle()
   >>> s1.x, s1.y, c1.x, c1.y
   (0, 0, 0, 0)
   >>> s1.move(4, 5)
   >>> c1.move(2, 3)
   >>> s1.x, s1.y, c1.x, c1.y
   (4, 5, 2, 3)

.. note::
   The Liskov Substitution Principle also applies to :ref:`duck-typing`: any
   object that claims to be a duck must fully implement the duck’s API. Duck
   types should be interchangeable. Applying logic across different data types
   of objects is known as `polymorphism
   <https://en.wikipedia.org/wiki/Polymorphism_(computer_science)>`_.

.. _interface-segregation:

Interface Segregation Principle
-------------------------------

The `Interface Segregation Principle
<https://en.wikipedia.org/wiki/Interface_segregation_principle>`_ applies the
:ref:`single-responsibility` to interfaces in order to isolate specific
behaviour. If a change is required to part of your code, extracting an object
that plays a particular role makes it possible to support the new behaviour
without having to modify the existing code. This is preferable to hard-coded
specialisations.

In the previous example, for instance, we checked whether our :obj:`Form` object
actually provided a :func:`circumference` method. This is necessary in case
shapes such as :class:`Point` or :class:`Line` are added later, which do not
have a circumference.

.. note::
   In this context, the `Law of Demeter
   <https://en.wikipedia.org/wiki/Law_of_Demeter>`_ is also of interest; it
   states that objects should only communicate with objects in their immediate
   vicinity. This effectively restricts the list of other objects to which an
   object can send a message and reduces coupling between objects: an object
   can only communicate with its neighbours, but not with the neighbours of its
   neighbours; objects can only send messages to those directly involved.

.. _dependency-inversion:

The Dependency Inversion Principle
----------------------------------

The `Dependency Inversion Principle
<https://en.wikipedia.org/wiki/Dependency_inversion_principle>`_ can be defined
as follows:

    Abstractions should not depend on details. Details (concrete
    implementations) should depend on abstractions.

– `The Dependency Inversion Principle
<https://www.cs.utexas.edu/users/downing/papers/DIP-1996.pdf>`_ by Robert C.
Martin

:func:`circumferences` should not be defined within the :class:`Forme` class,
as there are shapes without a circumference.
