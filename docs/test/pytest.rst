pytest
======

`pytest <https://docs.pytest.org/>`_ is an alternative to Python’s
:doc:`unittest` module that makes testing even easier.

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
    function that will be called to transform the collection’s items before they
    are compared. The parameter passed to key must be something that is
    callable.
``lambda``
    Function that in case of ``sorted`` only takes one parameter.


To structure test functions, you can follow the :abbr:`AAA (Arrange/Act/Assert)`
or :abbr:`GWT (Given/When/Then)` pattern.

Structure the test-suite
------------------------

Use a directory structure that corresponds to the way you want to run your code,
because it is easy to run an entire subdirectory. You can subdivide features and
functions, or use subsystems as a basis, or use the code structure as a guide.
You can also use :samp:`-k {FILTER}` to filter directories, classes or test
prefixes.

Test fixtures
-------------

Write a :term:`test fixture <Test Fixture>` with the ``@pytest.fixture``
decorator:

.. literalinclude:: test_pytest.py
   :language: python
   :lines: 9-16
   :lineno-start: 9

.. seealso::
   * `About fixtures
     <https://docs.pytest.org/en/latest/explanation/fixtures.html#about-fixtures>`_
   * `Fixtures reference
     <https://docs.pytest.org/en/latest/reference/fixtures.html>`_
   * `How to use fixtures
     <https://docs.pytest.org/en/latest/how-to/fixtures.html#how-to-fixtures>`_

Markers
-------

:samp:`@pytest.mark.{MYMARKER}`-Markers
    allows you to group or selectively disable tests.
:file:`pytest.ini`
    registers the markers.

    Alternatively, you can use ``pytestmark`` in Python files: :samp:`pytestmark
    = [pytest.mark.{MYMARKER1}, pytest.mark.{MYMARKER2}]`.

:samp:`--strict-markers`
    converts missing registrations into errors.

:samp:`--markers`
    displays all available markers.
:samp:`xfail`
    indicates that the test should fail.

    :samp:`-ra` oder :samp:`-rxX`
        shows the reasons why the test failed.

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

Plugins
-------

`pytest-asyncio <https://pypi.org/project/pytest-asyncio/>`_
    makes code testing easier if you use the
    :doc:`asyncio <python3:library/asyncio>` library.
`pytest-cov <https://pypi.org/project/pytest-cov/>`_
    creates coverage reports.
:doc:`pytest-grpc <jupyter-tutorial:data-processing/apis/grpc/test>`
    is a pytest plugin for
    :doc:`jupyter-tutorial:data-processing/apis/grpc/index`.
`pytest-icdiff <https://pypi.org/project/pytest-icdiff/>`_
    improves diffs in Pytest assertion error messages with `ICDiff
    <https://www.jefftk.com/icdiff>`_.

.. seealso::
   `Plugin List <https://docs.pytest.org/en/7.1.x/reference/plugin_list.html>`_
