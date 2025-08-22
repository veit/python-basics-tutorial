Adding more Python libraries
============================

Although Python’ :doc:`batteries` philosophy means that you can already do a lot
with the default installation of Python, there will inevitably come a situation
where you need functionality that is not included in Python.

If you need a third-party module that is not pre-built for your platform, you
must use its source distribution. However, this causes two problems:

* To install the source distribution, you need to find and download it.
* Certain Python paths and authorisations of your system are expected.

Python offers :ref:`pip` as a current solution for both problems. ``pip`` tries
to find the module in the :term:`Python Package Index` (:term:`PyPI`), downloads
it and all dependencies and takes care of the installation. You can also call
:term:`pypi.org` directly and search for packages or filter the packages by
category.

.. warning::
   Never install anything with ``pip`` into the global Python, not even with the
   ``--user`` flag. Always use :ref:`venv`. This way you avoid contaminating
   your Python installation with libraries that you install and then forget
   about. Every time you need to do something new, you should create a new
   virtual environment. This will also avoid library conflicts between different
   projects.

.. tip::
   We recommend that you configure ``pip`` so that it is not possible to install
   Python packages globally. To do this, you can enter the following in your
   :file:`~/.config/pip/pip.conf`:

   .. code-block:: ini

      [global]
      require-virtualenv = true

.. _venv:

``venv``
--------

A virtual environment (``virtualenv``) is a self-contained directory structure
that contains both an installation of Python and the additional packages. Since
the entire Python environment is contained in this directory, the libraries and
modules installed there cannot collide with those in the main system or in other
virtual environments, so that different applications can use different versions
of Python and its packages. Creating and using a virtual environment is a
two-step process:

#. First we create a project directory and then the virtual environment in it:

   .. tab:: Linux/macOS

      .. code-block:: console

         $ mkdir myproj
         $ cd myproj
         $ python3 -m venv .venv

   .. tab:: Windows

      .. code-block:: ps1

         > mkdir myproj
         > cd myproj
         > py -m venv .venv

   This creates the environment with Python and :term:`pip` in a directory
   called :samp:`.venv`.

#. You can then activate this environment so that the next time you call
   ``python``, it will use the Python from your new environment:

   .. tab:: Linux/macOS

      .. code-block:: console

         $ . .venv/bin/activate

   .. tab:: Windows

      .. code-block:: ps1

         > .venv\Scripts\activate

#. Install Python packages only for this virtual environment, for example the
   popular ``pandas`` library:

   .. tab:: Linux/macOS

      .. code-block:: console

         (.venv) $ python -m pip install pandas

   .. tab:: Windows

      .. code-block:: ps1

         (.venv) > python.exe -m pip install pandas

#. If you want to finish your work on this project, you can deactivate the
   virtual environment again with

   .. tab:: Linux/macOS

      .. code-block:: console

         (.venv) $ deactivate

   .. tab:: Windows

      .. code-block:: ps1

         (.venv) > deactivate

.. seealso::
   * :doc:`python3:tutorial/venv`

.. _pip:

``pip``
-------

The basic syntax of ``pip`` is quite simple:

.. code-block:: console

   $ python -m pip install pandas

If you want to specify a particular version of a package, you can simply append
the version numbers:

.. code-block:: console

   $ python -m pip install pandas==2.2.2

or

.. code-block:: console

   $ python -m pip install "pandas>=2"

Proxy server
~~~~~~~~~~~~

To install Python packages via a proxy server, you can enter the following:

:samp:`python -m pip install --proxy
http://{USER_NAME}{:{PASSWORD}}@{PROXYSERVER_NAME}:{PORT} {PKG_NAME}`

You can also save the proxy server permanently as an environment variable:

.. tab:: Linux

   for example in the :file:`~/.bashrc` with:

   .. code-block:: bash

      export HTTP_PROXY=http://{USER_NAME}:{PASSWORD}@{PROXYSERVER_NAME}:{PORT}

