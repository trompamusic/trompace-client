Demos
=====

We provide demo scripts which show how to use the library and how to structure the Trompa CE data model.

The scripts can optionally output sample graphql queries so that they can be copied and modified, and can also
submit the sample queries to a CE instance. The scripts also include some comments explaining specific
data modelling decisions that were made for some types.

Use the ``--print`` flag to output the graphql queries that are being executed, and ``--submit`` to send them
to the configured CE:

.. code-block:: bash

    TROMPACE_CLIENT_CONFIG=trompace.ini python -m demo.person --print --submit


DefinedTerm
^^^^^^^^^^^

Shows how to create a fixed vocabulary of folksonomy tags/categories, or a fixed vocabulary of annotation motivations
for use in Web Annotations using :schema:`DefinedTermSet` and :schema:`DefinedTerm`.

.. code-block:: bash

    python -m demo.definedterm --print --submit

MediaObject
^^^^^^^^^^^

Shows how to create :schema:`MediaObject`\ s which refer to files in the CE ecosystem (scores, images, audio, etc), as
well as the required links between ``MediaObject``\ s which are related to each other.

.. code-block:: bash

    python -m demo.mediaobject --print --submit

MusicComposition
^^^^^^^^^^^^^^^^

Shows how to create a :schema:`MusicComposition`, referring to a musical work. Also shows how to indicate movements of
larger works, and composers.

.. code-block:: bash

    python -m demo.musiccomposition --print --submit

Person
^^^^^^

Shows how to create :schema:`Person` objects, referring to natural people. Shows how to link together references
to the same ``Person`` on different websites.

.. code-block:: bash

    python -m demo.person --print --submit

Rating
^^^^^^

Shows how to create :schema:`Rating` objects and rating templates, for use in Web annotations,

.. code-block:: bash

    python -m demo.rating --print --submit

Annotation Body
^^^^^^^^^^^^^^^

Shows how to create :oa:`Annotation` objects and different types of values for :oa:`hasBody` (external URLs,
:oa:`TextualBody`, and links to existing nodes in the CE).

.. code-block:: bash

    python -m demo.annotation.annotationbody --print --submit

Annotation Fixed Vocabulary
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shows how to create :oa:`Annotation` objects and the use of a fixed :schema:`DefinedTerm` as an :oa:`hasBody`.

.. code-block:: bash

    python -m demo.annotation.annotationfixedvocab --print --submit

Annotation Linking
^^^^^^^^^^^^^^^^^^

Shows how to create multiple :oa:`Annotation` objects and link them together into a "meta" annotation.

.. code-block:: bash

    python -m demo.annotation.annotationlinking --print --submit

Annotation Motivation
^^^^^^^^^^^^^^^^^^^^^

Shows how to create :oa:`Annotation` objects and the use of a fixed :schema:`DefinedTerm` as an :oa:`motivatedBy`.

.. code-block:: bash

    python -m demo.annotation.annotationmotivation --print --submit

Annotation Rating
^^^^^^^^^^^^^^^^^

Shows how to create :oa:`Annotation` objects and the use of a :schema:`Rating` as an :oa:`hasBody`, along with
links to the Rating definition that the rating was derived from (:prov:`wasDerivedFrom`).

.. code-block:: bash

    python -m demo.annotation.annotationrating --print --submit

Annotation Tag
^^^^^^^^^^^^^^

Shows how to create :oa:`Annotation` objects and a freeform text tag.

.. code-block:: bash

    python -m demo.annotation.annotationtarget --print --submit

Annotation Target
^^^^^^^^^^^^^^^^^

Shows how to create :oa:`Annotation` objects and different types of values for :oa:`hasTarget` (external URLs,
existing nodes in the CE, URLs specified by fields of nodes in the CE).

.. code-block:: bash

    python -m demo.annotation.annotationbody --print --submit

Annotation Session
^^^^^^^^^^^^^^^^^^

Shows how to add many :oa:`Annotation` objects to a single logical session.

.. code-block:: bash

    python -m demo.annotation.session --print --submit


Annotation Toolkit
^^^^^^^^^^^^^^^^^^

Shows how to join together a collection of Rating templates, Fixed Vocabularies, and Motivations into an annotation toolkit.

.. code-block:: bash

    python -m demo.annotation.toolkit --print --submit
