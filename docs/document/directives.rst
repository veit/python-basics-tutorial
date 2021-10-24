Directives
==========

reStructuredText can be expanded with `Directives
<https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_.
Sphinx makes extensive use of this. Here are some examples:

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2

   start
   docstrings

.. code-block:: rest

   .. toctree::
      :maxdepth: 2

      start
      docstrings

Meta information
~~~~~~~~~~~~~~~~

.. sectionauthor:: Veit Schiele <veit@cusy.io>
.. codeauthor:: Veit Schiele <veit@cusy.io>

.. code-block:: rest

   .. sectionauthor:: Veit Schiele <veit@cusy.io>
   .. codeauthor:: Veit Schiele <veit@cusy.io>

See also
~~~~~~~~

.. seealso::
    `Sphinx Directives
    <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_

.. code-block:: rest

   .. seealso::
       `Sphinx Directives
       <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_

Glossary
~~~~~~~~

.. glossary::

   environment
       A structure where information about all documents under the root is
       saved, and used for cross-referencing.  The environment is pickled
       after the parsing stage, so that successive runs only need to read
       and parse new and changed documents.

   source directory
       The directory which, including its subdirectories, contains all
       source files for one Sphinx project.

.. code-block:: rest

   .. glossary::

      environment
          A structure where information about all documents under the root is
          saved, and used for cross-referencing.  The environment is pickled
          after the parsing stage, so that successive runs only need to read
          and parse new and changed documents.

      source directory
          The directory which, including its subdirectories, contains all
          source files for one Sphinx project.
