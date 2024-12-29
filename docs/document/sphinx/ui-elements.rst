UI elements and interactions
============================

Sphinx provides three different roles for the documentation of the user
interface and its interactions: ``guilabel``, ``kbd`` and ``menuselection``:

.. list-table::
   :header-rows: 1

   * - Input
     - Output
     - Annotations
   * - .. code-block:: rest

          :guilabel:`Cancel`
     -  :guilabel:`Cancel`
     - Any label used in the user interface can be labelled with this role,
       including the labels of buttons, window titles, field, menu and menu
       selection names and values in selection lists.
   * - .. code-block:: rest

          :guilabel:`&Cancel`
     -  :guilabel:`&Cancel`
     - Keyboard shortcuts for GUI labelling can be inserted with an et character
       (``&``); this leads to underlining of the following letter in the output.

       .. note::
          If you want to insert an et character, you can simply double it.
   * - .. code-block:: rest

          :kbd:`Ctrl-s`
     -  :kbd:`Ctrl-s`
     - This represents a sequence of keystrokes. The form of the key sequence
       may depend on platform or application-specific conventions. The names of
       modifier keys should be written out in full to improve accessibility.
       Keyboard labelling should be referenced.
   * - .. code-block:: rest

          :menuselection:`File --> Save`
     - :menuselection:`File --> Save`
     - A menu selection is labelled with the ``menuselection`` role. This marks
       the complete sequence, including the selection of submenus, specific
       operations or any sub-sequences. The names of the individual selections
       are separated by ``-->``.

       Like :rst:role:`guilabel`, :rst:role:`menuselection` supports keyboard
       shortcuts with an et character (``&``).
