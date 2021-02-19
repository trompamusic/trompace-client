Person
======

A ``Person`` objects represents a web resource about a person. For example, this could be a composer or performer.

We recommend that the following fields are set:

.. csv-table::
   :header: "field", "required", "Description"
   :stub-columns: 1

   `title <http://purl.org/dc/elements/1.1/title>`_, yes, The title of the resource indicated by ``source``
   contributor, yes,The main URL of the site where the information about this Person was taken from
   creator, yes, "The person, organization or service who is creating this Person (e.g. URL of the software)"
   source, yes, The URL of the web resource where information about this Person is taken from
   language, yes, "The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr"
   format\_, yes, The mimetype of the resource indicated by `source`
   name, yes, The name of the person
   family_name, , The family name of the person
   given_name, , The given name of the person
   gender, , The person's gender
   birth_date, , "The birth date of the person, formatted as yyyy, yyyy-mm or yyyy-mm-dd"
   death_date, , "The date of death of the person , formatted as yyyy, yyyy-mm or yyyy-mm-dd"
   description, , A biographical description of the person
   image, , URL to an image associated with the person
   publisher, , An entity responsible for making the resource available
   honorific_prefix, , An honorific prefix
   honorific_suffix, , An honorific suffix
   job_title, , The person's job title


Relations
---------

exactMatch: Use :meth:`trompace.mutations.person.mutation_person_add_exact_match_person`



.. automodule:: trompace.mutations.person
   :members: