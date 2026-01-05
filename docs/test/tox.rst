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

#. creates a :term:`virtual environment <Virtual environment>`
#. installs some dependencies with :term:`pip`
#. build your package
#. install your package with pip
#. run further tests

After all environments have been tested, tox outputs a summary of the results.

To accelerate this process with :term:`uv`, we don’t use tox directly, but
`tox-uv <https://github.com/tox-dev/tox-uv>`_.

Setting up tox
--------------

Until now, we had the items code in a :file:`src/` directory and the tests in
:file:`tests/api/` and :file:`tests/cli/`. Now we will add a :file:`tox.ini`
file so that the structure looks like this:

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

   [testenv]
   deps =
     pytest>=6.0
     faker
   commands = pytest

In the ``[tox]`` section, we have defined ``envlist = py313``. This is a
shortcut that tells tox to run our tests with Python version 3.13. We will be
adding more Python versions shortly, but using one version helps to understand
the flow of tox.

In the ``[testenv]`` section, ``pytest`` and ``faker`` are listed as
dependencies under ``deps``. So tox knows that we need these two tools for
testing. If you wish, you can also specify which version should be used, for
example ``pytest>=6.0``. Finally, commands instruct tox to execute ``pytest`` in
every environment.

Executing tox
-------------

Before you can run tox, you must ensure that you have installed tox-uv:

.. tab:: Linux/macOS

   .. code-block:: console

      $ uv sync --group dev

.. tab:: Windows

   .. code-block:: ps1con

      C:> uv sync --group dev

To run tox, simply start tox:

.. code-block:: pytest

   $ uv run tox
   .pkg: _optional_hooks> python /Users/veit/cusy/prj/items/.venv/lib/python3.13/site-packages/pyproject_api/_backend.py True hatchling.build
   .pkg: get_requires_for_build_sdist> python /Users/veit/cusy/prj/items/.venv/lib/python3.13/site-packages/pyproject_api/_backend.py True hatchling.build
   .pkg: build_sdist> python /Users/veit/cusy/prj/items/.venv/lib/python3.13/site-packages/pyproject_api/_backend.py True hatchling.build
   py313: install_package> .venv/bin/uv pip install --reinstall --no-deps items@/Users/veit/cusy/prj/items/.tox/.tmp/package/18/items-0.1.0.tar.gz
   py313: commands[0]> python --version --version
   Python 3.13.0 (main, Oct  7 2024, 23:47:22) [Clang 18.1.8 ]
   py313: commands[1]> coverage run -m pytest
   ============================= test session starts ==============================
   platform darwin -- Python 3.13.0, pytest-9.0.2, pluggy-1.6.0
   cachedir: .tox/py313/.pytest_cache
   rootdir: /Users/veit/cusy/prj/items
   configfile: pyproject.toml
   testpaths: tests
   plugins: Faker-40.1.0, cov-7.0.0
   collected 83 items

   tests/api/test_add.py ......                                             [  7%]
   tests/api/test_config.py .                                               [  8%]
   tests/api/test_count.py ...                                              [ 12%]
   tests/api/test_delete.py ...                                             [ 15%]
   tests/api/test_delete_all.py ..                                          [ 18%]
   tests/api/test_exceptions.py ..                                          [ 20%]
   tests/api/test_finish.py ....                                            [ 25%]
   tests/api/test_item.py ...                                               [ 28%]
   tests/api/test_item_id.py .                                              [ 30%]
   tests/api/test_list.py .........                                         [ 40%]
   tests/api/test_list_edge_cases.py ........                               [ 50%]
   tests/api/test_start.py ....                                             [ 55%]
   tests/api/test_update.py .....                                           [ 61%]
   tests/api/test_version.py .                                              [ 62%]
   tests/cli/test_add.py ..                                                 [ 65%]
   tests/cli/test_config.py ..                                              [ 67%]
   tests/cli/test_count.py .                                                [ 68%]
   tests/cli/test_delete.py .                                               [ 69%]
   tests/cli/test_errors.py .......                                         [ 78%]
   tests/cli/test_finish.py .                                               [ 79%]
   tests/cli/test_help.py .........                                         [ 90%]
   tests/cli/test_list.py .....                                             [ 96%]
   tests/cli/test_start.py .                                                [ 97%]
   tests/cli/test_update.py .                                               [ 98%]
   tests/cli/test_version.py .                                              [100%]

   ============================== 83 passed in 0.35s ==============================
   .pkg: _exit> python /Users/veit/cusy/prj/items/.venv/lib/python3.13/site-packages/pyproject_api/_backend.py True hatchling.build
     py313: OK (1.19=setup[0.45]+cmd[0.01,0.72] seconds)
     congratulations :) (1.23 seconds)

