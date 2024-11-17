Command design pattern
======================

`Command <https://en.wikipedia.org/wiki/Command_pattern>`_ is another design
pattern that can be simplified by using functions that are passed as arguments:

.. uml::

    title UML class diagram for the command design pattern

    together {
        abstract class  Caller
        abstract class  Command {
            {method}    execute()
        }
    }

    together {
        abstract class  Client
        abstract class  Receiver {
            {method}    action()
        }
        class           ConcreteCommand {
            state
            {method}    execute()
        }
    }

    Caller *-> Command
    Client -> Receiver
    Client -> ConcreteCommand
    Receiver <- ConcreteCommand
    ConcreteCommand -u-|> Command

The aim of the command design pattern is to decouple an object that calls an
operation from the  :obj:`Receiver` object that implements the operation. In the
example from the `design pattern
<https://en.wikipedia.org/wiki/Design_Patterns>`_ book, each :obj:`Caller`
object is a menu item in a graphical application, and the :obj:`Receiver`
objects are the document to be edited or the application itself. For this
purpose, a :obj:`Command` object is placed between the two, which implements an
interface with a single method that calls a method in the :class:`Receiver` to
perform the desired operation. In this way, the :class:`Caller` object does not
need to know the interface of the :class:`Receiver`, and different Receivers can
be customised using different :class:`Command` subclasses. :class:`Caller` is
configured with a :class:`ConcreteCommand` command and calls its
:meth:`execute` method to execute it.

    Commands are an object-orientated replacement for callbacks. [#]_

The question now is whether we really need such an object-oriented replacement
for callbacks in Python? Can’t we just give the :obj:`Caller` a function
instead? So instead of calling :func:`Command.execute`, the caller could simply
call :func:`command`. :class:`Command` can be a class that implements
:func:`__call__` and instances of :class:`Command` would be *callables*, each
containing a list of functions for future calls, for example:

.. literalinclude:: caller.py
   :language: python
   :linenos:
   :emphasize-lines: 4-5, 7-8

Lines 4–5
    creates a list from the command arguments and ensures that it is iterable.
Line 7–8
    creates a local copy of the command references in each :class:`MacroCommand`
    instance. When an instance of :class:`MacroCommand` is called, each command
    in ``self.commands`` is called in turn.

----

.. [#] `Design Patterns <https://en.wikipedia.org/wiki/Design_Patterns>`_