.. tab:: Windows

   Add the following line to the environment variables:

   .. code-block:: ps1

      set HTTP_PROXY={PROXYSERVER_NAME}:{PORT}

Pinning the version numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~

… of packages
:::::::::::::

For a stable environment, it makes sense to specify the version numbers of the
dependencies.

.. tip::
   In none of our library projects does so much happen that the :doc:`Git
   history  <Python4DataScience:productive/git/review>` should mainly consist of
   updates. We only restrict the version numbers to be used in the event of
   problems. For apps, however, we specify the version numbers.

We use `PDM <https://pdm-project.org/en/latest>`_ to specify the versions for
our applications and maintain cross-platform lock files. PDM also supports the
management of virtual environments with ``pdm venv activate``.

… of Python
:::::::::::

In contrast to applications, our packages usually support more than one Python
version. Nevertheless, we usually add the current standard version in
:file:`.python-version` to :doc:`packages <../packs/distribution>` as well:

.. literalinclude:: ../../.python-version
   :caption: .python-version

The nice thing about this is that we can use the same file in GitHub Actions as
input for `setup-python <https://github.com/actions/setup-python>`_:

.. literalinclude:: ../../.github/workflows/ci.yml
   :caption: .github/workflows/ci.yml
   :lines: 20-28
   :emphasize-lines: 9

In our :doc:`Python4DataScience:productive/git/advanced/gitlab/ci-cd/index`
pipelines, however, we use ``requires-python`` from the :ref:`pyproject-toml`
file to build :doc:`Docker containers with the appropriate Python version
<Python4DataScience:productive/git/advanced/gitlab/ci-cd/docker>`.

.. _uv:

``uv``
------

:term:`uv` simplifies the creation of an initial project structure and the
management of your dependencies.

Installation
~~~~~~~~~~~~

``uv`` ``uv`` does not depend on Python. Pre-compiled, standalone binaries can
be installed on Linux, macOS and Windows:

.. tab:: Linux/macOS

   .. code-block:: console

      $ curl -LsSf https://astral.sh/uv/install.sh | sh

.. tab:: Windows

   .. code-block:: ps1

      > powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

``uv``  updates itself regularly with this installation.

Automatic shell completion
~~~~~~~~~~~~~~~~~~~~~~~~~~

To activate automatic shell completion for ``uv`` commands, carry out one of the
following steps:

.. tab:: Linux/macOS

   Specify your shell, for example with ``echo $SHELL``, then execute one of the
   following commands:

   .. code-block:: console

      $ echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
      $ echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
      $ echo 'uv generate-shell-completion fish | source' >> ~/.config/fish/config.fish
      $ echo 'eval (uv generate-shell-completion elvish | slurp)' >> ~/.elvish/rc.elv

.. tab:: Windows

   .. code-block:: ps1

      Add-Content -Path $PROFILE -Value '(& uv generate-shell-completion powershell) | Out-String | Invoke-Expression'
      Add-Content -Path $PROFILE -Value '(& uvx --generate-shell-completion powershell) | Out-String | Invoke-Expression'

Then restart the shell or call up ``source`` with your shell configuration file.

Update
~~~~~~

You can easily update uv with:

.. code:: console

   $ uv self update
   info: Checking for updates...
   success: Upgraded uv from v0.8.12 to v0.8.13! https://github.com/astral-sh/uv/releases/tag/0.8.13

Python installation
~~~~~~~~~~~~~~~~~~~

With ``uv`` not only older CPython versions can be installed, but also, for
example, `PyPy <https://pypy.org>`_ with  ``uv python install pypy@3.12`` or
free-threaded Python 3.13 with  ``uv python install --python-preference
only-managed 3.13t``.

Create project structure
~~~~~~~~~~~~~~~~~~~~~~~~

Depending on whether you want to create a :doc:`library <../packs/distribution>`
or an :doc:`application <../packs/apps>`, ``uv`` can create a suitable project
structure.