Testing multiple Python versions
--------------------------------

To do this, we extend ``envlist`` in the :file:`tox.ini` file to add further
Python versions:

.. code-block:: ini

   [tox]
   envlist =
     py3{10-14}
     py3{13-14}t
   skip_missing_interpreters = True

We will now test Python versions from 3.10 to 3.14. In addition, we have also
added the setting ``skip_missing_interpreters = True`` so that tox does not fail
if one of the listed Python versions is missing on your system. If the value is
set to ``True``, tox will run the tests with every available Python version, but
will skip versions it doesn’t find without failing. The output is very similar,
although I will only highlight the differences in the following illustration:

.. code-block:: pytest
   :emphasize-lines: 3-6, 10-14, 18-22, 26-30, 34-38, 42-46, 50-54, 59-

    $ uv run tox
    ...
    py310: install_package> .venv/bin/uv pip install --reinstall --no-deps items@/Users/veit/cusy/prj/items/.tox/.tmp/package/19/items-0.1.0.tar.gz
    py310: commands[0]> python --version --version
    Python 3.10.17 (main, Apr  9 2025, 03:47:39) [Clang 20.1.0 ]
    py310: commands[1]> coverage run -m pytest
    ============================= test session starts ==============================
    ...
    ============================== 83 passed in 0.35s ==============================
    py310: OK ✔ in 1.3 seconds
    py311: install_package> .venv/bin/uv pip install --reinstall --no-deps items@/Users/veit/cusy/prj/items/.tox/.tmp/package/20/items-0.1.0.tar.gz
    py311: commands[0]> python --version --version
    Python 3.11.11 (main, Feb  5 2025, 18:58:27) [Clang 19.1.6 ]
    py311: commands[1]> coverage run -m pytest
    ============================= test session starts ==============================
    ...
    ============================== 83 passed in 0.36s ==============================
    py311: OK ✔ in 1.16 seconds
    py312: install_package> .venv/bin/uv pip install --reinstall --no-deps items@/Users/veit/cusy/prj/items/.tox/.tmp/package/21/items-0.1.0.tar.gz
    py312: commands[0]> python --version --version
    Python 3.12.12 (main, Oct 14 2025, 21:38:21) [Clang 20.1.4 ]
    py312: commands[1]> coverage run -m pytest
    ============================= test session starts ==============================
    ...
    ============================== 83 passed in 0.55s ==============================
    py312: OK ✔ in 1.79 seconds
    py313: install_package> .venv/bin/uv pip install --reinstall --no-deps items@/Users/veit/cusy/prj/items/.tox/.tmp/package/22/items-0.1.0.tar.gz
    py313: commands[0]> python --version --version
    Python 3.13.0 (main, Oct  7 2024, 23:47:22) [Clang 18.1.8 ]
    py313: commands[1]> coverage run -m pytest
    ============================= test session starts ==============================
    ...
    ============================== 83 passed in 0.35s ==============================
    py313: OK ✔ in 1.07 seconds
    py314: install_package> .venv/bin/uv pip install --reinstall --no-deps items@/Users/veit/cusy/prj/items/.tox/.tmp/package/23/items-0.1.0.tar.gz
    py314: commands[0]> python --version --version
    Python 3.14.0 (main, Oct 14 2025, 21:10:22) [Clang 20.1.4 ]
    py314: commands[1]> coverage run -m pytest
    ============================= test session starts ==============================
    ...
    ============================== 83 passed in 0.36s ==============================
    py314: OK ✔ in 1.28 seconds
    py313t: install_package> .venv/bin/uv pip install --reinstall --no-deps items@/Users/veit/cusy/prj/items/.tox/.tmp/package/24/items-0.1.0.tar.gz
    py313t: commands[0]> python --version --version
    Python 3.13.0 experimental free-threading build (main, Oct 16 2024, 08:24:33) [Clang 18.1.8 ]
    py313t: commands[1]> coverage run -m pytest
    ============================= test session starts ==============================
    ...
    ============================== 83 passed in 0.49s ==============================
    py313t: OK ✔ in 1.51 seconds
    py314t: install_package> .venv/bin/uv pip install --reinstall --no-deps items@/Users/veit/cusy/prj/items/.tox/.tmp/package/25/items-0.1.0.tar.gz
    py314t: commands[0]> python --version --version
    Python 3.14.0b4 free-threading build (main, Jul  8 2025, 21:06:49) [Clang 20.1.4 ]
    py314t: commands[1]> coverage run -m pytest
    ============================= test session starts ==============================
    ...
    ============================== 83 passed in 0.39s ==============================
    .pkg: _exit> python /Users/veit/cusy/prj/items/.venv/lib/python3.13/site-packages/pyproject_api/_backend.py True hatchling.build
      py310: OK (1.30=setup[0.54]+cmd[0.01,0.75] seconds)
      py311: OK (1.16=setup[0.38]+cmd[0.01,0.76] seconds)
      py312: OK (1.79=setup[0.42]+cmd[0.01,1.36] seconds)
      py313: OK (1.07=setup[0.34]+cmd[0.01,0.71] seconds)
      py314: OK (1.28=setup[0.42]+cmd[0.01,0.85] seconds)
      py313t: OK (1.51=setup[0.44]+cmd[0.01,1.05] seconds)
      py314t: OK (1.34=setup[0.44]+cmd[0.01,0.89] seconds)
      congratulations :) (9.48 seconds)

