Code blocks
===========

Code blocks can be easily represented with the :rst:dir:`code-block` directive.
Together with `Pygments <http://pygments.org/>`_, Sphinx will automatically
highlight the syntax. You can specify the appropriate language for a code block
with

.. rst:directive:: .. code-block:: LANGUAGE
   You can use this for example like this:

   .. code-block:: rest

      .. code-block:: python
         import this

   .. rubric:: Optionen

   .. rst:directive:option:: linenos

      For :rst:dir:`code-block`, the ``linenos`` option can also be used to
      specify that the code block should be displayed with line numbers:

      .. code-block:: rest

         .. code-block:: python

            :linenos:
            import this

      .. code-block:: python

         :linenos:
         import this

   .. rst:directive:option:: lineno-start

      Die erste Zeilennummer kann mit der ``lineno-start``-Option ausgewählt
      werden; ``linenos`` wird dann automatisch aktiviert:
      The first line number can be selected with the ``lineno-start`` option;
      ``linenos`` will then be activated automatically:

      .. code-block:: rest

         .. code-block:: python
            :lineno-start: 10

            import antigravity

      .. code-block:: python
          :lineno-start: 10

          import antigravity

   .. rst:directive:option:: emphasize-lines

      ``emphasize-lines`` allows you to emphasise individual lines.

.. rst:directive:: .. literalinclude:: FILENAME

   allows you to include external files.

   .. rubric:: Options

   .. rst:directive:option:: emphasize-lines
   .. rst:directive:option:: linenos

      Here is an example from our :doc:`jupyter-tutorial:index`:

      .. code-block:: rest

          .. literalinclude:: main.py
             :emphasize-lines: 3,7-10,20-22
             :linenos:

      .. literalinclude:: main.py
         :emphasize-lines: 3,7-10,20-22
         :linenos:
      
   .. rst:directive:option:: diff

      If you want to show the diff of your code, you can specify the old file
      with the diff option, for example:

      .. code-block:: rest

         .. literalinclude:: main.py
            :diff: main.py.orig

      .. literalinclude:: main.py
         :diff: main.py.orig

.. _deprecated:

Obsolete code
-------------

.. rst:directive:: .. deprecated:: version

   Describes when the function became obsolete. An explanation can also be
   given to inform what should be used instead. For example

   .. code-block:: rest

      .. deprecated:: 4.1
         instead use :func:`new_function`.

   .. deprecated:: 4.1
      instead use :func:`new_function`.

.. rst:directive:option:: py:module:deprecated

   Marks a Python module as obsolete; it is then marked as such in various
   places.
