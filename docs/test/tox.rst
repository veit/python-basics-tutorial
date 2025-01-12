tox
===

`tox <https://tox.readthedocs.io/>`_ is an automation tool that works similarly
to a :term:`CI` tool, but can be run both locally and in conjunction with other
CI tools on a server.

In the following, we will set up tox for our Items application so that it helps
us with local testing. We will then set up testing using GitHub Actions.

Introduction to tox
-------------------

tox is a command line tool that allows you to run your complete test suite in
different environments. We will use tox to test the Items project in multiple
Python versions, but tox is not limited to Python versions only. You can use it
to test with different dependency configurations and different configurations
for different operating systems. tox uses project information from the
:file:`setup.py` or :file:`pyproject.toml` file for the package under test to
create an installable :doc:`distribution of your package
<../packs/distribution>`. It searches the :file:`tox.ini` file for a list of
environments and then performs the following steps for each:

#. creates a :term:`virtual environment <Virtual environment>`,
#. installs some dependencies with :term:`pip`,
#. build your package,
#. install your package with pip,
#. run further tests.

After all environments have been tested, tox outputs a summary of the results.

.. note::
   Although tox is used by many projects, there are alternatives that fulfil
   similar functions. Two alternatives to tox are `nox
   <https://nox.thea.codes/en/stable/>`_ and `invoke
   <https://www.pyinvoke.org>`_.

Setting up tox
--------------

Until now, we had the items code in a :file:`src/` directory and the tests in
:file:`tests/api/` and :file:`tests/cli/`. Now we will add a :file:`tox.ini` file
so that the structure looks like this:

.. code-block:: console
   :emphasize-lines: 16

   items
    ├── …
    ├── pyproject.toml
    ├── src
    │   └── items
    │       └── …
    ├── tests
    │   ├── api
    │   │   ├── __init__.py
    │   │   ├── conftest.py
    │   │   └── test_….py
    │   └── cli
    │       ├── __init__.py
    │       ├── conftest.py
    │       └── test_….py
    └── tox.ini

This is a typical layout for many projects. Let’s take a look at a simple
:file:`tox.ini` file in the Items project:

.. code-block:: ini

   [tox]
   envlist = py313
   isolated_build = True

   [testenv]
   deps =
     pytest>=6.0
     faker
   commands = pytest

In the ``[tox]`` section, we have defined ``envlist = py313``. This is a
shortcut that tells tox to run our tests with Python version 3.13. We will be
adding more Python versions shortly, but using one version helps to understand
the flow of tox.

Also note the line ``isolated_build = True``: This is required for all packages
configured with :file:`pyproject.toml`. However, for all projects configured with
:file:`setup.py` that use the :term:`setuptools` library, this line can be
omitted.

In the ``[testenv]`` section, ``pytest`` and ``faker`` are listed as dependencies
under ``deps``. So tox knows that we need these two tools for testing. If you
wish, you can also specify which version should be used, for example
``pytest>=6.0``. Finally, commands instruct tox to execute ``pytest`` in every
environment.

Executing tox
-------------

Before you can run tox, you must ensure that you have installed it:

.. tab:: Linux/macOS

   .. code-block:: console

      $ python3 -m venv .venv
      $ . .venv/bin/activate
      $ python -m pip install tox

.. tab:: Windows

   .. code-block:: ps1con

      C:> python -m venv .venv
      C:> .venv\Scripts\activate.bat
      C:> python -m pip install tox

To run tox, simply start tox:

