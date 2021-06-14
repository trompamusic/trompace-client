Person
======

A :schema:`Person` object represents a web resource about a person. For example, this could be a composer or performer.


Creating objects
----------------

To create a ``Person`` object, use the ``CreatePerson`` mutation

.. autofunction:: trompace.mutations.person.mutation_create_person

To update a ``Person`` object, use the ``UpdatePerson`` mutation

.. autofunction:: trompace.mutations.person.mutation_update_person

To delete a ``Person`` object, use the ``DeletePerson`` mutation

.. autofunction:: trompace.mutations.person.mutation_delete_person


Relations
---------

exactMatch
^^^^^^^^^^

The `skos:exactMatch <http://www.w3.org/2004/02/skos/core#exactMatch>`_ relationship is used to identify
that two ``Person`` nodes refer to the exact same natural person.

.. image:: ../graphics/x.png
  :target: ../_images/x.png

Use the ``MergePersonExactMatch`` mutation to create a one-way link between two ``Person`` objects

.. autofunction:: trompace.mutations.person.mutation_person_add_exact_match_person

Use the ``RemovePersonExactMatch`` mutation to remove link between two ``Person`` objects

.. autofunction:: trompace.mutations.person.mutation_person_remove_exact_match_person
