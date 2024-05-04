Unified Modeling Language (UML)
===============================

Installation
------------

#. Install `plantuml <https://plantuml.com/starting>`_:

   .. tab:: Linux

      .. code-block:: console

         $ sudo apt install plantuml

   .. tab:: macOS

      .. code-block:: console

         $ brew install plantuml

#. Install `sphinxcontrib-plantuml
   <https://pypi.org/project/sphinxcontrib-plantuml/>`_:

   .. tab:: Linux/macOS

      .. code-block:: console

         $ bin/python -m pip install sphinxcontrib-plantuml

   .. tab:: Windows

      .. code-block:: ps1con

         C:> Scripts\python -m pip install sphinxcontrib-plantuml

#. We then configure the ``conf.py``:

   .. code-block:: python

      extensions = [
          ...,
          "sphinxcontrib.plantuml",
      ]

      plantuml = "/PATH/TO/PLANTUML"

   .. note::
      Also in Windows, the path is specified with ``/``.

.. toctree::
   :titlesonly:
   :hidden:

   sequence-diagram
   use-case-diagram
   activity-diagram
   class-diagram
