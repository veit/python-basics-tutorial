Mock
====

`Mock objects <https://en.wikipedia.org/wiki/Mock_object>`_ promote tests based
on the behaviour of objects. The Python library :doc:`mock
<python3:library/unittest.mock>` enables you to replace parts of the system to
be tested with mock objects and to make assertions about their use.

.. seealso::

   With  `responses <https://github.com/getsentry/responses>`_ you can create
   mock objects for the `Requests
   <https://jupyter-tutorial.readthedocs.io/de/latest/data-processing/requests/index.html>`_
   library.

Installation
------------

:doc:`python3:library/unittest.mock` has been in the standard library since
Python 3.3. For older versions of Python you can install it with:

.. tab:: Linux/macOS

   .. code-block:: console

      $ bin/python -m pip install mock

.. tab:: Windows

   .. code-block:: ps1con

      C:> Scripts\python -m pip install mock

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
      :lines: 9-11
      :lineno-start: 9

#. Then we mock datetime:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 14
      :lineno-start: 14

#. Finally, we test our two mock objects:

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 17-19
      :lineno-start: 17

   .. literalinclude:: test_mock.py
      :language: python
      :lines: 21-23
      :lineno-start: 21

``patch`` decorator
-------------------

To create mock classes or objects, the ``patch`` decorator can be used. In the
following examples, the output of ``os.listdir`` is mocked. For this, the file
``example.txt`` does not have to be present in the directory:

.. code-block:: python

    import os
    from unittest import mock
    @mock.patch("os.listdir", mock.MagicMock(return_value="example.txt"))
    def test_listdir():
        assert "example.txt" == os.listdir()

Alternatively, the return value can also be defined separately:

.. code-block:: python

    @mock.patch("os.listdir")
    def test_listdir(mock_listdir):
        mock_listdir.return_value = "example.txt"
        assert "example.txt" == os.listdir()
