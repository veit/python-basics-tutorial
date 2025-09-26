Apps
====

App projects are suitable for web servers, scripts and :abbr:`CLI (command line
interfaces)`. We can also create them with ``uv init --package``:

.. code-block:: console

   $ uv init --package myapp
   $  tree myapp -a
   myapp
   ├── .git
   │   └── ...
   ├── .gitignore
   ├── .python-version
   ├── README.md
   ├── pyproject.toml
   └── src
       └── myapp
           └── __init__.py

.. note::
   I strongly believe that a Python application should be properly packaged to
   enjoy the many benefits, such as

   * source management with :doc:`importlib <python3:library/importlib>`
   * executable scripts with ``project.scripts`` instead of attached
     :file:`scripts` folders
   * the benefits of :file:`src` layout with a common, documented and well
     understood structure.

:file:`myapp/pyproject.toml`
    The :file:`pyproject.toml` file contains a ``scripts`` entry point
    ``myapp:main``:

    .. literalinclude:: myapp/pyproject.toml
       :caption: myapp/pyproject.toml
       :lines: 12-13

:file:`myapp/src/myapp/__init__.py`
    The module defines a CLI function :func:`main`:

    .. literalinclude:: myapp/src/myapp/__init__.py
       :caption: myapp/src/myapp/__init__.py

    It can be called up with ``uv run``:

    .. code-block:: console

       $ uv run mypack
       Hello from myapp!

    Alternatively, you can also build a :ref:`virtual environment <venv>` and
    then call :func:`main` from Python:

    .. code-block:: pycon

       $  uv add .
       Resolved 1 package in 1ms
       Audited in 0.01ms
       $ uv run python
       >>> import myapp
       >>> myapp.main()
       Hello from myapp!

.. _uv_lock:

:file:`uv.lock` file
    With ``uv add .`` the :file:`uv.lock` file was also created alongside the
    :file:`pyproject.toml` file. :file:`uv.lock` is a cross-platform lock file
    that records the packages that are to be installed across all possible
    Python features such as operating system, architecture and Python version.

    Unlike :file:`pyproject.toml`, which specifies the general requirements of
    your project, :file:`uv.lock` contains the exact resolved versions that are
    installed in the project environment. This file should be checked into the
    :doc:`Git <Python4DataScience:productive/git/index>` version control system
    to enable consistent and reproducible installations on different computers.

    .. literalinclude:: myapp/uv.lock
       :caption: myapp/uv.lock

    :file:`uv.lock` is a human-readable
    :doc:`Python4DataScience:data-processing/serialisation-formats/toml/index`
    file, but is managed by ``uv`` and should not be edited manually.

    .. note::
       If ``uv`` is to be integrated into other tools or workflows, you can
       export the content to the `requirements file format
       <https://pip.pypa.io/en/stable/reference/requirements-file-format/>`_
       using :samp:`uv export --format requirements-txt > {CONSTRAINTS.TXT}`.
       Conversely, the :samp:`{CONSTRAINTS.TXT}` file created can then be used
       with ``uv pip install`` or other tools.

.. _reproduce-virtual-env:

Reproducing the Python environment
----------------------------------

In production environments, you should always use exactly the versions that have
been tested. You can use ``uv sync --locked`` in your environment to ensure that
the :file:`uv.lock` file matches the project metadata. Otherwise an error
message will be displayed.

You can then use ``uv sync --frozen`` in the production environment to ensure
that the versions of  :file:`uv.lock` are used as the source of truth, but if
the  :file:`uv.lock` file is missing in the production environment, ``uv sync
--frozen`` will terminate with an error. Finally, changes to dependencies in the
:file:`pyproject.toml` file are ignored if they are not yet written to the
:file:`uv.lock` file.

If you want to use ``uv run`` in a productive environment, the ``--no-sync``
option prevents the environment from being updated.

.. _update-uv-lock:

Updating the Python environment
-------------------------------

By default, ``uv`` favours the locked versions of the packages when executing
``uv sync`` and ``uv lock``. Package versions are only changed if the dependency
conditions of the project exclude the previous, locked version.

With ``uv lock --upgrade`` you can upgrade all packages and with :samp:`uv lock
--upgrade-package {PACKAGE}=={VERSION}` you can upgrade individual packages to a
specific version.

.. tip::
   You can also use the
   :doc:`Python4DataScience:productive/git/advanced/hooks/pre-commit` to
   regularly update your :file:`uv.lock` file:

   .. code-block:: yaml
      :caption: .pre-commit-config.yaml

      - repo: https://github.com/astral-sh/uv-pre-commit
        rev: 0.5.21
        hooks:
          - id: uv-lock

Restrict platform and Python versions
-------------------------------------

If your project only supports a limited number of platforms or Python versions,
you can do this in the :file:`pyprojects.toml` file :pep:`508` compliant, for
example to restrict your project to macOS and Linux only you can add the
following section in your :file:`pyproject.toml` file:

.. code-block:: toml

   [tool.uv]
   environments = [
       "sys_platform == 'darwin'",
       "sys_platform == 'linux'",
   ]
