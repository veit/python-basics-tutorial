Legacy software
===============

There may be various reasons for wanting to modify existing software:

* to add a feature
* to fix a bug
* to improve the software architecture (→ :ref:`refactoring`)
* to improve resource usage

If an existing codebase lacks significant test coverage, existing code is often
modified and then checked to see whether the desired feature is working or the
bug has been fixed. One might also check whether the change has broken other
features; nevertheless, it remains uncertain whether all the implications of the
code change have been taken into account.

In :doc:`test-driven development <tdd>` for legacy software, tests are first
written for the code to be modified and for all code that depends on it. With
such :term:`regression tests <regression test>`, we can identify changes and
determine whether the software still functions exactly as it did in the past.
This ensures that only the intended changes are made. However, regression tests
are usually carried out at the application interface, which means they present a
number of problems:

Error localisation
    The further tests stray from what you are actually supposed to be testing,
    the more difficult it becomes to identify the root cause of the error.
Execution time
    Larger tests also take longer to run. This means that test runs can take a
    frustratingly long time. Tests that take too long to run are usually carried
    out much less frequently.

Unit tests make it easier to localise errors and reduce execution time. Unlike

* sections of code can be tested independently of one another
* tests can be grouped so that, under certain conditions, only some are executed
  whilst others are run under different conditions.
* they help us pinpoint errors quickly.

So why don’t we simply write unit tests? Often, dependency issues prevent this.
When objects depend directly on something that is difficult to use in a test,
these dependencies are also difficult to change and manage. Often, a large part
of the work on legacy code involves breaking down such dependencies so that
changes can be made more easily. Consequently, we are often unable to set up
unit tests without first modifying the code. Unit tests are therefore not very
practical in such cases.

By resolving dependencies, we can write tests that make more far-reaching
changes safer. However, such initial refactorings should be carried out very
conservatively, so that the risk of introducing errors remains low. If we do
this, the code in that area may end up looking slightly less elegant.

    *“They are like the incision points in surgery: There might be a scar left
    in your code after your work, but everything beneath it can get better.”*

– `Working Effectively with Legacy Code
<https://www.pearson.de/working-effectively-with-legacy-code-9780131177055>`_ by
Michael C. Feathers

The aim with legacy code is to make functional changes that add value whilst, at
the same time, incorporating a larger part of the system into the tests. At the
end of each development cycle, we should be able to point not only to code that
provides a new function, but also to the associated tests. In future, working on
code that has already been tested will become much easier. You can follow these
steps when you need to make changes to legacy code:

#. **Identify the section of code to be modified.** Where changes need to be
   made depends heavily on the architecture.
#. :ref:`find-test-opportunities`: In some cases, it is easy to find suitable
   places to write tests, but with legacy code this can often be difficult.
#. :ref:`resolve-dependencies`: Dependencies are often the most obvious obstacle
   to testing, as they cause difficulties in test environments when
   instantiating objects or executing methods. With legacy code, dependencies
   often need to be decoupled in order to set up tests. Ideally, we would have
   tests to show us whether the measures we take to decouple dependencies have
   themselves caused problems – but this is often not the case.
#. :ref:`write-tests`: Tests for legacy code may differ slightly from those for
   new code.
#. :ref:`refactoring`: Once we have made changes to the legacy code, we are
   often more familiar with its issues, and the tests we wrote to add
   functionality often provide us with a degree of assurance that allows us to
   carry out refactoring. This often means that the code has become a little
   easier to maintain than before. But do not underestimate this work: simple
   measures – such as splitting up a large class – can make a significant
   difference in applications, even if they seem somewhat mechanical.

.. _find-test-opportunities:

Finding testing opportunities
-----------------------------

Sprout
~~~~~~

You can use Sprout when you need to add a function or class to a system and it
can be completely rewritten. Write the code at the point where the new
functionality is required. You may not be able to test the call sites straight
away, but at least you can write tests for your new code.

