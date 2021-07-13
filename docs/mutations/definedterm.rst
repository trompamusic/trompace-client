DefinedTerm
===========

A :schema:`DefinedTermSet` is a set of known terms (:schema:`DefinedTerm`) grouped together, for example
a set of categories or a classification scheme.

Creating objects
----------------

DefinedTermSets
^^^^^^^^^^^^^^^

A :schema:`DefinedTermSet` is a logical grouping.

.. autofunction:: trompace.mutations.definedterm.create_defined_term_set
.. autofunction:: trompace.mutations.definedterm.update_defined_term_set
.. autofunction:: trompace.mutations.definedterm.delete_defined_term_set

DefinedTerms
^^^^^^^^^^^^
A :schema:`DefinedTerm` is an element in a group.

.. autofunction:: trompace.mutations.definedterm.create_defined_term
.. autofunction:: trompace.mutations.definedterm.update_defined_term
.. autofunction:: trompace.mutations.definedterm.delete_defined_term


Relations
---------

hasDefinedTerm
^^^^^^^^^^^^^^

A :schema:`DefinedTerm` is joined to a :schema:`DefinedTermSet` with the :schema:`hasDefinedTerm` relation.

.. autofunction:: trompace.mutations.definedterm.defined_term_add_to_defined_term_set
