Modules
=======

Modules are used in Python to organise larger projects. The Python standard
library is divided into modules to make it more manageable. You don’t have to
organise your own code into modules, but if you write larger programs or code
that you want to reuse, you should do so.

What is a module?
-----------------

A module is a file that contains code. It defines a group of Python functions or
other objects, and the name of the module is derived from the name of the file.
Modules usually contain Python source code, but can also be compiled C or C++
object files. Compiled modules and Python source modules are used in the same
way.

Modules not only group related Python objects together, but also help to avoid
naming conflicts. You can write a module called ``mymodule`` for your programme
that defines a function called ``my_func``. In the same programme, you may also
want to use another module called ``othermodule``, which also defines a
function called ``my_func``, but does something different from your ``my_func``
function. Without modules, it would be impossible to use two different functions
with the same name. With modules, you can refer to the functions
``mymodule.my_func`` and ``othermodule.my_func`` in your main programme. Using
the module names ensures that the two ``my_func`` functions are not confused, as
Python uses so-called namespaces. A namespace is essentially a dictionary of
names for the functions, classes, modules, :abbr:`etc. (et cetera)` available
there.

Modules are also used to make Python itself more manageable. Most of Python’s
standard functions are not integrated into the core of the language, but are
provided via special modules that you can load as needed.

Creating modules
----------------

Probably the best way to learn about modules is to create your own module. To do
this, we create a text file called :file:`wc.py`, and enter the Python code
below into this text file. If you use :ref:`idle`, select :menuselection:`File
--> New Window` and start typing.

It is easy to create your own modules that can be imported and used in the same
way as Python's built-in library modules. The example in this listing is a
simple module with a function that prompts for a file name and determines the
number of words that occur in that file.

.. literalinclude:: wc.py
   :linenos:

Lines 1,2 and 4
    :doc:`../document/docstrings` are standard methods for documenting modules,
    functions, methods and classes.
Line 9
    ``read`` returns a string containing all the characters in a file, and
    ``split`` returns a list of the words in a string using spaces.
Line 17
    You can use an ``\`` to split a long statement over several lines.
Lines 20 and 21
    With this ``if``-statement you can execute the program as a script by typing
    ``python3 wc.py`` in the command line.

First save this code in one of the directories of the module search path, which
can be found in the list of ``sys.path``. We recommend ``.py`` as the file name
extension, as this identifies the file as Python source code.

.. note::
   The list of directories displayed with ``sys.path`` depends on your system
   configuration. This list of directories is searched by Python in the order
   when an import statement is executed. The first module found that matches the
   import request is used. If there is no matching module in this search path,
   an ``ImportError`` is raised.

   If you are using :ref:`idle`, you can view the search path and the modules it
   contains graphically by using the :menuselection:`File --> Path Browser`
   window.

   The variable ``sys.path`` is initialised with the value of the environment
   variable ``PYTHONPATH``, if it exists. When you run a Python script, the
   ``sys.path`` variable for that script will have the directory where the
   script is located as the first element, so you can conveniently find out
   where the executing Python programme is located.

Now start the Python shell and enter the following:

.. code-block:: python

    >>> import wc
    >>> wc.words_occur()
    Enter the name of the file: README.rst
    File README.rst has 350 words (187 are unique)
    {'Quick': 1, ...}

Alternatively, you can also import ``words_occur`` directly:

.. code-block:: python

    >>> from wc import words_occur
    >>> words_occur()

You can use the interactive mode of the Python shell or :ref:`idle` to
incrementally test a module as you create it. However, if you change your module
on disk, entering the import command again will not reload it. For this purpose,
you must use the ``reload`` function from the :doc:`importlib
<python3:library/importlib>` module:

.. code-block:: python

    >>> import wc, importlib
    >>> importlib.reload(wc)
    <module 'wc' from '/home/veit/.local/lib/python3.8/site-packages/wc.py'>