Essentially, however, this means we are giving up on improving and testing the
original function or class. We’re simply adding new features. Nevertheless, this
is sometimes the most practical approach, even if it leaves the code in a sort
of limbo: it’s not really clear why this particular function or class is located
elsewhere. On the other hand, the new code is clearly separated from the old:
your changes can be viewed in isolation and have a clean interface with the old
code.

Wrap
~~~~

For wrap, a function is created with the same name as the original function, and
this then points to our original code. Using this approach, we can add new
behaviour or a new call to the original function. This ensures that all
responsibilities appear to be clearly separated from one another. Here are the
steps for this wrap method:

#. Identify the method you need to change
#. If the change can be expressed as a single sequence of instructions in one
   place, rename the function and then create a new function with the same name
   and signature as the old method. Make sure to retain the signatures.
#. Insert a call to the old function within the new function.
#. Develop a new function and test it first.

One potential drawback is that the new function must not be intertwined with the
logic of the old function. It must be something that is executed either before
or after the old function. In reality, this isn’t really a drawback at all. A
serious drawback, however, is that a new name must be found for the old code.

Another form of the wrap method, which we can use when we simply want to add a
new function, does not have this problem. The steps are then as follows:

#. Identify a function that you need to change
#. If the change can be expressed as a single sequence of statements in one
   place, develop a new function for this using test-driven development
#. Create another function that calls both the new and the old functions.

Wrap has the advantage over Sprout in that it does not increase the existing
scope. Furthermore, the new functionality is independent of the existing
functionality, and code intended for one purpose is not intertwined with code
intended for another.

When we apply Wrap to classes, this is known as the *Decorator pattern*. We
create objects of a class that wraps another class and pass these on. The
wrapping class should have the same interface as the wrapped class, so that
clients do not realise they are working with a wrapper. The Decorator pattern
allows complex behaviours to be built up at runtime through the composition of
objects.

.. admonition:: Decorator Pattern
   :collapsible: closed

   Decorator is a structural pattern that provides a flexible alternative to
   subclassing for extending a class with additional functionality. It should
   not be confused with Python :doc:`decorators <../../functions/decorators>`.

   You can find an example of the `Decorator Pattern
   <https://wiki.python.org/moin/DecoratorPattern>`_ on the Python Wiki. It
   shows us how decorators are incorporated into the pipeline to dynamically
   inject various behaviours into an object.

Although the Decorator pattern is useful, it should be used sparingly:

    *“Navigating through code that contains decorators that decorate other
    decorators is a lot like peeling away the layers of an onion. It is
    necessary work, but it does make your eyes water.”*

– `Working Effectively with Legacy Code
<https://www.pearson.de/working-effectively-with-legacy-code-9780131177055>`_
by Michael C. Feathers

If the new behaviour only needs to be applied in a few places, it may therefore
be useful to create a wrapper that does not follow the Decorator pattern. Over
time, you should keep an eye on the wrapper’s responsibilities and consider
whether it could evolve into a broader concept within your system. Here are the
steps for the wrap class:

#. Identify a method where you need to make the change.
#. If the change can be expressed as a single sequence of statements in one
   place, create a class that accepts the class to be wrapped as a constructor
   argument. If you find it difficult to create a class that wraps the original
   class, you may need to extract functions or interfaces from the wrapped class
   so that you can instantiate your wrapper.
#. Using test-driven development, create a method within this class that
   performs the new task. Write another method that calls both the new method
   and the old method of the wrapped class.
#. Instance the wrapper class in your code at the point where you wish to
   activate the new behaviour.

.. _resolve-dependencies:

Resolving dependencies
----------------------

Systems that are broken down into small, clearly named and understandable parts
allow you to work more quickly. Many dependencies are problematic, but
fortunately they can be resolved. With object-oriented code, the first step is
often to instantiate the required classes in a :term:`test fixture <test
fixture>`.

