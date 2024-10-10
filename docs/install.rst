Installation
============

Installing Python can be easy. The first step is to download the latest version
from `www.python.org/downloads <https://www.python.org/downloads/>`_. The
tutorial is based on Python 3.13.0, but if you have Python 3.8 or newer
installed, this should not be a problem.

.. tab:: Linux

   Python is already included in the `Linux Standard Base
   <https://wiki.linuxfoundation.org/lsb/start>`_. However, most Linux
   distributions do not want to have anything to do with the language-specific
   package manager, but want to manage everything via ``rpm``/``deb`` or
   similar. package managers :abbr:`etc (et cetera)`. They also don’t want their
   packages to be used for anything other than system purposes. You should
   therefore install your own Python. Under Ubuntu, for example, you can do this
   with:

   .. code-block:: console

      $ wget https://www.python.org/ftp/python/3.12.4/Python-3.13.0.tgz
      $ tar xf Python-3.13.0.tgz
      $ cd Python-3.13.0
      $ ./configure --enable-optimizations
      $ sudo make altinstall

   .. warning::
      One disadvantage is that you have to return to the website regularly to
      check for security updates as there is no integrated auto-updater.

   If older Python versions are required, for example to test libraries with
   :doc:`test/tox`, we use `deadsnakes
   <https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa>`_.

.. tab:: macOS

   You can obtain Python directly from https://www.python.org/downloads/macos/.
   The ``universal2`` installers also run on Intel-based environments.

   One disadvantage is that you have to return to the website regularly to check
   for security updates, as there is no integrated auto-updater. Alternatively,
   you can install `MOPUp <https://pypi.org/project/MOPUp/>`_ with ``python -m
   pip install MOPUp`` and then regularly call ``mopup`` to get the latest
   version of your Python installation.

   If older Python versions are required, for example to test libraries with
   :doc:`test/tox`, `python-build-standalone
   <https://gregoryszorc.com/docs/python-build-standalone/main/building.html#macos>`_
   can be used.

.. tab:: Windows

   Python can be installed for most Windows versions after Windows 7 with the
   Python installer in three steps:

   #. Download the latest Python Releases for Windows installer, for example
      `Windows installer (64-bit)
      <https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe>`_.
   #. Start the installation programme. If you have the necessary
      authorisations, install Python with the option *Install launcher for all
      users*. This should install Python in
      :file:`C:\\Program Files\\Python313-64`. In addition, *Add Python 3.13 to
      PATH* should be activated so that this path to the Python installation is
      also entered in the list of ``PATH`` environment variables.
   #. Finally, you can now check the installation by entering the following in
      the command prompt:

      .. code-block:: ps1con

         C:\> python -V
         Python 3.13.0

      .. warning::
         One disadvantage is that you have to return to the website regularly to
         check for security updates, as there is no integrated auto-updater.

.. tip::
   `direnv <https://direnv.net>`_ allows you to set environment variables
   depending on the directory. This allows you to install environment variables
   from `The twelve-factor apps <https://12factor.net>`_ and project-specific
   environments as well as providing secrets for deployment.
