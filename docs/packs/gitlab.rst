GitLab Package Registry
=======================

You can also publish your distribution packages in the package registry of your
GitLab project. However, the following conditions must be met:

* You must `authenticate
  <https://docs.gitlab.com/ee/user/packages/pypi_repository/?tab=With+a+deploy+token#authenticate-with-the-gitlab-package-registry>`_
  yourself when registering the package.
* Your `version information
  <https://docs.gitlab.com/ee/user/packages/pypi_repository/?tab=With+a+deploy+token#use-valid-version-strings>`_
  must be valid.
* The package must be smaller than 5 GB and the description must not be longer than 4000 characters.
* The package has not yet been published in the package registry. Attempting to publish the same version of a package will return ``400 Bad Request``.

You can then use the package with both :term:`pip` and :term:`uv`.

.. seealso::
   `Publish a PyPI package
   <https://docs.gitlab.com/ee/user/packages/pypi_repository/#publish-a-pypi-package>`_

Authentication
--------------

To authenticate to the GitLab Package Registry, you can use one of the following
methods:

* a `personal access token
  <https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html>`_ with
  the scope ``api``.
* a `deploy token
  <https://docs.gitlab.com/ee/user/project/deploy_tokens/index.html>`_ with the
  scopes ``read_package_registry``, ``write_package_registry`` or both.
* a `CI job token <https://docs.gitlab.com/ee/ci/jobs/ci_job_token.html>`_.

.. tab:: personal access token

   .. code-block:: yaml
      :caption: .gitlab-ci.yml
      :emphasize-lines: 5-6

      variables:
        UV_VERSION: 0.5
        PYTHON_VERSION: 3.12
        BASE_LAYER: bookworm-slim
        UV_PUBLISH_USERNAME: <personal_access_token_name>
        UV_PUBLISH_PASSWORD: <personal_access_token>

.. tab:: deploy token

   .. code-block:: yaml
      :caption: .gitlab-ci.yml
      :emphasize-lines: 5-6

      variables:
        UV_VERSION: 0.5
        PYTHON_VERSION: 3.12
        BASE_LAYER: bookworm-slim
        UV_PUBLISH_USERNAME: <deploy_token_username>
        UV_PUBLISH_PASSWORD: <deploy_token>

.. tab:: job token

   .. code-block:: yaml
      :caption: .gitlab-ci.yml
      :emphasize-lines: 5-6

      variables:
        UV_VERSION: 0.5
        PYTHON_VERSION: 3.12
        BASE_LAYER: bookworm-slim
        UV_PUBLISH_USERNAME: <gitlab-ci-token>
        UV_PUBLISH_PASSWORD: $CI_JOB_TOKEN

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
        echo "$PWD/.venv/bin" >> $PATH
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

Now you can publish your package on GitLab with :

.. code-block:: yaml
   :caption: .gitlab-ci.yml

   …
   stages:
     - publish
   uv:
     stage: publish
     image: ghcr.io/astral-sh/uv:$UV_VERSION-python$PYTHON_VERSION-$BASE_LAYER
     script:
       - uv build
       - uv publish --publish-url ${CI_API_V4_URL}/projects/${CI_PROJECT_ID}/packages/pypi dist/*

.. tip::
   If necessary, you can use ``RUST_LOG=uv=trace`` to obtain further information
   on the authentication attempts, for example with ``RUST_LOG=uv=trace uv
   --verbose publish --publish-url
   ${CI_API_V4_URL}/projects/${CI_PROJECT_ID}/packages/pypi dist/*``.

.. seealso::
   In :ref:`uv-gitlab` you will find further instructions on how to configure
   the :file:`.gitlab-ci.yml` file.

Installing the package
----------------------

You can install the latest version of your package for example with

.. code-block:: console

   $ uv add -i https://{NAME}:{PERSONAL_ACCESS_TOKEN}@ce.cusy.io/api/v4/projects/{PROJECT_ID}/packages/pypi/simple --no-deps {PACKAGE_NAME}

… or from the group level with

.. code-block:: console

   $ uv add -i https://{NAME}:{PERSONAL_ACCESS_TOKEN}@ce.cusy.io/api/v4/groups/{GROUP_ID}/-/packages/pypi/simple --no-deps {PACKAGE_NAME}

… or in the :file:`pyproject.toml` file with

.. code-block:: toml
   :caption: pyproject.toml

   [tool.uv]
   extra-index-url = ["https://ce.cusy.io/api/v4/projects/{PROJECT_ID}/packages/pypi/simple {PACKAGE_NAME}"]
