Mock
====

`Mock objects <https://en.wikipedia.org/wiki/Mock_object>`_ promote tests based
on the behaviour of objects.

Installation
------------

:doc:`python3:library/unittest.mock` has been in the standard library since
Python 3.3. For older versions of Python you can install it with:

.. code-block:: console

   $ python3 -m pip install mock

Example
-------

In our example we want to check whether working days are correctly determined
from Monday to Friday.

#. First we import ``datetime.datetime`` and ``Mock``:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 1-2
      :lineno-start: 1

#. We then define two test days:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 5-6
      :lineno-start: 5

#. Now we define a method to check the working days where Python’s datetime
   library treats Mondays as ``0`` and Sundays as ``6``:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 8-10
      :lineno-start: 8

#. Then we mock datetime:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 12
      :lineno-start: 12

#. Finally, we test our two mock objects:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 15,17
      :lineno-start: 15

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 19,21
      :lineno-start: 19
