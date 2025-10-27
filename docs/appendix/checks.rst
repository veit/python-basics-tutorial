Checks
======

:doc:`/variables-expressions`
-----------------------------

* Create some variables in the Python shell. What happens if you add spaces,
  hyphens or other characters to the variable names?

  .. blacken-docs:off

  .. code-block:: pycon

     >>> x = 3
     >>> var fünf = 5
       File "<stdin>", line 1
         var fünf = 5
             ^^^^
     SyntaxError: invalid syntax
     >>> var_fünf = 5

  .. blacken-docs:on

* Do the results change if you use brackets to group numbers in different ways?

  .. code-block:: pycon

     >>> 2 + 3 * 4 - 5 / 6
     13.166666666666666
     >>> (2 + 3) * 4 - 5 / 6
     19.166666666666668
     >>> 2 + (3 * 4) - 5 / 6
     13.166666666666666
     >>> 2 + 3 * (4 - 5) / 6
     1.5

* Which of the following variable and function names do you think are not good
  Python style, and why?

  ``var*``
      ❌ contains an invalid character (``*``)
  ``varname``
      ✅ ok, but easier to read with underscore
  ``func_name()``
      ✅
  ``varName``
      ❌ Mixed upper and lower case letters
  ``VARNAME``
      ❌ Capital letters only, difficult to read
  ``very_very_long_var_name``
      ✅ ok, but very long and therefore only recommended if you want to differentiate between many very similar variables

:doc:`/types/numbers/index`
---------------------------

* Create some number variables (integers, floating point numbers and complex
  numbers). Experiment a little with what happens when you perform operations
  with them, even across types.

  .. blacken-docs:off

  .. code-block:: pycon

     >>> x = 3
     >>> import math
     >>> pi = math.pi
     >>> pi
     3.141592653589793
     >>> c = 3j4
       File "<stdin>", line 1
         c = 3j4
              ^
     SyntaxError: invalid imaginary literal
     >>> c = 3 +4j
     >>> c
     (3+4j)
     >>> x * c
     (9+12j)
     >>> x + c
     (6+4j)

  .. blacken-docs:on

:doc:`/types/numbers/complex`
-----------------------------

* Load the :mod:`math` module and try out some of the functions. Then load the
  :mod:`cmath` module and do the same.

  .. code-block:: pycon

     >>> from math import sqrt
     >>> sqrt(3)
     1.7320508075688772
     >>> from cmath import sqrt
     >>> sqrt(3)
     (1.7320508075688772+0j)

* How can you restore the functions of the :mod:`math` module?

  .. code-block:: pycon

     >>> from math import sqrt
     >>> sqrt(3)
     1.7320508075688772

:doc:`/types/numbers/bool`
--------------------------

* Decide whether the following statements are true or false:

  * ``1`` → True
  * ``0`` → False
  * ``-1`` → True
  * ``[0]`` → True (List with one item)
  * ``1 and 0`` → False
  * ``1 > 0 or []`` → True

:doc:`/types/sequences-sets/lists`
----------------------------------

* What does :func:`len` return for each of the following cases:

  .. code-block:: pycon

     >>> len([3])
     1
     >>> len([])
     0
     >>> len([[1, [2, 3], 4], "5 6"])
     2

