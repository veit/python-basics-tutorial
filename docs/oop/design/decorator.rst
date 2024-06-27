Decorator
=========

The Decorator is a structural pattern. The pattern is a flexible alternative to
subclassing in order to extend a class with additional functionalities.

.. warning::
   The Decorator pattern has nothing to do with Python
   :doc:`../../functions/decorators`.

Example
-------

You can find an example of the `Decorator Pattern
<https://wiki.python.org/moin/DecoratorPattern>`_ in the Python wiki. It shows
us how decorators are built into the pipeline to dynamically insert many
behaviours into an object.

Pros and cons
-------------

Pros

* Several decorators can be connected in series.
* The decorators can be exchanged at runtime and even after instantiation.
* The class to be decorated is not necessarily fixed, but its interface is.
* In addition, long and confusing inheritance hierarchies can be avoided.

Cons

* As a decorated component is not identical to the component itself, care must
  be taken when testing for object identity.
* When using decorated components, the messages must be forwarded from the
  decorator to the decorated object.