.. code-block:: pytest

   $ python -m tox
   py313: install_package> python -I -m pip install --force-reinstall --no-deps /Users/veit/cusy/prj/items/.tox/.tmp/package/20/items-0.1.0.tar.gz
   py313: commands[0]> coverage run -m pytest
   ============================= test session starts ==============================
   platform darwin -- Python 3.13.0, pytest-8.3.3, pluggy-1.5.0
   cachedir: .tox/py313/.pytest_cache
   rootdir: /Users/veit/cusy/prj/items
   configfile: pyproject.toml
   testpaths: tests
   plugins: cov-5.0.0, anyio-4.6.0, Faker-30.3.0
   collected 49 items

   tests/api/test_add.py ....                                               [  8%]
   tests/api/test_config.py .                                               [ 10%]
   tests/api/test_count.py ...                                              [ 16%]
   tests/api/test_delete.py ...                                             [ 22%]
   tests/api/test_finish.py ....                                            [ 30%]
   tests/api/test_list.py .........                                         [ 48%]
   tests/api/test_start.py ....                                             [ 57%]
   tests/api/test_update.py ....                                            [ 65%]
   tests/api/test_version.py .                                              [ 67%]
   tests/cli/test_add.py ..                                                 [ 71%]
   tests/cli/test_config.py ..                                              [ 75%]
   tests/cli/test_count.py .                                                [ 77%]
   tests/cli/test_delete.py .                                               [ 79%]
   tests/cli/test_errors.py ....                                            [ 87%]
   tests/cli/test_finish.py .                                               [ 89%]
   tests/cli/test_list.py ..                                                [ 93%]
   tests/cli/test_start.py .                                                [ 95%]
   tests/cli/test_update.py .                                               [ 97%]
   tests/cli/test_version.py .                                              [100%]

   ============================== 49 passed in 0.16s ==============================
   .pkg: _exit> python /Users/veit/cusy/prj/items/.venv/lib/python3.13/site-packages/pyproject_api/_backend.py True hatchling.build
   py313: OK ✔ in 1.48 seconds
     congratulations :) (1.48 seconds)

Testing multiple Python versions
--------------------------------

To do this, we extend ``envlist`` in the :file:`tox.ini` file to add further
Python versions:

.. code-block:: ini
   :emphasize-lines: 2, 4

   [tox]
   envlist = py39, py310, py311, py312, py313
   isolated_build = True
   skip_missing_interpreters = True

We will now test Python versions from 3.8 to 3.11. In addition, we have also
added the setting ``skip_missing_interpreters = True`` so that tox does not fail
if one of the listed Python versions is missing on your system. If the value is
set to ``True``, tox will run the tests with every available Python version, but
will skip versions it doesn’t find without failing. The output is very similar,
although I will only highlight the differences in the following illustration:

.. code-block:: pytest
   :emphasize-lines: 3-4, 8-12, 16-20, 24-28, 32-

   $ python -m tox
   ...
   py39: install_package> python -I -m pip install --force-reinstall --no-deps /Users/veit/cusy/prj/items/.tox/.tmp/package/17/items-0.1.0.tar.gz
   py39: commands[0]> coverage run -m pytest
   ============================= test session starts ==============================
   ...
   ============================== 49 passed in 0.16s ==============================
   py39: OK ✔ in 2.17 seconds
   py310: skipped because could not find python interpreter with spec(s): py310
   py310: SKIP ⚠ in 0.01 seconds
   py311: install_package> python -I -m pip install --force-reinstall --no-deps /Users/veit/cusy/prj/items/.tox/.tmp/package/18/items-0.1.0.tar.gz
   py311: commands[0]> coverage run -m pytest
   ============================= test session starts ==============================
   ...
   ============================== 49 passed in 0.15s ==============================
   py311: OK ✔ in 1.41 seconds
   py312: install_package> python -I -m pip install --force-reinstall --no-deps /Users/veit/cusy/prj/items/.tox/.tmp/package/19/items-0.1.0.tar.gz
   py312: commands[0]> coverage run -m pytest
   ============================= test session starts ==============================
   ...
   ============================== 49 passed in 0.15s ==============================
   py312: OK ✔ in 1.43 seconds
   py313: install_package> python -I -m pip install --force-reinstall --no-deps /Users/veit/cusy/prj/items/.tox/.tmp/package/20/items-0.1.0.tar.gz
   py313: commands[0]> coverage run -m pytest
   ============================= test session starts ==============================
   ...
   ============================== 49 passed in 0.16s ==============================
   .pkg: _exit> python /Users/veit/cusy/prj/items/.venv/lib/python3.13/site-packages/pyproject_api/_backend.py True hatchling.build
   py313: OK ✔ in 1.48 seconds
     py39: OK (2.17=setup[1.54]+cmd[0.63] seconds)
     py310: SKIP (0.01 seconds)
     py311: OK (1.41=setup[0.81]+cmd[0.60] seconds)
     py312: OK (1.43=setup[0.82]+cmd[0.61] seconds)
     py313: OK (1.48=setup[0.82]+cmd[0.66] seconds)
     congratulations :) (10.46 seconds)

