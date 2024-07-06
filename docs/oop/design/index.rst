Design patterns
===============

    Conformity to patterns is not a measure of quality. [#]_

Although design patterns are language-independent, this does not mean that every
pattern is suitable for every language. In his 1996 talk *Design Patterns in
Dynamic Languages*, Peter Norvig notes that 16 of the 23 patterns from the
original `Design Patterns <https://en.wikipedia.org/wiki/Design_Patterns>`_ book
become either invisible or simpler in a dynamic language [#]_. The authors of
*Design Patterns* recognise in their introduction that the implementation
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

   factory
   decorator
   strategy
   command
