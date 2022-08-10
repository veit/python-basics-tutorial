Installation
============

The installation of Python is simple. The first step is to download the latest
version from `www.python.org/downloads <https://www.python.org/downloads/>`_.
The tutorial is based on Python 3.10, but if you have Python 3.7 or 3.8
installed, that is no problem either.

.. tab:: Linux

   Most Linux distributions have Python already installed. If a precompiled
   version of Python exists in your Linux distribution, I recommend you to use
   it.

.. tab:: macOS

   You need a Python version that matches your macOS and processor. Once you
   have determined the correct version, you can download the image file, mount
   it with a double click and then start the installation programme contained
   in it. Python will then be in the :file:`Applications` folder.

   If you use `Homebrew <https://brew.sh/>`_, you can also install Python in the
   terminal with:

   .. code-block:: console

      $ brew install python3

.. tab:: Windows

   Python can be installed for most Windows versions after Windows 7 with the
   Python installer in three steps:

   #. Download the latest `Python Releases for Windows
      <https://www.python.org/downloads/windows/>`_ installer, for example 
      `Windows installer (64-bit)
      <https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe>`_.
   #. Start the installation programme. If you have the necessary permissions,
      install Python with the option *Install launcher for all users*. This
      should install Python in :file:`C:\\Program Files\\Python310-64`. Also,
      *Add Python 3.10 to PATH* should be activated so that this path to the
      Python installation is also entered in the list of ``PATH`` environment
      variables.
   #. Finally, you can now check the installation by entering the following in
      the command prompt:

      .. code-block:: ps1con

         C:\> python -V
         Python 3.10.6

.. note::
   If Python is already installed on your system, you can easily install your
   own Python. A new version does not replace the old one but is installed in a
   different location.
