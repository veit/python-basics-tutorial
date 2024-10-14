GitLab Package Registry
=======================

You can also publish your distribution packages in the package registry of your
GitLab project and use them with both :term:`Pip` and :term:`twine`.

.. seealso::
   `PyPI packages in the Package Registry
   <https://docs.gitlab.com/ee/user/packages/pypi_repository/#publish-a-pypi-package-by-using-twine>`_

Authentication
--------------

To authenticate to the GitLab Package Registry, you can use one of the following
methods:

* A :ref:`personal access token <personal-access-tokens>` with the scope
  ``api``.
* A :ref:`deploy token <deploy-tokens>` with the scopes
  ``read_package_registry``, ``write_package_registry`` or both.
* A :ref:`CI job token. <ci-job-token>`.

.. _personal-access-tokens:

… with a personal access token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To authenticate yourself with a personal access token, you can add the following
to the :file:`~/.pypirc` file, for example:

.. code-block:: ini

    [distutils]
    index-servers=
        gitlab

    [gitlab]
    repository = https://ce.cusy.io/api/v4/projects/{PROJECT_ID}/packages/pypi
    username = {NAME}
    password = {YOUR_PERSONAL_ACCESS_TOKEN}

.. _deploy-tokens:

… with a deploy token
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ini

    [distutils]
    index-servers =
        gitlab

    [gitlab]
    repository = https://ce.cusy.io/api/v4/projects/{PROJECT_ID}/packages/pypi
    username = {DEPLOY_TOKEN_USERNAME}
    password = {DEPLOY_TOKEN}

.. _ci-job-token:

… with a job token
~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    image: python:latest

    - name: Setup cached uv
      uses: hynek/setup-cached-uv@v2
    - name: Create venv and install twine
      run: |
        uv venv
        echo "$PWD/.venv/bin" >> $GITHUB_PATH
        uv add --upgrade twine
    - name: Build
      run: |
        uv build
    - name: Retrieve and publish
      - TWINE_PASSWORD=${CI_JOB_TOKEN} TWINE_USERNAME=gitlab-ci-token python -m twine upload --repository-url ${CI_API_V4_URL}/projects/${CI_PROJECT_ID}/packages/pypi dist/*

… for access to packages within a group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the :samp:`{GROUP_URL}` instead of the :samp:`{PROJECT_ID}`.

Publishing the distribution package
-----------------------------------

You can publish your package with the help of :term:`twine`:

.. code-block:: console

    $ uv run twine upload -r gitlab dist/*

.. note::
   If you try to publish a package that already exists with the same name and
   version, you will get the error ``400 Bad Request``; you will have to delete
   the existing package first.

Installing the package
----------------------

You can install the latest version of your package for example with

.. code-block:: console

   uv add -i https://{NAME}:{PERSONAL_ACCESS_TOKEN}@ce.cusy.io/api/v4/projects/{PROJECT_ID}/packages/pypi/simple --no-deps {PACKAGE_NAME}

… or from the group level with

.. code-block:: console

   uv add -i https://{NAME}:{PERSONAL_ACCESS_TOKEN}@ce.cusy.io/api/v4/groups/{GROUP_ID}/-/packages/pypi/simple --no-deps {PACKAGE_NAME}

… or in the :file:`pyproject.toml` file with

.. code-block:: toml
   :caption: pyproject.toml

   [tool.uv]
   extra-index-url = ["https://ce.cusy.io/api/v4/projects/{PROJECT_ID}/packages/pypi/simple {PACKAGE_NAME}"]
