``dataclasses``
===============

:doc:`dataclasses <python3:library/dataclasses>` were introduced in Python 3.7
and are a special shortcut with which we can create classes that store data.
Python offers a special :doc:`decorator <functions/decorators>` if we want to
create such a class.

.. note::
   For table data I generally use :doc:`pandas Series or DataFrames
   <Python4DataScience:workspace/pandas/data-structures>` and if I need to store
   matrices with numbers I use :doc:`Numpy
   <Python4DataScience:workspace/numpy/index>`.

Let’s say we want to store a class that represents an item with ``summary``,
``owner``, ``state`` and ``id``. We can define such a class with:

.. code-block:: pycon

   >>> from dataclasses import dataclass
   >>> @dataclass
   ... class Item:
   ...     summary: str = None
   ...     owner: str = None
   ...     state: str = "todo"
   ...     id: int = None
   ...

The ``@dataclass`` decorator creates the ``__init__`` and ``__repr__`` methods.
If I display the instance of the class, I get the class name and the attributes:

.. code-block:: pycon

   >>> i1
   Item(summary='My first item', owner='veit', state='todo', id=1)

In general, data classes are used as syntactic sugar for creating classes that
store data. You can add extra functionality to your classes by defining methods.
We will add a method to the class that creates an Item object from a
:doc:`Dict <types/dicts>`:

.. code-block:: pycon

   >>> @dataclass
   ... class Item:
   ...     ...
   ...     @classmethod
   ...     def from_dict(cls, d):
   ...         return Item(**d)
   ...
   >>> item_dict = {
   ...     "summary": "My first item",
   ...     "owner": "veit",
   ...     "state": "todo",
   ...     "id": 1,
   ... }
   >>> Item.from_dict(item_dict)
   Item(summary='My first item', owner='veit', state='todo', id=1)
