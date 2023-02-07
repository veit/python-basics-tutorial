pytest
======

`pytest <https://docs.pytest.org/>`_ is an alternative to Python’s :doc:`unittest`
module that makes testing even easier.

Features
--------

* More detailed information on failing assert statements
* Automatic discovery of test modules and functions
* Modular fixtures for managing small or parametrised long lived test resources
* Can also run unittests out of the box
* Rich plugin architecture, with over 800 external plugins

Installation
------------

.. tab:: Linux/macOS

   .. code-block:: console

    $ bin/python -m pip install pytest
    Collecting pytest
    …
    Successfully installed attrs-21.2.0 iniconfig-1.1.1 pluggy-1.0.0 py-1.10.0 pytest-6.2.5 toml-0.10.2

.. tab:: Windows

   .. code-block:: ps1con

    C:> Scripts\python -m pip install pytest
    Collecting pytest
    …
    Successfully installed attrs-21.2.0 iniconfig-1.1.1 pluggy-1.0.0 py-1.10.0 pytest-6.2.5 toml-0.10.2

Single test
-----------

.. literalinclude:: test_pytest.py
   :language: python
   :lines: 1-4, 19-24
   :lineno-start: 1

``key``
    function that will be called to transform the collection’s items before they are
    compared. The parameter passed to key must be something that is callable.
``lambda``
    Function that in case of ``sorted`` only takes one parameter.

Test ficture
------------

Write a :term:`test fixture <Test Fixture>` with the ``@pytest.fixture``
decorator:

.. literalinclude:: test_pytest.py
   :language: python
   :lines: 9-16
   :lineno-start: 9

Test parameterisation
---------------------

.. literalinclude:: test_pytest.py
   :language: python
   :lines: 35-
   :lineno-start: 35

Run pytest
----------

.. tab:: Linux/macOS

   .. code-block:: console

      $ bin/python -m pytest -v
      ============================= test session starts ==============================
      platform darwin -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0 -- /Users/veit/python-basics/bin/python
      rootdir: /Users/veit/python-basics/docs/test
      plugins: hypothesis-6.23.2
      collected 5 items

      test_pytest.py::test_sorted PASSED                                       [ 20%]
      test_pytest.py::test_sorted__key_example_1 PASSED                        [ 40%]
      test_pytest.py::test_sorted__key_example_2 PASSED                        [ 60%]
      test_pytest.py::test_examples[input0-expected0] PASSED                   [ 80%]
      test_pytest.py::test_examples[zasdqw-expected1] PASSED                   [100%]

      ============================== 5 passed in 0.02s ===============================

.. tab:: Windows

   .. code-block:: ps1con

      C:> Scripts\python -m pytest -v
      ============================= test session starts ==============================
      platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
      rootdir: C:\Users\veit\python-basics\docs\test
      plugins: hypothesis-6.23.2
      collected 5 items

      test_pytest.py::test_sorted PASSED                                       [ 20%]
      test_pytest.py::test_sorted__key_example_1 PASSED                        [ 40%]
      test_pytest.py::test_sorted__key_example_2 PASSED                        [ 60%]
      test_pytest.py::test_examples[input0-expected0] PASSED                   [ 80%]
      test_pytest.py::test_examples[zasdqw-expected1] PASSED                   [100%]

      ============================== 5 passed in 0.02s ===============================
