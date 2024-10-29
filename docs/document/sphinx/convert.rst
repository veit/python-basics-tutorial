Convert
=======

Other file formats can be converted to :doc:`rest` with Pandoc.

Installation of Pandoc
----------------------

`Pandoc <https://pandoc.org/installing.html>`_ is a powerful document conversion
utility. We use it for simple conversions, but it is capable of much more.

Installation
------------

You can install Pandoc for the different platforms:

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $  sudo apt install pandoc

.. tab:: macOS

   .. code-block:: console

      $  brew install pandoc

.. tab:: Windows

   .. code-block:: ps1

      $  choco install pandoc

.. seealso::
   * `Installing pandoc <https://pandoc.org/installing.html>`_

Convert
-------

In the terminal, navigate to the directory containing the documents to be
converted. Then enter the command :samp:`pandoc -s --toc -f {INPUT_FORMAT} -t
rst {MYDOC}.{SUFFIX}`:

``-s``
    creates an independent document
``--toc``
    creates a table of contents (optional)
``-t``
    creates a reStructuredText output
``-f``
    tells Pandoc the input format. You can find an overview of the available
    input formats in `General options
    <https://pandoc.org/MANUAL.html#general-options>`_.

Correcting the converted document
---------------------------------

The extent of the correction for the converted document depends on the file
format you are converting from. Here are a few things you should pay attention
to:

* Multi-line titles must be converted to single-line titles
* Independent ``**`` characters
* :samp:`***BOLD***` should be :samp:`**BOLD**`
* Incorrect tables
