Modules for files
=================

.. _builtin-file-modules:

Built-in modules
----------------

The Python standard library contains a number of built-in modules that you can
use to manage files:

.. _file-modules:

+-----------------------------------+-------------------------------------------------------------------------------+
| Module                            | Description                                                                   |
+===================================+===============================================================================+
| :py:mod:`os.path`                 | performs common pathname manipulations                                        |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`pathlib`                 | manipulates pathnames                                                         |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`fileinput`               | iterates over multiple input files                                            |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`filecmp`                 | compares files and directories                                                |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`tempfile`                | creates temporary files and directories                                       |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`glob`,                   | use UNIX-like path and file name patterns                                     |
| :py:mod:`fnmatch`                 |                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`linecache`               | randomly accesses lines of text                                               |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`shutil`                  | performs higher level file operations                                         |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`mimetypes`               | Assignment of file names to MIME types                                        |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`pickle`,                 | enable Python object serialisation and persistence, see also                  |
| :py:mod:`shelve`                  | :doc:`../save-data/pickle`                                                    |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`csv`                     | reads and writes CSV files                                                    |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`json`                    | JSON encoder and decoder                                                      |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`sqlite3`                 | provides a DB-API 2.0 interface for SQLite databases, see also                |
|                                   | :doc:`../save-data/sqlite/index`                                              |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`xml`,                    | reads and writes XML files, see also R:doc:`../save-data/xml`                 |
| :py:mod:`xml.parsers.expat`,      |                                                                               |
| :py:mod:`xml.dom`,                |                                                                               |
| :py:mod:`xml.sax`,                |                                                                               |
| :py:mod:`xml.etree.ElementTree`   |                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`html.parser`,            | Parsing HTML and XHTML                                                        |
| :py:mod:`html.entities`           |                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`configparser`            | reads and writes Windows-like configuration files (``.ini``)                  |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`base64`,                 | encodes/decodes files or streams                                              |
| :py:mod:`binascii`,               |                                                                               |
| :py:mod:`quopri`,                 |                                                                               |
| :py:mod:`uu`                      |                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`struct`                  | reads and writes structured data to and from files                            |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`zlib`,                   | for working with archive files and compressions                               |
| :py:mod:`gzip`,                   |                                                                               |
| :py:mod:`bz2`,                    |                                                                               |
| :py:mod:`zipfile`,                |                                                                               |
| :py:mod:`tarfile`                 |                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+

.. _end-file-modules:

.. _pandas-io-tools:

pandas IO tools
---------------

* :doc:`Python4DataScience:data-processing/pandas-io`

  Examples of serialisation formats:

  * :doc:`CSV
    <Python4DataScience:data-processing/serialisation-formats/csv/example>`
  * :doc:`JSON
    <Python4DataScience:data-processing/serialisation-formats/json/example>`
  * :doc:`Excel
    <Python4DataScience:data-processing/serialisation-formats/excel>`
  * :doc:`XML/HTML
    <Python4DataScience:data-processing/serialisation-formats/xml-html/index>`
  * :doc:`YAML
    <Python4DataScience:data-processing/serialisation-formats/yaml/example>`
  * :doc:`TOML
    <Python4DataScience:data-processing/serialisation-formats/toml/example>`
  * :doc:`Pickle
    <Python4DataScience:data-processing/serialisation-formats/pickle/pickle-examples>`

Checks
------

* What use cases can you imagine in which the :mod:`python3:struct` module would
  be useful for reading or writing binary data?

  * when reading and writing a binary file
  * when reading from an external interface, where the data should be stored
    exactly as it was transmitted

* Why :doc:`pickle <python3:library/pickle>` may or may not be suitable for the
  following use cases:

  #. Saving some state variables from one run to the next ✅
  #. Storing evaluation results ❌, as pickle is dependent on the respective
     Python version
  #. Saving user names and passwords ❌, as pickles are not secure
  #. Saving a large dictionary with English terms ❌, as the entire pickle would
     have to be loaded into memory
