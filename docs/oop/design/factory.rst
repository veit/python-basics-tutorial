Abstract Factory
================

.. warning::
   The Abstract Factory is an awkward workaround for the lack of first-class
   functions and classes in less powerful programming languages. It is a poor
   fit for Python, where we can instead simply pass a class or a factory
   function when a library needs to create objects on our behalf.

   – Brandon Rhodes: `The Abstract Factory Pattern
   <https://python-patterns.guide/gang-of-four/abstract-factory/>`_

The :mod:`python3:json` module of the Python standard library is a good example
of a library that needs to instantiate objects on behalf of its caller. Let’s
look at a JSON string like this:

.. literalinclude:: books.json
   :language: json

Normally, the :func:`python3:json.load` function of the :mod:`python3:json`
module generates Unicode objects for the strings and a Dict for the top-level
JSON object.

However, this default value is not satisfactory for the publication date, so we
want to convert it into a date format:

.. code-block:: pycon
   :emphasize-lines: 2-4, 8, 11

    >>> import json
    >>> from datetime import datetime
    >>> def convert_date(string):
    ...     return datetime.strptime(string, "%Y-%m-%d").date()
    ...
    >>> with open("books.json") as f:
    ...     books = json.load(f)
    ...     books["Publication date"] = convert_date(books["Publication date"])
    ...     print(books)
    ...
    {'Title': 'Python basics', 'Language': 'en', 'Authors': 'Veit Schiele', 'License': 'BSD-3-Clause', 'Publication date': datetime.date(2021, 10, 28)}

This simple factory was successfully executed: the date returned is of type
``datetime.date``.

.. note::
   I chose the verb :func:`convert_date()` as the name for this function, rather
   than a noun like :func:`date_factory()`, because it expresses what the
   function does, rather than telling me what kind of function it is.

Some legacy languages only support passing class instances, not callable
functions. With this restriction, any simple factory would have to go from a
function to a method:

.. code-block:: python

   class DateFactory(object):
       @staticmethod
       def build_date(dict):
           dict["Publication date"] = datetime.strptime(
               dict["Publication date"], "%Y-%m-%d"
           ).date()

In traditional object-oriented programming, the word factory is the name for a
type of class that provides a method to create an object. If we could not pass a
Python class directly, but only object instances, the :class:`DateFactory` class
could not be passed as an argument to the :func:`load` method. Instead,
:class:`DateFactory` would have to be instantiated unnecessarily and then the
resulting object would have to be passed:

.. code-block:: python
   :emphasize-lines: 6

   class Loader(object):
       @staticmethod
       def load(books_file, factory):
           with open(books_file) as f:
               books = json.load(f)
               factory.build_date(books)
               return books

.. code-block:: pycon

   >>> df = DateFactory()
   >>> b = Loader.load("books.json", df)
   >>> print(b)
   {'Title': 'Python basics', 'Language': 'en', 'Authors': 'Veit Schiele', 'License': 'BSD-3-Clause', 'Publication date': datetime.date(2021, 10, 28)}

.. note::
   #. Since Python classes provide static and class methods that can be called
      without an instance, we don’t need to instantiate the :class:`DateFactory`
      class first – we can simply pass it as an object.
   #. Languages that force you to declare the type of each method parameter in
      advance limit your future possibilities excessively.

Finally, the *Abstract Factory* design pattern aims to separate the
specification from the implementation by creating an abstract class. Your
abstract class would simply promise that the :class:`DateFactory` argument for
:func:`load()` will be a class that matches the required interface:

.. code-block:: python

   from abc import ABCMeta, abstractmethod


   class AbstractFactory(metaclass=ABCMeta):

       @abstractmethod
       def build_date(self, dict):
           pass

However, once the abstract class is present and :class:`DateFactory` inherits
from it, the operations that take place at runtime are exactly the same as
before. The :class:`DateFactory` methods are called with different arguments
that instruct them to create different types of objects without the caller
needing to know the details.