Running Tox environments in parallel
------------------------------------

In the previous example, the different environments were executed one after the
other. It is also possible to run them in parallel with the ``-p`` option:

.. code-block:: pytest

   $ python -m tox -p
   py310: SKIP ⚠ in 0.09 seconds
   py312: OK ✔ in 2.08 seconds
   py313: OK ✔ in 2.18 seconds
   py311: OK ✔ in 2.23 seconds
   py39: OK ✔ in 2.91 seconds
     py39: OK (2.91=setup[2.17]+cmd[0.74] seconds)
     py310: SKIP (0.09 seconds)
     py311: OK (2.23=setup[1.27]+cmd[0.96] seconds)
     py312: OK (2.08=setup[1.22]+cmd[0.86] seconds)
     py313: OK (2.18=setup[1.23]+cmd[0.95] seconds)
     congratulations :) (3.05 seconds)

.. note::
   The output is not abbreviated; this is the full output you will see if
   everything works.

Add coverage report in tox
--------------------------

The configuration of coverage reports can easily be added to the :file:`tox.ini`
file. To do this, we need to add ``pytest-cov`` to the ``deps`` settings so that
the ``pytest-cov`` plugin is installed in the tox test environments. Including
``pytest-cov`` also includes all its dependencies, such as ``coverage``. We then
extend commands to ``pytest --cov=items``:

.. code-block::
   :emphasize-lines: 12-

   [tox]
   envlist = py3{9,10,11,12,13}
   isolated_build = True
   skip_missing_interpreters = True

   [testenv]
   deps =
    pytest>=6.0
    faker
   commands = pytest

   [testenv:coverage-report]
   description = Report coverage over all test runs.
   deps = coverage[toml]
   skip_install = true
   allowlist_externals = coverage
   commands =
     coverage combine
     coverage report

When using Coverage with ``tox``, it can sometimes be useful to add a section in
the :file:`:file:`pyproject.toml`` file to tell Coverage which source code paths
should be considered identical:

.. code-block:: ini

   [tool.coverage.paths]
   source = ["src", ".tox/py*/**/site-packages"]

The items source code is initially located in :file:`src/items/` before tox
creates the virtual environments and installs items in the environment. It is
then located in :file:`.tox/py313/lib/python3.13/site-packages/items`, for
example.

.. code-block:: console
   :emphasize-lines: 1

   $ python -m tox
   ...
   coverage-report: commands[0]> coverage combine
   Combined data file .coverage.fay.local.19539.XpQXpsGx
   coverage-report: commands[1]> coverage report
   Name               Stmts   Miss Branch BrPart  Cover   Missing
   --------------------------------------------------------------
   src/items/api.py      68      1     12      1    98%   88
   --------------------------------------------------------------
   TOTAL                428      1     32      1    99%

   26 files skipped due to complete coverage.
     py39: OK (2.12=setup[1.49]+cmd[0.63] seconds)
     py310: SKIP (0.01 seconds)
     py311: OK (1.41=setup[0.80]+cmd[0.62] seconds)
     py312: OK (1.43=setup[0.81]+cmd[0.62] seconds)
     py313: OK (1.46=setup[0.83]+cmd[0.62] seconds)
     coverage-report: OK (0.16=setup[0.00]+cmd[0.07,0.09] seconds)
     congratulations :) (10.26 seconds)

Set minimum coverage
--------------------

When executing coverage by tox, it also makes sense to define a minimum coverage
level in order to recognise any coverage failures. This is achieved with the
``--cov-fail-under`` option:

.. code-block:: console
   :emphasize-lines: 8

   Name               Stmts   Miss Branch BrPart  Cover   Missing
   --------------------------------------------------------------
   src/items/api.py      68      1     12      1    98%   88
   --------------------------------------------------------------
   TOTAL                428      1     32      1    99%

   26 files skipped due to complete coverage.
   Coverage failure: total of 99 is less than fail-under=100

This adds the highlighted line to the output.

.. _posargs:

Passing pytest parameters to tox
--------------------------------

We can also call individual tests with tox by making another change so that
parameters can be passed to pytest:

.. code-block:: ini
   :emphasize-lines: 17

   [tox]
   envlist =
       pre-commit
       docs
       py3{9,10,11,12,13}
       coverage-report
   isolated_build = True
   skip_missing_interpreters = True

   [testenv]
   extras =
     tests: tests
   deps =
     tests: coverage[toml]
   allowlist_externals = coverage
   commands =
     coverage run -m pytest {posargs}