* How would you use :func:`len` and slices to determine the second half of a
  list if you don’t know how long it is?

  .. code-block:: pycon

     >>> l = [[1, [2, 3], 4], "5 6"]
     >>> l[len(l) // 2 :]
     ['5 6']

* How could you move the last two entries of a list to the beginning without
  changing the order of the two?

  .. code-block:: pycon

     >>> l[-2:] + l[:2]
     ['5 6', 7, [1, [2, 3], 4], '5 6']

* Which of the following cases triggers an exception?

  * ``min(["1", "2", "3"])``
  * ``max([1, 2, "3"])``
  * ``[1,2,3].count("1")``

  ``max([1, 2, "3"])``, as strings and integers cannot be compared; it is
  therefore impossible to obtain a maximum value.

* If you have a list ``l``, how can you remove a certain value ``i`` from it?

  .. code-block:: pycon

     >>> if i in l:
     ...     l.remove(i)
     ...

  .. note::
     This code only removes the first occurrence of ``i``. To remove all
     occurrences of ``i`` from the list, the list could be converted to the
     :doc:`set </types/sequences-sets/sets>` type, for example:

     .. code-block:: pycon

        >>> l = set(l)
        >>> if i in l:
        ...     l.remove(i)
        ...
        >>> l = list(l)

* If you have a nested list ``ll``, how can you get a copy ``nll`` of this list
  in which you can change the elements without changing the contents of ``ll``?

  .. code-block:: pycon

      >>> import copy
      >>> nll = copy.deepcopy(ll)

* Make sure that the object ``my_collection`` is a list before you try to append
  data to it.

  .. code-block:: pycon

     >>> my_collection = []
     >>> if isinstance(my_collection, list):
     ...     print(f"my_collection is a list")
     ...
     my_collection is a list

* What other options could you have besides explicitly checking the type?

:doc:`/types/sequences-sets/tuples`
-----------------------------------

* Explain why the following operations cannot be applied to the tuple ``t``:

  * ``t.append(1)``
  * ``t[2] = 2``
  * ``del t[3]``

  All operations attempt to change the tuple ``t``. However, tuples cannot be
  changed.

* How can you sort the elements of a tuple?

  .. code-block:: pycon

     >>> sorted(t)

:doc:`/types/sequences-sets/sets`
---------------------------------

* How many elements does a set have if it is formed from the following list
  ``[4, 2, 3, 2, 1]``?

  Four different elements.

:doc:`/types/dicts`
-------------------

* Suppose you have the two dictionaries ``x = {"a":1, "b":2, "c":3, "d":4}`` and
  ``y = {"a":5, "e":6, "f":7}``. What would be the content of ``x`` after the
  following code snippets have been executed?

  .. code-block:: pycon

     >>> del x["b"]
     >>> z = x.setdefault("e", 8)
     >>> x.update(y)

  .. code-block:: pycon

     >>> x = {"a": 1, "b": 2, "c": 3, "d": 4}
     >>> y = {"a": 5, "e": 6, "f": 7}
     >>> del x["b"]
     >>> z = x.setdefault("e", 8)
     >>> x.update(y)
     >>> x
     {'a': 5, 'c': 3, 'd': 4, 'e': 6, 'f': 7}

* Which of the following expressions can be a key of a dictionary:  ``1``;
  ``"Veit"``; ``("Veit", [1])``; ``[("Veit", [1])]``; ``["Veit"]``; ``("Veit",
  "Tim", "Monique")``

  .. code-block:: pycon

     >>> d = {}
     >>> d[1] = None
     >>> d["Veit"] = None
     >>> d[("Veit", [1])]
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     TypeError: unhashable type: 'list'
     >>> d[["Veit"]] = None
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     TypeError: unhashable type: 'list'
     >>> d[("Veit", "Tim", "Monique")] = None

* You can use a :doc:`Dictionary </types/dicts>` like a spreadsheet table by
  using :doc:`/types/sequences-sets/tuples` as key row and column values. Write
  sample code to add and retrieve values.

  .. code-block:: pycon

     >>> tabular = {}
     >>> tabular[("A", 0)] = 1
     >>> tabular[("A", 1)] = 2
     >>> tabular[("B", 0)] = 3
     >>> tabular[("B", 1)] = 4
     >>> print(tabular[("A", 1)])
     2

* How can you remove all duplicates from a list without changing the order of the
  elements in the list?

  The keys of a :doc:`/types/dicts` can be used for this:

  .. code-block:: pycon

     >>> list(dict.fromkeys(l))

:doc:`/types/strings/index`
---------------------------

* For example, can you add or multiply a string with an integer, a floating
  point number or a complex number?

  .. code-block:: pycon

     >>> x = 3
     >>> c = 3 + 4j
     >>> snake = "🐍"
     >>> x + snake
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     TypeError: unsupported operand type(s) for +: 'int' and 'str'
     >>> x * snake
     '🐍🐍🐍'
     >>> c + snake
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     TypeError: unsupported operand type(s) for +: 'complex' and 'str'
     >>> c * snake
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     TypeError: can't multiply sequence by non-int of type 'complex'

:doc:`/types/strings/operators-functions`
-----------------------------------------

* Which of the following strings cannot be converted into numbers and why?

  .. blacken-docs:off

  .. code-block:: pycon

     >>> int("1e2")
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     ValueError: invalid literal for int() with base 10: '1e2'
     >>> int(1e+2)
     100
     >>> int("1+2")
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     ValueError: invalid literal for int() with base 10: '1+2'
     >>> int("+2")
     2

  .. blacken-docs:on

* How can you change a heading such as ``variables and expressions`` so that it
  contains hyphens instead of spaces and can therefore be better used as a file
  name?

  .. code-block:: pycon

     >>> ve = "variables and expressions"
     >>> "-".join(ve.split())
     'variables-and-expressions'

* If you want to check whether a line begins with ``.. note::``, which method
  would you use? Are there any other options?

  .. code-block:: pycon

     >>> x.startswith(".. note::")
     True
     >>> x[:9] == ".. note::"
     True

* Suppose you have a string with exclamation marks, quotation marks and line
  breaks. How can these be removed from the string?

  .. code-block:: pycon

     >>> hipy = "„Hello Pythonistas!“\n"
     >>> hipy.strip("„“!\n")
     'Hello Pythonistas'

* How can you change all spaces and punctuation marks from a string to a hyphen
  (``-``)?

  .. code-block:: pycon

     >>> from string import punctuation, whitespace
     >>> chars = punctuation + whitespace
     >>> subs = str.maketrans(chars, len(chars) * "-")
     >>> hipy = "Hello Pythonistas!\n"
     >>> hipy.translate(subs)
     'Hello-Pythonistas--'

:doc:`/types/strings/built-in-modules/re`
-----------------------------------------

* Which regular expression would you use to find strings that represent the
  numbers between -3 and +3?

  ``r"-?[0-3]"`` or ``r"-{0,1}[0-3]"``

  ``?``
      is a quantifier for one or no occurrence.

* Which regular expression would you use to find hexadecimal values?

  ``r"0[xX][0-9a-fA-F]+"``
      corresponds to an expression starting with ``0``, followed by a lower or
      upper case ``x``, followed by one or more characters in the ranges
      ``0-9``, ``a-f`` or ``A-F``.

:doc:`/types/strings/input`
---------------------------

* How can you get string and integer values with the :func:`input` function?

  .. code-block:: pycon

     >>> year_birth = input("Geburtsjahr: ")
     Geburtsjahr: 1964
     >>> type(year_birth)
     <class 'str'>
     >>> year_birth = int(input("Geburtsjahr: "))
     Geburtsjahr: 1964
     >>> type(year_birth)
     <class 'int'>

* What is the effect if you do not use :func:`int` to call :func:`input` for
  integer inputs?

  .. code-block:: pycon

     >>> import datetime
     >>> current = datetime.datetime.now()
     >>> year = current.year
     >>> year_birth = input("Geburtsjahr? ")
     Geburtsjahr? 1964
     >>> age = year - year_birth
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     TypeError: unsupported operand type(s) for -: 'int' and 'str'

* Can you change the code so that it accepts a floating point number?

  .. code-block:: pycon

     >>> import datetime
     >>> current = datetime.datetime.now()
     >>> year = current.year
     >>> year_birth = float(input("Geburtsjahr: "))
     Geburtsjahr: 1964
     >>> type(year_birth)
     <class 'float'>

* What happens if you enter an incorrect value type?

  .. code-block:: pycon

     >>> import datetime
     >>> current = datetime.datetime.now()
     >>> year = current.year
     >>> year_birth = int(input("Geburtsjahr: "))
     Geburtsjahr: Schaltjahr
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     ValueError: invalid literal for int() with base 10: 'Schaltjahr'

* Write the code to ask for the names and ages of three users. After the values
  have been entered, ask for one of the names and output the corresponding age.

  .. code-block:: pycon

     >>> personal_data = {}
     >>> for i in range(3):
     ...     name = input("Name? ")
     ...     age = int(input("Age? "))
     ...     personal_data[name] = age
     ...
     Name? Veit
     Age? 60
     Name? Tim
     Age? 35
     Name? Monique
     Age? 37
     >>> who = input("Who? ")
     Who? Veit
     >>> print(personal_data[who])
     60

:doc:`/control-flow/loops`
--------------------------

* Removes all negative numbers from the list ``x = [ -2, -1, 0, 1, 2, 3]``.

  .. code-block:: pycon

     >>> x = [-2, -1, 0, 1, 2, 3]
     >>> pos = []
     >>> for i in x:
     ...     if i >= 0:
     ...         pos.append(i)
     ...
     >>> pos
     [0, 1, 2, 3]

* Which list comprehension would you use to achieve the same result?

  .. code-block:: pycon

     >>> x = [-2, -1, 0, 1, 2, 3]
     >>> pos = [i for i in x if i >= 0]
     >>> pos
     [0, 1, 2, 3]

* How would you count the total number of negative numbers in the list ``[[-1,
  0, 1], [-1, 1, 3], [-2, 0, 2]]``?

  .. code-block:: pycon

     >>> x = [[-1, 0, 1], [-1, 1, 3], [-2, 0, 2]]
     >>> neg = 0
     >>> for row in x:
     ...     for col in row:
     ...         if col < 0:
     ...             neg += 1
     ...
     >>> neg
     3

* Creates a generator that only returns odd numbers from 1 to 10.

  .. tip::
     A number is odd if there is a remainder when it is divided by 2, in other
     words if ``% 2`` is true.

  .. code-block:: pycon

     >>> x = (x for x in range(10) if x % 2)
     >>> for i in x:
     ...     print(i)
     ...
     1
     3
     5
     7
     9

* Write a :doc:`dict </types/dicts>` with the edge lengths and volumes of cubes.

  .. code-block:: pycon

     >>> {x: x**3 for x in range(1, 5)}
     {1: 1, 2: 8, 3: 27, 4: 64}

:doc:`/control-flow/exceptions`
-------------------------------

* Write code that receives two numbers and divides the first number by the
  second. Check if the :class:`python3:ZeroDivisionError` occurs when the second
  number is ``0`` and catch it.

  .. code-block:: pycon

     >>> x = int(input("Please enter an integer: "))
     Please enter an integer: 7
     >>> y = int(input("Please enter an integer: "))
     Please enter an integer: 6
     >>> try:
     ...     z = x / y
     ... except ZeroDivisionError as e:
     ...     print("It cannot be divided by 0!")
     ...
     >>> z
     1.1666666666666667
     >>> y = int(input("Please enter an integer: "))
     Please enter an integer: 0
     >>> try:
     ...     print("It cannot be divided by 0!")
     ... except ZeroDivisionError as e:
     ...     print("It cannot be divided by 0!")
     ...
     It cannot be divided by 0!

* If :class:`MyError` inherits from :class:`Exception`, what is the difference
  between ``except Exception as e`` and ``except MyError as e``?

  The first catches every exception that inherits from :class:`Exception`, while
  the second only catches :class:`MyError` exceptions.

* Write a simple program that receives a number and then uses the :func:`assert`
  statement to throw an :class:`python3:Exception` if the number is ``0``.

  .. code-block:: pycon

     >>> x = int(input("Please enter an integer that is not zero: "))
     Please enter an integer that is not zero: 0
     >>> assert x != 0, "The integer must not be zero."
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     AssertionError: The integer must not be zero.

* Write a user-defined exception :class:`outliers` that throws an
  :class:`Exception` if the variable ``x`` is greater or less than ``3``?

  .. code-block:: pycon

     >>> class Outliers(Exception):
     ...     pass
     ...
     >>> x = -4
     >>> if abs(x) > 3:
     ...     raise Outliers(f"The value {x} is an outlier")
     ...
     Traceback (most recent call last):
       File "<stdin>", line 2, in <module>
     Outliers: The value -4 is an outlier

* Is checking whether an object is a list (:ref:`Check: Listen <check-list>`)
  programming in the style of :abbr:`LBYL (look before you leap)` or
  :abbr:`EAFP (easier to ask forgiveness than permission)`?

  This is :abbr:`LBYL (look before you leap)` programming. Only when you add
  :func:`append` to a ``try... except`` block and catch :class:`TypeError`
  exceptions does it become a bit more :abbr:`EAFP (easier to ask forgiveness
  than permission)`.

:doc:`/functions/params`
------------------------

* Write a function that can take any number of unnamed arguments and output
  their values in reverse order?

  .. code-block:: pycon

     >>> values = input("Values separated by commas: ")
     Values separated by commas: 1,3,2,4
     >>> value_list = values.split(",")
     >>> reverse(value_list)
     ['4', '3', '2', '1']

:doc:`/functions/variables`
---------------------------

* Assuming ``x = 1``, :func:`func` sets the local variable ``x`` to ``2`` and
  :func:`gfunc` sets the global variable ``x`` to ``3``, what value does ``x``
  assume after :func:`func` and :func:`gfunc` have been run through?

  .. code-block:: pycon

     >>> x = 1
     >>> def func():
     ...     x = 2
     ...
     >>> def gfunc():
     ...     global x
     ...     x = 3
     ...
     >>> func()
     >>> x
     1
     >>> gfunc()
     >>> x
     3

:doc:`/modules/index`
---------------------

* If you have created a :mod:`my_math` module that contains a :func:`divide`
  function, what options are there for importing this function and then using
  it? What are the advantages and disadvantages of each option?

  .. code-block:: pycon

     >>> import my_math
     >>> my_math.divide(..., ...)

  .. code-block:: pycon

     >>> from my_math import divide
     >>> divide(..., ...)

  The first solution is often favoured as there will be no conflict between the
  identifiers in :mod:`my_math` and the importing namespace. However, this
  solution is a little more complex.

* A variable ``min`` is contained in the :mod:`scope.py` module. In which of the
  following contexts can ``min`` be used?

  #. With the module itself
  #. Within the :func:`scope` function of the module
  #. Within a script that has imported the :mod:`scope.py` module

  1. and 2. but not 3.

* Pack the functions that you created at the end of :doc:`/functions/decorators`
  as an independent module. The functions should initially only be fully usable
  from another script.

  .. literalinclude:: example_mod.py
     :caption: example_mod.py
     :name: example_mod.py
     :language: python

  .. literalinclude:: my_script.py
     :caption: my_script.py
     :name: my_script.py
     :language: python

* Make your module executable.

  .. literalinclude:: example_mod2.py
     :diff: example_mod.py
     :language: python

.. _wcargv_stdin:

* Rewrite your version of the :mod:`wc` utility so that it implements both the
  distinction between bytes and characters and the ability to read from files
  and from standard input.

  .. literalinclude:: /modules/wcargv_stdin.py
     :diff: /modules/wcargv.py

:doc:`/oop/classes`
-------------------

* Write a :class:`Triangle` class that can also calculate the area.

  .. code-block:: python

     class Triangle:
         def __init__(self, width, height):
             self.width = width
             self.height = height

         def area(self):
             return 0.5 * self.width * self.height

:doc:`/oop/methods`
-------------------

* Write a class method that is similar to :func:`circumferences`, but returns
  the total area of all circles.

  .. code-block:: python

     def area(self):
         return self.diameter**2 / 4 * self.__class__.pi


     @classmethod
     def areas(cls):
         """Class method to sum all areas."""
         careasum = 0
         for c in cls.circles:
             careasum = careasum + c.area()
         return careasum

:doc:`/oop/inheritance`
-----------------------

* Rewrites the code for a :class:`Triangle` class so that it inherits from
  :class:`Form`.

  .. code-block:: pycon

     >>> class Form:
     ...     def __init__(self, x=0, y=0):
     ...         self.x = x
     ...         self.y = y
     ...
     >>> class Triangle(Form):
     ...     def __init__(self, width=1, height=1, x=0, y=0):
     ...         super().__init__(x, y)
     ...         self.length = length
     ...         self.height = height
     ...

* How would you write the code to add an :func:`area` method for the
  :class:`Triangle` class? Should the :func:`area` method be moved to the
  :class:`Form` base class and inherited by :class:`Circle`, :class:`Square` and
  :class:`Triangle`? What problems would this change cause?

  It makes sense to put the :func:`area` method in a :class:`Triangle` class;
  but putting it in :class:`Form` would not be very helpful because different
  types of :class:`Form` have their own area calculations. Any derived
  :class:`Form` would override the base :func:`area` method anyway.

:doc:`/oop/types`
-----------------

* What would be the difference between using :func:`type` and :func:`isinstance`
  in :ref:`Check: Lists <check-list>`?

  With :func:`type` you would only get lists, but not instances of lists.

:doc:`/oop/private`
-------------------

* Modify the code of the :class:`Triangle` class to make the dimension variables
  private. What restriction will this change impose on the use of the class?

  .. code-block:: pycon

     >>> class Triangle:
     ...     def __init__(self, x, y):
     ...         self.__x = x
     ...         self.__y = y
     ...

  The dimension variables are no longer available outside the class via ``.x``
  and ``.y``.

* Update the dimensions of the :class:`Triangle` class so that they are
  properties with getters and setters that do not allow negative values.

  .. code-block:: pycon

     >>> class Triangle:
     ...     def __init__(self, x, y):
     ...         self.__x = x
     ...         self.__y = y
     ...     @property
     ...     def x(self):
     ...         return self.__x
     ...     @x.setter
     ...     def x(self, new_x):
     ...         if new_x >= 0:
     ...             self.__x = new_x
     ...     @property
     ...     def y(self):
     ...         return self.__y
     ...     @y.setter
     ...     def y(self, new_y):
     ...         if new_y >= 0:
     ...             self.__y = new_y
     ...
     >>> t1 = Triangle(-2, 2)
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
       File "<stdin>", line 6, in __init__
     ValueError: The number must be greater or equal to zero.
     >>> t1 = Triangle(2, 2)
     >>> t1.x = -2
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
       File "<stdin>", line 13, in x
     ValueError: The number must be greater or equal to zero.
     >>> t1.x = 3
     >>> t1.x
     3

:doc:`/packs/distribution`
--------------------------

* If you want to create a task management package that writes the tasks to a
  database and provides them via a Python :abbr:`API (Application Programming
  Interface)` and a command line interface (:abbr:`CLI (Command-Line
  Interface)`), how would you structure the files?

  The package performs three types of actions:

  * Accessing the database
  * Providing a Python API
  * Providing a command line interface

  .. code-block:: console

     ├── README.rst
     ├── pyproject.toml
     └── src
         └── items
             ├── __init__.py
             ├── api.py
             ├── cli.py
             └── db.py

* Think about how you want to fulfil the above tasks. Which libraries and
  modules can you think of that could fulfil this task? Sketch the code for the
  modules of the Python API, the command line interface and the database
  connection.

  I would create a :class:`DB` class in :file:`src/items/db.py` for
  communication with the database, in the following example for `tinydb
  <https://tinydb.readthedocs.io/en/latest/>`_:

  .. code-block:: python

     import tinydb


     class DB:
         def __init__(self, db_path, db_file_prefix):
             self._db = tinydb.TinyDB(
                 db_path / f"{db_file_prefix}.json", create_dirs=True
             )

         def create(self, item: dict):
             """Create an item

             Returns:
                 id: The items id.
             """

             return id

         def read(self, id: int):
             """Reads an item.

             Args:
                 id (int): The item id of an item.
             Returns:
                 item: The item object."""
             return item

         def update(self, id: int, mods):
             """Update an item in the database.

             Args:
                 id (int): The item id of an item.
                 mods (Item): The modifications to be made to this item.
             """
             self._db.update(changes, doc_ids=[id])

         def delete(self, id: int):
             """Deletes an item in the database.

             Args:
                 id (int): The item id of an item.
             """
             self._db.remove(doc_ids=[id])

         def close(self):
             """Closes the database connection."""
             self._db.close()

  Then I would use :func:`dataclass` in :file:`src/items/api` to create an
  :class:`Item` class:

  .. code-block:: python

     from dataclasses import dataclass, field


     @dataclass
     class Item:
         summary: str = None
         owner: str = None
         state: str = "todo"
         id: int = field(default=None, compare=False)


     class ItemsException(Exception):
         pass


     class ItemsDB:
         def __init__(self, db_path):
             self._db_path = db_path
             self._db = DB(db_path, ".items_db")

         def add_item(self, item: Item):
             return

         def get_item(self, item: Item):
             return

         def update_item(self, item: Item):
             return

         def delete_item(self, item: Item):
             return

         def close(self):
             self._db.close()

         def path(self):
             return self._db_path

  :class:`ItemsException` Item and :class:`ItemsDB` are then provided in
  :file:`src/items/__init__.py`:

  .. code-block:: python

     from .api import ItemsException, Item, ItemsDB

  .. seealso::
     You can find a complete example at `github.com/veit/items
     <https://github.com/veit/items/>`_.

:doc:`/save-data/files-directories`
-----------------------------------

* Use the functions of the :mod:`python3:pathlib` module to take a path to a
  file named :file:`example.log` and create a new file path in the same
  directory for a file named :file:`example.log1`.

  .. code-block:: pycon

     >>> from pathlib import Path
     >>> l = Path("logs", "instance.log")
     >>> l1 = Path("logs", "instance.log1")
     >>> l.rename(l1)
     PosixPath('logs/instance.log1')

* What is the significance of adding ``b`` as a :term:`parameter` to
  :func:`python3:open`?

  This opens the file in binary mode, which means that bytes and not characters
  are read and written.

* Open a file :file:`my_file.txt` and insert additional text at the end of the
  file. Which command would you use to open :file:`my_file.txt`? Which command
  would you use to reopen the file and read it from the beginning?

  .. code-block:: pycon

     >>> from pathlib import Path
     >>> p = Path("docs", "save-data", "myfile.txt")
     >>> p.write_text("Hi, Pythonistas!\n")
     17
     >>> p.read_text()
     'Hi, Pythonistas!\n'

* If you look at the `man page for the wc utility
  <https://linux.die.net/man/1/wc>`_, you will see two command line options:

  ``-c``
      counts the bytes in the file
  ``-m``
      counts the characters, which in the case of some Unicode characters can be
      two or more bytes long

  Also, if a file is specified, our module should read from and process that
  file, but if no file is specified, it should read from and process ``stdin``.

  .. seealso::
     :ref:`_wcargv_stdin.py <wcargv_stdin>`

* If a context manager is used in a script that reads and/or writes multiple
  files, which of the following approaches do you think would be best?

  #. Put the entire script in a block managed by a ``with`` statement.
  #. Use one ``with`` statement for all reads and another for all writes.
  #. Use a ``with`` statement every time you read or write a file, that is, for
     every line.
  #. Use a ``with`` statement for each file you read or write.

  Probably 4. is the best approach as part of the context manager’s job when
  accessing files is to ensure that a file is closed.

* Archive :file:`*.txt` files from the current directory in the :file:`archive`
  directory as :file:`*.zip` files with the current date as the file name.

  * Which modules do you need for this?

    :mod:`python3:datetime`, :mod:`python3:pathlib` and :mod:`python3:zipfile`.

  * Write a possible solution.

    .. code-block:: pycon
       :linenos:

       >>> import datetime
       >>> import pathlib
       >>> import zipfile
       >>> file_pattern = "*.txt"
       >>> archive_path = "archive"
       >>> today = f"{datetime.date.today():%Y-%m-%d}"
       >>> cur_path = pathlib.Path(".")
       >>> paths = cur_path.glob(file_pattern)
       >>> zip_path = cur_path.joinpath(archive_path, today + ".zip")
       >>> zip_file = zipfile.ZipFile(str(zip_path), "w")
       >>> for path in paths:
       ...     zip_file.write(str(path))
       ...     path.unlink()
       ...

    Line 9
        creates the path to the ZIP file in the archive directory.
    Line 10
        opens the new ZIP file object for writing; :func:`str` is required to
        convert a path into a character string.
    Line 12
        writes the current file to the ZIP file.
    Line 13
         removes the current file from the working directory.

:doc:`/save-data/modules`
-------------------------

* What use cases can you imagine in which the :mod:`python3:struct` module would
  be useful for reading or writing binary data?

  * when reading and writing a binary file
  * when reading from an external interface, where the data should be stored
    exactly as it was transmitted

* Why :doc:`pickle <python3:library/pickle>` may or may not be suitable for the
  following use cases:

  #. Saving some state variables from one run to the next ✅
  #. Storing evaluation results ❌, as pickle is dependent on the respective
     Python version
  #. Saving user names and passwords ❌, as pickles are not secure
  #. Saving a large dictionary with English terms ❌, as the entire pickle would
     have to be loaded into memory
