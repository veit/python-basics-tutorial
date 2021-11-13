The ``xml`` module
==================

The  :doc:`XML <python3:library/xml>` module comes with Python. In the following
section we will focus on the two sub-modules :doc:`minidom
<python3:library/xml.dom.minidom>` and :doc:`ElementTree
<python3:library/xml.etree.elementtree>`.

Working with ``minidom``
------------------------

In the following example we analyse :download:`books.xml`:

.. literalinclude:: books.xml
   :language: xml
   :lines: 1-
   :lineno-start: 1

#. To do this, we first import the ``minidom`` module and give it the same name
   so that it can be referenced more easily:

   .. literalinclude:: minidom_example.py
      :language: py
      :lines: 1
      :lineno-start: 1

#. Then we define the method ``getTitles`` and capture the desired XML tags with
   the method ``getElementsByTagName``:

   .. literalinclude:: minidom_example.py
      :language: py
      :lines: 3-9
      :lineno-start: 3

#. Then we create an empty list called ``titles``, which is filled with the
   title objects:

   .. literalinclude:: minidom_example.py
      :language: py
      :lines: 11-14
      :lineno-start: 11

#. Now the title is output in nested ``for``-loops:

   .. literalinclude:: minidom_example.py
      :language: py
      :lines: 16-20
      :lineno-start: 16

#. Finally, we set the ``__name__`` variable like ``__main__`` so that the
   module can be executed like the main program. Then we apply our ``getTitles``
   method to our :download:`books.xml` file:

   .. literalinclude:: minidom_example.py
      :language: py
      :lines: 22-
      :lineno-start: 22

Parsing with ElementTree
------------------------

#. Importing ``cElementTree``:

   .. literalinclude:: elementtree_example.py
      :language: py
      :lines: 1
      :lineno-start: 1

   .. note::
      ``cElementTree``  written in C and is considerably faster than
      ``ElementTree``.

#. Then we define the method ``parseXML`` and the ``root`` element:

   .. literalinclude:: elementtree_example.py
      :language: py
      :lines: 3-10
      :lineno-start: 3

   .. code-block:: py

      <Element 'catalog' at 0x10b009620>
      tag=catalog, attrib={}

#. Output the XML child elements of ``book``:

   .. literalinclude:: elementtree_example.py
      :language: py
      :lines: 12-16
      :lineno-start: 12

   .. code-block:: py

      book {'id': '1'}
      title
      language
      author
      license
      date
      book {'id': '2'}
      ...

#. Output the contents of the child elements with  ``iter``:

   .. literalinclude:: elementtree_example.py
      :language: py
      :lines: 19-26
      :lineno-start: 19

   .. code-block:: py

      --------------------
      Iterating using iter
      --------------------
      catalog=
      book=
      title=Python basics
      language=en
      author=Veit Schiele
      license=BSD-3-Clause
      date=2021-10-28
      book=
      title=Jupyter Tutorial
      ...
