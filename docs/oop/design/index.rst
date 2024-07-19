Object-orientated designs
=========================

In software development, a design pattern describes a relatively small,
well-defined aspect of a computer program in terms of how code is to be written.
The purpose of using a pattern is to utilise an existing concept rather than
reinventing it. This can reduce the time required for software development and
increase the quality of the resulting programme.

    Conformity to patterns is not a measure of quality. [#]_

Although `design patterns <https://en.wikipedia.org/wiki/Design_Patterns>`_ are
language-independent, this does not mean that every pattern is suitable for
every language. In his talk *Design Patterns in Dynamic Languages* from 1996,
Peter Norvig states that 16 of the 23 patterns from the classic book *Design
Patterns* become either invisible or simpler in a dynamic language [#]_. The
authors of the book also recognise in their introduction that the implementation
language determines which patterns are relevant:

    The choice of programming language is important because it influences the
    perspective. Our patterns are based on Smalltalk/C++ language features, and
    this choice determines what can and cannot be easily implemented. If we had
    started from procedural languages, we might have included design patterns
    labelled *inheritance*, *encapsulation* and *polymorphism*. Similarly, some
    of our patterns are directly supported by the less common object-oriented
    languages.

Norvig suggests, among other things, replacing the strategy pattern with
instances of some classes with simple functions and thus reducing a lot of
boilerplate code. In the following :doc:`strategy pattern <strategy>` section,
we will refactor the strategy pattern using function objects.

:doc:`SOLID <solid>` is an acronym for five design principles that are intended
to make object-orientated designs more comprehensible, flexible and
maintainable.

.. tip::
   `cusy seminar: Design patterns in Python
   <https://cusy.io/en/our-training-courses/design-patterns-in-python>`_

.. seealso::
   * `Architecture Patterns with Python
     <https://www.oreilly.com/library/view/architecture-patterns-with/9781492052197/>`_
     by Harry Percival and Bob Gregory
   * `Clean Architectures in Python
     <https://www.thedigitalcatbooks.com/pycabook-introduction/>`_ by Leonardo
     Giordani
   * `Enterprise Integration Patterns
     <https://www.pearson.de/enterprise-integration-patterns-designing-building-and-deploying-messaging-solutions-9780133065107>`_
     by Gregor Hohpe and Bobby Woolf

----

.. [#] Ralph Johnson, co-author of the `design pattern
   <https://en.wikipedia.org/wiki/Design_Patterns>`_ standard book.
.. [#] `Design Patterns in Dynamic Languages
       <http://norvig.com/design-patterns/>`_

.. toctree::
   :titlesonly:
   :hidden:

   solid
   factory
   decorator
   strategy
   command
