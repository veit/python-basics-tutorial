reStructuredText
================

.. code-block:: rest

    Underline the title with punctuation marks
    ==========================================

    Change the punctuation mark for subtitles
    -----------------------------------------

Paragraphs
----------

A paragraph consists of one or more lines of non-indented text, separated
from the material above and below by blank lines.

.. code-block:: rest

   A paragraph consists of one or more lines of non-indented text, separated
   from the material above and below by blank lines.

Inline markup
-------------

*Italic*, **bold** and ``preformatted``

.. code-block:: rest

   *Italic*, **bold** and ``preformatted``

Links
-----

External links
~~~~~~~~~~~~~~

`hyperlink <http://en.wikipedia.org/wiki/Hyperlink>`_ `link`_

.. _link: http://en.wikipedia.org/wiki/Link_(The_Legend_of_Zelda)

.. code-block:: rest

   `hyperlink <http://en.wikipedia.org/wiki/Hyperlink>`_ `link`_

   .. _link: http://en.wikipedia.org/wiki/Link_(The_Legend_of_Zelda)

Internal links
~~~~~~~~~~~~~~

Cross-referencing locations
:::::::::::::::::::::::::::

.. _my-reference-label:

Section to reference
....................

To refer to the section, use :ref:`my-reference-label`.

.. code-block:: rest

   .. _my-reference-label:

   Section to reference
   ....................

   To refer to the section, use :ref:`my-reference-label`.

Referencing documents
:::::::::::::::::::::

Link to :doc:`start page <../index>` or :doc:`docstrings`.

.. code-block:: rest

   Link to :doc:`start page <../index>` or :doc:`docstrings`.

Download documents
::::::::::::::::::

Link to a document, not rendered by Sphinx, for example
:download:`docstrings-example.rst`.

.. code-block:: rest

   Link to a document, not rendered by Sphinx, for example
   :download:`docstrings-example.rst`.

Images
------

.. image:: python-logo.png

.. code-block:: rest

   .. image:: python-logo.png

Other semantic markup
~~~~~~~~~~~~~~~~~~~~~

File listing
::::::::::::

:file:`/Users/{NAME}/python-basics`

.. code-block:: rest

   :file:`/Users/{NAME}/python-basics`

Menu selections and GUI labels
::::::::::::::::::::::::::::::

#. :menuselection:`File --> Save as …`
#. :guilabel:`&Submit`

.. code-block:: rest

   #. :menuselection:`File --> Save as …`
   #. :guilabel:`&Submit`

Lists
-----

Numbered lists
--------------

#. First
#. Second
#. Third

.. code-block:: rest

   #. First
   #. Second
   #. Third

Unnumbered lists
~~~~~~~~~~~~~~~~

* Each entry in a list begins with an Asterisk (``*``).
* List items can be displayed for multiple lines as long as the list items
  remain indented.

.. code-block:: rest

   * Each entry in a list begins with an Asterisk (``*``).
   * List items can be displayed for multiple lines as long as the list items
     remain indented.

Definition lists
~~~~~~~~~~~~~~~~

Term
    Definition of the term
Different term
    …and its definition

.. code-block:: rest

   Term
       Definition of the term
   Different term
       …and its definition

Nested lists
------------

* Lists can also be nested

  * and contain subitems

.. code-block:: rest

   * Lists can also be nested

     * and contain subitems

Literal blocks
--------------

    «Block quotation marks look like paragraphs, but are indented with one
    or more spaces.»

.. code-block:: rest

        «Block quotation marks look like paragraphs, but are indented with one
        or more spaces.»

Line blocks
-----------

| Because of the pipe character, this becomes one line.
| And this will be another line.

.. code-block:: rest

   | Because of the pipe character, this becomes one line.
   | And this will be another line.

Code blocks
-----------

Blocks of code are introduced and indented with a colon::

    import docutils
    print help(docutils)

>>> print 'But doctests start with ">>>" and don’t need to be indented.'

.. code-block:: rest

   Blocks of code are introduced and indented with a colon::

       import docutils
       print help(docutils)

   >>> print 'But doctests start with ">>>" and don’t need to be indented.'

Tables
------

+----------------+----------------+----------------+----------------+
| Column heading | Column heading | Column heading | Column heading |
+================+================+================+================+
| body row 1,    | body row 1,    | body row 1,    | body row 1,    |
| column 1       | column 2       | column 3       | column 4       |
+----------------+----------------+----------------+----------------+
| body row 2,    | body row 2,    | body row 2,                     |
| column 1       | column 2       | column 3,  colspan 2            |
+----------------+----------------+----------------+----------------+
| body row 3,    | body row 3,    | body row 3,    | body row 4,    |
| column 1       | column 2       | column 3,      | column 4       |
+----------------+----------------+ rowspan 2      +----------------+
| body row 5,    | body row 5,    |                | body row 5,    |
| column 1       | column 2       |                | column 4       |
+----------------+----------------+----------------+----------------+

.. code-block:: rest

   +----------------+----------------+----------------+----------------+
   | Column heading | Column heading | Column heading | Column heading |
   +================+================+================+================+
   | body row 1,    | body row 1,    | body row 1,    | body row 1,    |
   | column 1       | column 2       | column 3       | column 4       |
   +----------------+----------------+----------------+----------------+
   | body row 2,    | body row 2,    | body row 2,                     |
   | column 1       | column 2       | column 3,  colspan 2            |
   +----------------+----------------+----------------+----------------+
   | body row 3,    | body row 3,    | body row 3,    | body row 4,    |
   | column 1       | column 2       | column 3,      | column 4       |
   +----------------+----------------+ rowspan 2      +----------------+
   | body row 5,    | body row 5,    |                | body row 5,    |
   | column 1       | column 2       |                | column 4       |
   +----------------+----------------+----------------+----------------+

Comments
--------

.. A comment block begins with two points and can be indented further

.. code-block:: rest

   .. A comment block begins with two points and can be indented further