If you have a class instance that needs to be modified in a test, this is
generally very quick. However, if this requires access to external resources
such as a database, hardware or communications infrastructure, it quickly
becomes time-consuming. In such cases, it is worth checking everything that
depends on what you want to instantiate. You should then define interfaces and
move the dependencies into new modules.

.. admonition:: Dependency Inversion Principle
   :collapsible: closed

   The `Dependency Inversion Principle
   <https://en.wikipedia.org/wiki/Dependency_inversion_principle>`_ states that
   your code’s dependencies are much lower when it depends on an interface.
   Interfaces generally change far less frequently than the underlying code. You
   can then modify classes or implement the interface without having to change
   the underlying code. For this reason, it is better to rely on interfaces or
   abstract classes rather than concrete classes. By relying on things that
   change less frequently, you minimise the likelihood that certain changes will
   trigger extensive reworking.

We can decouple dependencies and distribute classes across different modules so
that we can run our tests quickly and receive feedback, thereby reducing the
error rate. However, this comes at a price: more interfaces and modules entail
conceptual overhead. Ultimately, you end up with sections of code that are
easier to work with. It may be a little more laborious to test a small group of
classes separately, but it is important to remember that they do not need to be
tested when another group of classes is being tested.

Programming by Difference
~~~~~~~~~~~~~~~~~~~~~~~~~

In object-oriented programming, we can use inheritance to introduce
functionality without having to modify a class directly. Once we have added the
functionality, we can work out exactly how we want to integrate it. This
*programming by difference* is useful for making changes quickly. However,
certain pitfalls, such as breaching the :doc:`solid`, should be avoided.

.. _write-tests:

Writing tests
-------------

It’s not always easy to instantiate a class in a test fixture. Here are the four
most common problems we encounter:

* Objects of the class cannot be created easily.
* The test fixture cannot be built easily using the class.
* The constructor we need to use has undesirable side effects.
* Extensive calculations are carried out in the constructor, and we need to
  capture these.

There is a whole arsenal of techniques for tackling these problems:

Interfering configurations, environment variables, paths and parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To check whether these details are actually being used, we can simply pass
:doc:`../../types/none` where appropriate. The worst that can happen is that
part of the code attempts to use this parameter and throws an :doc:`exception
<../../control-flow/exceptions>`. Alternatively, the method that handles this
can be overridden using :ref:`monkeypatch
</test/libs/pytest/builtin-fixtures.rst#monkeypatch>`. However, we must ensure
that we do not alter the behaviour we are trying to test.

Hidden resources
~~~~~~~~~~~~~~~~

Often, a hidden resource – such as an SMTP server – is used, which we cannot
easily access in our test fixture. *Parameterize constructor* externalises such
a resource and then passes it as a parameter.

.. _refactoring:

Refactoring
-----------

We will illustrate what refactoring might look like using two different
examples:

* **Library dependencies:** A library that solves a specific problem for us
  often saves us a great deal of time on a project. However, they should not be
  used indiscriminately throughout the code, as otherwise switching libraries
  could be tantamount to rewriting the entire programme.

* **Refactoring API calls:** Essentially, there are two approaches to
  refactoring API calls:

  * With *Skin and Wrap* of the API, we create interfaces that mirror the API as
    closely as possible, and then we create wrappers around the library’s
    functions. Ultimately, we have no dependencies on the underlying API code,
    and the wrappers can delegate to the real API in production code, whilst we
    use :term:`fakes <Fake>` during testing.

    *Skin and Wrap* is well suited when

    * the API is relatively small
    * you wish to completely decouple your dependencies from a third-party
      library
    * you have no tests and are unable to write any, as you cannot test the API.
      We then have the option to test our entire code – with the exception of a
      thin delegation layer from the wrapper to the actual API classes.

  * With *Responsibility-Based Extraction*, we identify responsibilities in the

    *Responsibility-Based Extraction* is more suitable if

    * the API is more complex
    * you already have a tool with extraction methods
