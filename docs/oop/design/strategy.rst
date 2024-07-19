Strategy pattern
================

In the design pattern book, the `strategy pattern
<https://en.wikipedia.org/wiki/Strategy_pattern>`_ is defined as a family of
algorithms that should be encapsulated and interchangeable. The algorithms vary
independently of the clients.

.. uml::

    title UML class diagram for the strategy design pattern

    abstract class  "Client"
    Client --> Context
    Client --> Strategy

    together {
        interface Context {
            {method} context_interface()
        }
        abstract class Strategy {
            {method} algorithm()
        }
    }
    Context o-> Strategy

    together {
        class ConcreteStrategyA {
            {method} algorithm()
        }
        class ConcreteStrategyB {
            {method} algorithm()
        }
    }
    ConcreteStrategyA -u-|> Strategy
    ConcreteStrategyB -u-|> Strategy

The strategy pattern is a good example of a design pattern that can be simpler
in Python if functions are used as first-class objects. To do this, we first
implement the classic structure of this pattern and then refactor this code
using functions.

An illustrative example of the application of the strategy pattern is the
calculation of discounts on orders depending on the characteristics of the
customers and the items ordered.

Let's take an online shop with the following discount rules:

* Customers with a thousand or more loyalty points receive a global discount of
  5% per order.
* A 10% discount is applied to any item with ten or more units in the same
  order.
* A 7% discount is granted on orders with at least ten different items.

Only one discount can be applied to an order.

Context
    holds a strategy variable that references a specific strategy. In our
    e-commerce example, the context is an :samp:`Order` that is configured to
    apply a promotional discount according to one of several algorithms.
Strategy
    is the common interface for the components that implement the various
    algorithms. In our example, this role is performed by an abstract class
    called :samp:`Discount`.
Concrete Strategy
    is one of the concrete subclasses of the abstract strategy.
    :samp:`LoyaltyDiscount`, :samp:`QuantityDiscount` and :samp:`BulkDiscount`
    are the three concrete strategies implemented.

.. literalinclude:: strategy.py
   :language: python
   :linenos:

Function-orientated strategy
----------------------------

Each concrete strategy in the previous example is a class with a single method,
:func:`discount`. In addition, the strategy instances have no state (no instance
attributes). In the following example, we do a refactoring, replacing the
concrete strategies with simple functions and removing the abstract
:class:`Promotion` class.

.. literalinclude:: promos.py
   :language: python
   :linenos:
   :lines: 1-57

Line 33:
    To calculate a discount, simply call the function :func:`self.promotion()`.
Line 40:
    Each strategy is a function, not a class.

The authors of the design pattern book suggest sharing it with the `flyweight
<https://en.wikipedia.org/wiki/Flyweight_pattern>`_ design pattern:

    Strategy objects are often good flyweights.

    A flyweight is a shared object that can be used in multiple contexts at the
    same time.

Sharing is recommended to reduce the cost of creating a new concrete strategy
object when the same strategy is used repeatedly in each new context – in our
example, each new order instance. Thus, to overcome a disadvantage of the
strategy pattern – its runtime cost – the authors recommend the use of another
pattern. In the meantime, the amount of code and the maintenance costs pile up.

.. tip::
   In a more difficult use case with complex concrete strategies that contain an
   internal state, all parts of the strategy and flyweight pattern can be
   combined. But often concrete strategies do not have an internal state; they
   only process data from the context. In this case, you should definitely use
   simple functions instead of coding one-method classes that implement a
   one-method interface declared in another class. A function is more
   lightweight than an instance of a user-defined class, and there is no need
   for the flyweight strategy since each strategy function is only created once
   by Python when the `module <../../modules/index>` is compiled. A simple
   function is also *a shared object that can be used in multiple contexts at
   the same time*.

It can be helpful that the built-in function :py:func:`globals` within a
function or method always refers to the module in which this function or method
is defined – and not to the module from which it is called.

In this way, :py:func:`globals` can be used to automatically find all
:samp:`{special}_promo` functions available in the module:

.. literalinclude:: promos.py
   :language: python
   :lines: 60
   :lineno-start: 60

This iterates over every name in the :doc:`dictionary <../../types/dicts>`
returned by :py:func:`globals()` and selects only those names that end with the
``_promo`` suffix.

To find the :samp:`{special}_promo` functions in another module, the
:doc:`inspect <python3:library/inspect>` library can be used:

.. literalinclude:: best_promo.py
   :language: python
   :linenos:

The :py:func:`inspect.getmembers` function returns the attributes of an object –
in this case the :mod:`promos`. We then use :py:func:`inspect.isfunction` to get
only the functions of the module. This example works regardless of the names of
the functions; the only important thing is that the :mod:`promos` module
contains the relevant functions.
