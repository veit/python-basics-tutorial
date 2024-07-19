SOLID principles
================

`SOLID <https://en.wikipedia.org/wiki/SOLID>`_  an acronym for the first five
principles of object-oriented design (OOD) by Robert C. Martin (also known as
`Uncle Bob <https://en.wikipedia.org/wiki/Robert_C._Martin>`_).

These principles establish practices for developing software with considerations
for maintenance and extensibility as the project grows. Adopting these
principles can also help to avoid code smells, refactor code and develop agile
or adaptive software.

SOLID stands for:

S – :ref:`single-responsibility`
    The methods of a class should be orientated towards a single purpose.
O – :ref:`open-closed`
    Objects should be open for extensions but closed for changes.
L – :ref:`liskov-substitution`
    Subclasses should be substitutable by their superclasses.
I – :ref:`interface-segregation`
    Objects should not depend on methods that they do not use.
D – :ref:`dependency-inversion`
    Abstractions should not depend on details.

.. _single-responsibility:

Single responsibility principle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `single responsibility principle
<https://en.wikipedia.org/wiki/Single-responsibility_principle>`_ states that
each class should only fulfil one task:

    A class should have one and only one reason to change, meaning that a class
    should have only one job.

– `SRP: The Single Responsibility Principle
<https://web.archive.org/web/20140407020253/http://www.objectmentor.com/resources/articles/srp.pdf>`_
by Robert C. Martin

For example, consider an application that takes a collection of shapes – circles
and squares – and calculates the sum of the circumferences of all the forms in
the collection.

First create the :class:`Form` classes with the necessary parameters. For
squares this is the edge length and for circles the diameter:

.. literalinclude:: forms.py
   :language: python
   :lines: 4-18, 22-24, 27-29

Now you can create a :class:`SquaresAndCircles` class with the logic to
calculate all the circumferences of squares and circles:

.. literalinclude:: forms.py
   :language: python
   :lines: 1-3, 35-46

The :class:`SquaresAndCircles` class takes over the logic required to calculate
all the circumferences of squares and circles. This fulfils the principle of
individual responsibility.

.. _open-closed:

Open-closed principle
---------------------

The :abbr:`OCP (Open-closed principle)` states:

    Objects or entities should be open for extension but closed for
    modification.

This means that a class should be extendable without changing the class itself.

Let’s take a look at the :class:`SquaresAndCircles` class and focus on the
:func:`circumferences` method. Imagine a scenario where you want to calculate
the sum of additional forms such as triangles, pentagons, hexagons, :abbr:`etc.
(et cetera)` You would have to constantly edit this class and add more  ``if``
blocks. This would violate the open-closed principle. One way to improve this
method is to remove the logic for calculating the circumference of each form
from the :class:`SquaresAndCircles` class and attach it to the special form
classes. Here, the circumference calculations are defined in the :class:`Square`
and :class:`Circle` classes:

.. literalinclude:: forms.py
   :language: python
   :lines: 15-32

The :func:`circumferences` sum method in the :class:`CircumferenceFormInstances`
class can then be rewritten as follows:

.. literalinclude:: forms.py
   :language: python
   :lines: 49-

This fulfils the open-closed principle.

.. tip::
   If your code is not yet open for new requirements, you should first
   refactor the existing code so that it is open for the new function. Only
   then should you add new code.

       Refactoring is the process of changing a software system in such a way
       that it does not alter the external behavior of the code yet improves its
       internal structure.

   – `Refactoring
   <https://www.mitp.de/IT-WEB/Software-Entwicklung/Refactoring.html>`_ by
   Martin Fowler

.. note::
   Safe refactoring relies on :doc:`tests </test/index>`. If you really refactor
   the code without changing the behaviour, the existing tests should continue
   to succeed at every step. The tests are a safety net that justifies
   confidence in the new arrangement of the code. If they fail,

   * you have inadvertently broken the code,
   * or the existing tests are flawed.

.. _liskov-substitution:

Liskov substitution principle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Liskov substitution principle
<https://en.wikipedia.org/wiki/Liskov_substitution_principle>`_ states that a
programme that uses objects of the base class must also function correctly with
objects of the subclass.

Let’s extend our :class:`Form` class so that derived forms can be moved in the
x and y directions:

.. literalinclude:: forms.py
   :language: python
   :lines: 4-12
   :emphasize-lines: 7-9

You can then move both squares and circles on the x and y axes:

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
   Liskov’s substitution principle also applies to :ref:`duck-typing`: every
   object that claims to be a duck must fully implement the duck’s API. Duck
   types should be interchangeable. Applying logic across different data types
   of objects is called `polymorphism
   <https://en.wikipedia.org/wiki/Polymorphism_(computer_science)>`_.

.. _interface-segregation:

Interface segregation principle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `interface segregation principle
<https://en.wikipedia.org/wiki/Interface_segregation_principle>`_ applies the
:ref:`single-responsibility` principle to interfaces in order to isolate a
specific behaviour. If a change to a part of your code is required, extracting
an object that plays a role opens up the possibility of supporting the new
behaviour without having to change the existing code. This is preferable to
coded concretisations.

In the previous example, we checked whether our :obj:`Form` object actually
provides a :func:`circumference` method. This is necessary if forms such as
:class:`Point` or :class:`Line` are added later that do not have a
circumference.

.. note::
   In this context, `Demeter’s law
   <https://en.wikipedia.org/wiki/Law_of_Demeter>`_ is also interesting, which
   states that objects should only communicate with objects in their immediate
   vicinity. This effectively restricts the list of other objects to which an
   object can send a message and reduces the coupling between objects: an object
   can only talk to its neighbours, but not to the neighbours of its neighbours;
   objects can only send messages to those directly involved.

.. _dependency-inversion:

Dependency inversion principle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `Dependency inversion principle
<https://en.wikipedia.org/wiki/Dependency_inversion_principle>`_ can be
defined as

    Abstractions should not depend upon details. Details should depend upon
    abstractions.

– `Robert C. Martin: The Dependency Inversion Principle
<https://www.cs.utexas.edu/~downing/papers/DIP-1996.pdf>`_

:func:`circumferences` should not already be defined in the :class:`Form` class,
as there are also forms without circumferences.
