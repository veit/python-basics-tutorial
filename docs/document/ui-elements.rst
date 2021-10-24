UI elements and interactions
============================

.. rst:role:: guilabel

   Labels that are presented as part of an interactive user interface should be
   marked with :rst:role:`guilabel`. Any label used in the interface should be
   identified with this role, including labels for buttons, window titles,
   field names, menu and menu selection names, and even values in selection
   lists.

   A keyboard shortcut for GUI labelling can be inserted with an ampersand (&);
   this will underline the following letter in the output.

   :guilabel:`&Cancel` is achieved, for example, with the following distinction:

   .. code-block:: rest

      :guilabel:`&Cancel`

   .. note::
      If you want to insert an ampersand, you can simply double it.

.. rst:role:: kbd

   This represents a sequence of keystrokes. The form of the key sequence may
   depend on platform- or application-specific conventions. If there are no
   corresponding conventions, the names of modifier keys should be written out
   to improve accessibility. Also, do not reference a specific keyboard label.

   You can achieve :kbd:`Ctrl-s`, for example, with the following markup:

   .. code-block:: rest

      :kbd:`Ctrl-s`

.. rst:role:: menuselection

   A menu selection should be marked with the ``menuselection`` role. This is
   used to mark a complete sequence, including submenu selections and selections
   of specific operations or any subsequences. The names of the individual
   selections should be separated by ``-->``.

   :menuselection:`View --> Cell Toolba r--> Slideshow` is achieved, for
   example, with the following markup:

   .. code-block:: rest

      :menuselection:`View --> Cell Toolbar --> Slideshow`

   :rst:role:`menuselection`, just like  :rst:role:`guilabel`, also supports
   keyboard shortcuts with an ampersand (&).