To pass arguments to pytest, insert them between the tox arguments and the
pytest arguments. In this case, we select ``test_version`` tests with the ``-k``
keyword option. We also use ``--no-cov`` to disable coverage:

.. code-block:: pytest
   :emphasize-lines: 1, 3

   $ tox -e py313 -- -k test_version --no-cov
   ...
   py313: commands[0]> coverage run -m pytest -k test_version --no-cov
   ============================= test session starts ==============================
   platform darwin -- Python 3.13.0, pytest-8.3.3, pluggy-1.5.0
   cachedir: .tox/py313/.pytest_cache
   rootdir: /Users/veit/cusy/prj/items
   configfile: pyproject.toml
   testpaths: tests
   plugins: cov-5.0.0, anyio-4.6.0, Faker-30.3.0
   collected 49 items / 47 deselected / 2 selected

   tests/api/test_version.py .                                              [ 50%]
   tests/cli/test_version.py .                                              [100%]

   ======================= 2 passed, 47 deselected in 0.07s =======================
   .pkg: _exit> python /Users/veit/cusy/prj/items/.venv/lib/python3.13/site-packages/pyproject_api/_backend.py True hatchling.build
     py313: OK (1.49=setup[0.96]+cmd[0.53] seconds)
     congratulations :) (1.53 seconds)

``tox`` is not only ideal for the local automation of test processes, but also
helps with server-based :term:`CI`. Let’s continue with the execution of pytest
and tox using GitHub actions.

Running ``tox`` with GitHub actions
-----------------------------------

If your project is hosted on `GitHub <https://github.com/>`_, you can use GitHub
actions to automatically run your tests in different environments. A whole range
of environments are available for GitHub actions:
`github.com/actions/virtual-environments
<https://github.com/actions/runner-images?tab=readme-ov-file>`_.

#. To create a GitHub action in your project, click on :menuselection:`Actions
   --> set up a workflow yourself`. This usually creates a
   :file:`.github/workflows/main.yml` file.
#. Give this file a more descriptive name. We usually use :file:`ci.yml` for
   this.
#. The prefilled YAML file is not very helpful for our purposes. You can add a
   ``coverage`` section, for example with:

   .. code-block:: yaml

      jobs:
        coverage:
          name: Ensure 99% test coverage
          runs-on: ubuntu-latest
          needs: tests
          if: always()
          steps:
            - uses: actions/checkout@v4
            - uses: actions/setup-python@v5
              with:
                cache: pip
                python-version: 3.13
            - name: Download coverage data
              uses: actions/download-artifact@v4
              with:
                pattern: coverage-data-*
                merge-multiple: true
            - name: Combine coverage and fail if it’s <99%.
              run: |
                python -m pip install --upgrade coverage[toml]
                python -m coverage combine
                python -m coverage html --skip-covered --skip-empty
                # Report and write to summary.
                python -m coverage report --format=markdown >> $GITHUB_STEP_SUMMARY
                # Report again and fail if under 99%.
                python -m coverage report --fail-under=99

   ``name``
       can be any name. It is displayed in the GitHub Actions user interface.
   ``steps``
       is a list of steps. The name of each step can be arbitrary and is
       optional.
   ``uses: actions/checkout@v4``
       is a GitHub actions tool that checks out our repository so that the rest
       of the workflow can access it.
   ``uses: actions/setup-python@v5``
       is a GitHub actions tool that configures Python and installs it in a build
       environment.
   ``with: python-version: ${{ matrix.python }}``
       says that an environment should be created for each of the Python versions
       listed in ``matrix.python``.
   ``run: python -m pip install tox tox-gh-actions``
       installs tox and simplifies the execution of tox in GitHub actions with
       `tox-gh-actions <https://pypi.org/project/tox-gh-actions/>`_ by providing
       the environment that tox itself uses as the environment for the tests.
       However, we still need to adjust our :file:`tox.ini` file for this, for
       example:

       .. code-block:: ini

          [gh-actions]
          python =
              3.9: py39
              3.10: py310
              3.11: py311
              3.12: py312
              3.13: py313

       This assigns GitHub actions to tox environments.

       .. note::
          * You do not need to specify all variants of your environment. This
            distinguishes ``tox-gh-actions`` from ``tox -e py``.
          * Make sure that the versions in the ``[gh-actions]`` section match the
            available Python versions and, if applicable, those in the
            :ref:`GitHub actions for Git pre-commit hooks
            <gh-action-pre-commit-example>`.
          * Since all tests for a specific Python version are executed one after
            the other in a container, the advantages of parallel execution are
            lost.

   ``run: python -m tox``
       executes tox.

