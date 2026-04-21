``dataclasses``
===============

:doc:`dataclasses <python3:library/dataclasses>` were introduced in Python 3.7
and are a special shortcut with which we can create classes that store data.
Python offers a special :doc:`decorator <../functions/decorators>` if we want to
create such a class.

.. tip::
   For table data I generally use :doc:`pandas Series or DataFrames
   <Python4DataScience:workspace/pandas/data-structures>` and if I need to store
   matrices with numbers I use :doc:`Numpy
   <Python4DataScience:workspace/numpy/index>`.

Let’s say we want to store a class that represents a task with ``summary``,
``owner``, ``state`` and ``id``. We can define such a class with:

.. code-block:: pycon

   >>> from dataclasses import dataclass
   >>> @dataclass
   ... class Task:
   ...     summary: str = None
   ...     owner: str = None
   ...     state: str = "todo"
   ...     id: int = None
   ...

The ``@dataclass`` decorator creates the ``__init__`` and ``__repr__`` methods.
If I display the instance of the class, I get the class name and the attributes:

.. code-block:: pycon

   >>> i1
   Task(summary='My first task', owner='veit', state='todo', id=1)

In general, data classes are used as syntactic sugar for creating classes that
store data. You can add extra functionality to your classes by defining methods.
We will add a method to the class that creates a Task object from a
:doc:`Dict <../types/dicts>`:

.. code-block:: pycon

   >>> @dataclass
   ... class Task:
   ...     ...
   ...     @classmethod
   ...     def from_dict(cls, d):
   ...         return Task(**d)
   ...
   >>> task_dict = {
   ...     "summary": "My first task",
   ...     "owner": "veit",
   ...     "state": "todo",
   ...     "id": 1,
   ... }
   >>> Task.from_dict(task_dict)
   Task(summary='My first task', owner='veit', state='todo', id=1)

.. tip::
   `cusy seminar: Advanced Python
   <https://cusy.io/en/our-training-courses/advanced-python.html>`_
