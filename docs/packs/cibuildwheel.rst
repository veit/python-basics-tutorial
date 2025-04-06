``cibuildwheel``
================

:term:`cibuildwheel` simplifies the creation of :term:`Python Wheels <wheel>`
for the different platforms and Python versions through Continuous Integration
(CI) workflows. More precisely it builds manylinux, macOS 10.9+, and Windows
wheels for CPython and PyPy with GitHub Actions, Azure Pipelines, Travis CI,
AppVeyor, CircleCI, or
:doc:`Python4DataScience:productive/git/advanced/gitlab/ci-cd/index`.

In addition, it bundles shared library dependencies on Linux and macOS through
`auditwheel <https://github.com/pypa/auditwheel>`_ and `delocate
<https://github.com/matthew-brett/delocate>`_.

Finally, the tests can also run against the wheels.

.. seealso::
   * `Docs <https://cibuildwheel.pypa.io/>`_
   * `GitHub <https://github.com/pypa/cibuildwheel>`_

.. _cibuildwheel-in-gitlab-ci: GitLab CI/CD

.. tab:: GitHub Actions

    To build Linux, macOS, and Windows wheels, create a
    :file:`.github/workflows/build_wheels.yml` file in your GitHub repo:

    .. literalinclude:: .github/workflows/build_wheels.yml
       :caption: .github/workflows/build_wheels.yml
       :language: yaml
       :lines: 1-7

    ``workflow_dispatch``
        allows you to click a button in the graphical user interface to trigger
        a build. This is perfect for manually testing wheels before a release,
        as you can easily download them from *artifacts*.

        .. seealso::
           * `workflow_dispatch
             <https://github.blog/changelog/2020-07-06-github-actions-manual-triggers-with-workflow_dispatch/>`_

    ``release``
        is executed when a tagged version is transferred.

        .. seealso::
           * `release
             <https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#release>`_

    Now the :term:`wheels <wheel>` can be built with:

    .. literalinclude:: .github/workflows/build_wheels.yml
       :language: yaml
       :lines: 9-22

    This runs the CI workflow with the following default settings:

    * ``package-dir: .``
    * ``output-dir: wheelhouse``
    * ``config-file: "{package}/pyproject.toml"``

    .. seealso::
       * `Workflow syntax for GitHub Actions
         <https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions>`_

    Now you can finally upload the artefacts of both jobs to the :term:`PyPI`:

    .. literalinclude:: .github/workflows/build_wheels.yml
       :language: yaml
       :lines: 24-

.. tab:: GitLab CI/CD

    To build wheels for Linux, macOS, and Windows with
    :doc:`Python4DataScience:productive/git/advanced/gitlab/ci-cd/index`,
    create a :file:`.gitlab-ci.yml` file in your repository:

    .. literalinclude:: .gitlab-ci.yml
       :language: yaml

    .. seealso::
       * `Keyword reference for the .gitlab-ci.yml file
         <https://docs.gitlab.com/ee/ci/yaml/>`_

Options
-------

``cibuildwheel`` can be configured either via environment variables or via a
configuration file such as :file:`pyproject.toml`, for example:

.. literalinclude:: pyproject.toml
   :language: toml

.. seealso::
   * `cibuildwheel: Options
     <https://cibuildwheel.pypa.io/en/stable/options/>`_

Examples
--------

* Coverage.py: `.github/workflows/kit.yml <https://github.com/nedbat/coveragepy/blob/master/.github/workflows/kit.yml>`_
* matplotlib: `.github/workflows/cibuildwheel.yml <https://github.com/matplotlib/matplotlib/blob/main/.github/workflows/cibuildwheel.yml>`_
* MyPy: `.github/workflows/build.yml
  <https://github.com/mypyc/mypy_mypyc-wheels/blob/master/.github/workflows/build.yml>`__
* psutil: `.github/workflows/build.yml
  <https://github.com/giampaolo/psutil/blob/master/.github/workflows/build.yml>`__