#. You can then click on :guilabel:`Start commit`. As we want to make further
   changes before the tests are executed automatically, we select
   :guilabel:`Create a new branch for this commit and start a pull request` and
   github-actions as the name for the new :term:`branch <branch>`. Finally, you
   can click on :guilabel:`Create pull request`.
#. To switch to the new branch, we go to :menuselection:`Code --> main -->
   github-actions`.

The actions syntax is well documented. A good starting point in the GitHub
Actions documentation is the `Building and Testing Python
<https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python>`__
page. The documentation also shows you how to run pytest directly without tox and
how to extend the matrix to multiple operating systems. As soon as you have set
up your :file:`*.yml` file and uploaded it to your GitHub repository, it will be
executed automatically. You can then see the runs in the :menuselection:`Actions`
tab:

.. figure:: github-actions.png
   :alt: Screenshot of the GitHub actions overview

The different Python environments are listed on the left-hand side. If you select
one, the results for this environment are displayed, as shown in the following
screenshot:

.. figure:: github-actions-run.png
   :alt: Screenshot of a GitHub actions run for an environment

.. seealso::
   * `Building and testing Python
     <https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python>`__
   * `Workflow syntax for GitHub Actions
     <https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions>`_

Display badge
-------------

Now you can add a badge of your :term:`CI` status to your :file:`README.rst`
file, for example with:

.. code-block:: rest

   .. image:: https://github.com/YOU/YOUR_PROJECT/workflows/CI/badge.svg?branch=main
      :target: https://github.com/YOU/YOUR_PROJECT/actions?workflow=CI
      :alt: CI Status

Publish test coverage
---------------------

You can publish the test coverage on GitHub, see also :ref:`Coverage
GitHub-Actions <coverage-github-actions>`.

Extend tox
----------

tox uses `pluggy <https://pluggy.readthedocs.io/en/stable/>`_ to customise the
default behaviour. Pluggy finds a plugin by searching for an entry point with the
name ``tox``, for example in a :file:`pyproject.toml` file:

.. code-block:: toml

   [project.entry-points.tox]
   my_plugin = "my_plugin.hooks"

To use the plugin, it therefore only needs to be installed in the same
environment in which tox is running and it is found via the defined entry point.

A plugin is created by implementing extension points in the form of hooks. For
example, the following code snippet would define a new ``--my`` :abbr:`CLI
(Command Line Interface)`:

.. code-block:: python

   from tox.config.cli.parser import ToxParser
   from tox.plugin import impl


   @impl
   def tox_add_option(parser: ToxParser) -> None:
       parser.add_argument("--my", action="store_true", help="my option")

.. seealso::
   * `Extending tox <https://tox.wiki/en/latest/plugins.html>`_
   * `tox development team <https://github.com/orgs/tox-dev/repositories>`_

.. _tox_uv:

``tox-uv``
----------

`tox-uv <https://pypi.org/project/tox-uv/>`_ is a Tox plugin that replaces
:term:`virtualenv` and :term:`pip` with :term:`uv` in your Tox environments.

You can install ``tox`` and ``tox-uv`` with:

.. code-block:: console

   $ uv tool install tox --with tox-uv

``uv.lock`` support
~~~~~~~~~~~~~~~~~~~

If you want to use ``uv sync`` with a ``uv.lock`` file for a Tox environment,
you must change the runner for this Tox environment to ``uv-venv-lock-runner``.
You should also use the extras configuration in such environments to instruct
``uv`` to install the specified extras, for example:

.. code-block:: ini
   :caption: tox.ini

   [testenv]
   runner = uv-venv-lock-runner
   extras =
       dev
   commands = pytest

``dev`` uses the ``uv-venv-lock-runner`` and uses ``uv sync`` to install
dependencies in the environment with the ``dev`` extras.
