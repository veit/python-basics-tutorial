tox
===

`tox <https://tox.readthedocs.io/>`_ is a tool for automating virtualenv environment
management and testing with multiple interpreter configurations.

.. seealso::
   * `tox plugins <https://tox.readthedocs.io/en/latest/plugins.html>`_

#. Installation

   .. tab:: Linux/MacOS

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

   #. Optionally create a Python package with

      .. code-block:: console

           $ pipenv run python setup.py sdist

   #. Creating the environments specified in ``envlist``

      In each of these environments,

      #. the dependencies and packages are installed
      #. the ``commands`` are executed

   #. Create a report with the results from each of the environments, for example:

      .. code-block:: text

           ____________________ summary ____________________
           py27: commands succeeded
           ERROR:   py36: commands failed

   .. seealso::

      * `Examples <https://tox.readthedocs.io/en/latest/examples.html>`_

GitHub Actions
--------------

If your project is hosted on GitHub, you can use `GitHub <https://github.com/>`_
actions to automatically run your tests in different environments. There are a
number of environments available for GitHub actions:
github.com/actions/virtual-environments.

To create a GitHub Action in your project, click :menuselection:`Actions --> set
up a workflow yourself`. This will usually create a
:file:`.github/workflows/main.yml` file.

Give this file a more descriptive name. We usually use :file:`ci.yml`, where
``ci`` stands for `Continuous Integration
<https://en.wikipedia.org/wiki/Continuous_integration>`_.

The pre-filled YAML file is not very useful for our purposes. You can replace
the text, for example with:

   .. code-block:: yaml

      name: CI
      on:
        push:
          branches: ["main"]
        pull_request:
          branches: ["main"]
        workflow_dispatch:
      jobs:
        tests:
          name: "Python ${{ matrix.python-version }}"
          runs-on: "ubuntu-latest"
          env:
            USING_COVERAGE: '3.6,3.8'
          strategy:
            matrix:
              python-version: ["3.6", "3.7", "3.8"]
          steps:
            - uses: "actions/checkout@v2"
            - uses: "actions/setup-python@v2"
              with:
                python-version: "${{ matrix.python-version }}"
            - name: "Install dependencies"
              run: |
                set -xe
                python -VV
