tox
===

`tox <https://tox.readthedocs.io/>`_ is a tool for automating virtualenv environment
management and testing with multiple interpreter configurations.

.. seealso::
   * `tox plugins <https://tox.readthedocs.io/en/latest/plugins.html>`_

#. Installation

   .. tab:: Linux/macOS

      .. code-block:: console

         $ bin/python -m pip install tox

   .. tab:: Windows

      .. code-block:: ps1con

         C:> Scripts\python -m pip install tox

#. Configuration

   With tox you can configure complex multi-parameter test matrices via a simple
   configuration file in the `INI <https://en.wikipedia.org/wiki/INI_file>`_ style,
   for example:

   .. literalinclude:: tox.ini
      :language: ini
      :lineno-start: 1

#. Execute

   The following steps are then run through with ``bin/tox``:

   #. Creating the environments specified in :envvar:`envlist`:

      In each of these environments, the dependencies and packages are then
      installed.

   #. Create a report with the results from each of the environments, for example:

      .. code-block:: text

           ____________________ summary ____________________
           ERROR:   py37: commands failed
           py38: commands succeeded
           py39: commands succeeded
           py310: commands succeeded
           py311: commands succeeded

GitHub Actions
--------------

If your project is hosted on `GitHub <https://github.com/>`_, you can use GitHub
actions to automatically run your tests in different environments. There are a
number of environments available for GitHub actions:
`github.com/actions/virtual-environments
<https://github.com/actions/virtual-environments/#readme>`_.

#. To create a GitHub Action in your project, click :menuselection:`Actions -->
   set up a workflow yourself`. This will usually create a
   :file:`.github/workflows/main.yml` file.
#. Give this file a more descriptive name. We usually use :file:`ci.yml`, where
   ``ci`` stands for `continuous integration
   <https://en.wikipedia.org/wiki/Continuous_integration>`_.
#. The pre-filled YAML file is not very useful for our purposes. You can replace
   the text, for example with:

   .. literalinclude:: ci.yaml
      :language: yaml
      :lines: 1-45
      :lineno-start: 1

   .. note::
      If necessary, adjust the Python versions in :envvar:`python-version`.
      However, you do not need to change the environment variable in
      :envvar:`USING_COVERAGE` as well, as this is done by the tox plugin
      ``tox-gh-actions`` (see below).

#. Then you can click on :guilabel:`Start commit`. Since we want to make further
   changes before the tests are executed automatically, we choose
   :guilabel:`Create a new branch for this commit and start a pull request` and
   as name for the new :term:`Branch <branch>` ``github-actions``. Finally you
   can click on :guilabel:`Create pull request`.
#. To switch to the new branch, we go to :menuselection:`Code --> main -->
   github-actions`.
#. `tox-gh-actions <https://pypi.org/project/tox-gh-actions/>`_ simplifies
   running tox in GitHub actions by providing the environment for the tests as
   the one tox itself uses. However, for this we still need to adapt our
   :file:`tox.ini` file, for example:

   .. literalinclude:: tox.ini
      :language: ini
      :lines: 15-
      :lineno-start: 15

   This maps GitHub actions to tox environments.

   .. note::
      * Not all variants of your environment need to be specified. This
        distinguishes ``tox-gh-actions`` from ``tox -e py``.
      * Make sure that the versions in the ``[gh-actions]`` section match the
        available Python versions and, if applicable, those in the :ref:`GitHub
        actions for Git pre-commit hooks <gh-action-pre-commit-example>`.
      * Since all tests for a specific Python version are executed one after the
        other in a container, the advantages of parallel execution are lost
        here.

   .. seealso::
      * `Building and testing Python
        <https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python>`_
      * `Workflow syntax for GitHub Actions
        <https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions>`_

#. Now you can add a badge of your CI status in your :file:`README.rst` file,
   for example with:

   .. code-block::

    .. image:: https://github.com/YOU/YOUR_PROJECT/workflows/CI/badge.svg?branch=main
         :target: https://github.com/YOU/YOUR_PROJECT/actions?workflow=CI
         :alt: CI Status

#. You can publish the test coverage on GitHub, see :ref:`Coverage GitHub
   actions <coverage-github-actions>`.
#. You can also display a badge for the code coverage in your :file:`README.rst`
   file, see :ref:`Coverage badge <coverage-badge>`.