.. versionchanged:: tox≥4.25.0
   Before tox 4.25.0 dated 27 March 2025, the versions had to be specified one
   by one:

   .. code-block:: ini

      [tox]
      envlist = py3{10,11,12,13,14,13t,14t}

Running Tox environments in parallel
------------------------------------

In the previous example, the different environments were executed one after the
other. It is also possible to run them in parallel with the ``-p`` option:

.. code-block:: pytest

   $ uv run tox -p
   py311: OK ✔ in 1.7 seconds
   py310: OK ✔ in 1.8 seconds
   py313: OK ✔ in 1.8 seconds
   py314t: OK ✔ in 1.89 seconds
   py314: OK ✔ in 1.91 seconds
   py313t: OK ✔ in 2.24 seconds
     py310: OK (1.80=setup[0.62]+cmd[0.02,1.16] seconds)
     py311: OK (1.70=setup[0.54]+cmd[0.02,1.15] seconds)
     py312: OK (2.28=setup[0.58]+cmd[0.01,1.69] seconds)
     py313: OK (1.80=setup[0.60]+cmd[0.02,1.18] seconds)
     py314: OK (1.91=setup[0.62]+cmd[0.02,1.28] seconds)
     py313t: OK (2.24=setup[0.72]+cmd[0.02,1.51] seconds)
     py314t: OK (1.89=setup[0.61]+cmd[0.02,1.26] seconds)
     congratulations :) (2.33 seconds)

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
   :emphasize-lines: 11-

   [tox]
   envlist =
     py3{10-14}
     py3{13-14}t
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
the :file:`pyproject.toml` file to tell Coverage which source code paths should
be considered identical:

.. code-block:: toml

   [tool.coverage.paths]
   source = ["src", ".tox/py*/**/site-packages"]

The items source code is initially located in :file:`src/items/` before tox
creates the virtual environments and installs items in the environment. It is
then located in :file:`.tox/py313/lib/python3.13/site-packages/items`, for
example.

.. code-block:: console
   :emphasize-lines: 1

   $ uv run tox
   ...
   Name    Stmts   Miss Branch BrPart  Cover   Missing
   ---------------------------------------------------
   TOTAL     540      0     32      0   100%

   33 files skipped due to complete coverage.
     py310: OK (1.10=setup[0.44]+cmd[0.01,0.64] seconds)
     py311: OK (0.98=setup[0.31]+cmd[0.01,0.66] seconds)
     py312: OK (1.59=setup[0.34]+cmd[0.01,1.24] seconds)
     py313: OK (1.06=setup[0.34]+cmd[0.01,0.71] seconds)
     py314: OK (1.10=setup[0.35]+cmd[0.01,0.74] seconds)
     py313t: OK (1.36=setup[0.40]+cmd[0.01,0.95] seconds)
     py314t: OK (1.31=setup[0.44]+cmd[0.01,0.86] seconds)
     coverage-report: OK (1.55=setup[0.37]+cmd[1.08,0.10] seconds)
     congratulations :) (10.09 seconds)

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
:term:`parameters <Parameter>` can be passed to pytest:

.. code-block:: ini
   :emphasize-lines: 15-

   [tox]
   envlist =
       pre-commit
       docs
       py3{10-14}
       py3{13-14}t
       coverage-report
   skip_missing_interpreters = True

   [testenv]
   dependency_groups = tests
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

   $ uv run tox -e py313 -- -k test_version --no-cov
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
          name: Ensure 100% test coverage
          runs-on: ubuntu-latest
          needs: tests
          if: always()

          steps:
            - uses: actions/checkout@v4
              with:
                persist-credentials: false
            - uses: actions/setup-python@v5
              with:
                python-version-file: .python-version
            - uses: hynek/setup-cached-uv@v2

            - name: Download coverage data
              uses: actions/download-artifact@v4
              with:
                pattern: coverage-data-*
                merge-multiple: true

            - name: Combine coverage and fail if it’s <100%.
              run: |
                uv tool install coverage

                coverage combine
                coverage html --skip-covered --skip-empty

                # Report and write to summary.
                coverage report --format=markdown >> $GITHUB_STEP_SUMMARY

                # Report again and fail if under 100%.
                coverage report --fail-under=100

   ``name``
       can be any name. It is displayed in the GitHub Actions user interface.
   ``steps``
       is a list of steps. The name of each step can be arbitrary and is
       optional.
   ``uses: actions/checkout@v4``
       is a GitHub actions tool that checks out our repository so that the rest
       of the workflow can access it.
   ``uses: actions/setup-python@v5``
       is a GitHub actions tool that configures Python and installs it in a
       build environment.
   ``with: python-version: ${{ matrix.python }}``
       says that an environment should be created for each of the Python
       versions listed in ``matrix.python``.
   ``uses: hynek/setup-cached-uv@v2``
       uses :term:`uv` in GitHub Actions.

       .. seealso::
          * `setup-cached-uv <https://github.com/hynek/setup-cached-uv>`_

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
page. The documentation also shows you how to run pytest directly without tox
and how to extend the matrix to multiple operating systems. As soon as you have
set up your :file:`*.yml` file and uploaded it to your GitHub repository, it
will be executed automatically. You can then see the runs in the
:menuselection:`Actions` tab:

.. figure:: github-actions.png
   :alt: Screenshot of the GitHub actions overview

The different Python environments are listed on the left-hand side. If you
select one, the results for this environment are displayed, as shown in the
following screenshot:

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
default behaviour. Pluggy finds a plugin by searching for an entry point with
the name ``tox``, for example in a :file:`pyproject.toml` file:

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
You should also use the dependency_groups configuration in such environments
to instruct ``uv`` to install the specified dependency group, for example:

.. code-block:: ini
   :caption: tox.ini

   [testenv]
   runner = uv-venv-lock-runner
   dependency_groups = dev
   commands = pytest

``dev`` uses the ``uv-venv-lock-runner`` and uses ``uv sync`` to install
dependencies in the environment with the ``dev`` dependency group.
