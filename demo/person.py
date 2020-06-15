import itertools

from trompace.mutations import person


def main(print_queries: bool, submit_queries: bool):
    mutation_musicbrainz = person.mutation_create_person(
        # These 5 fields are required:
        # Who created the item in the CE, either a link to the version of the software,
        #  or if not possible, https://trompamusic.eu
        creator="https://github.com/trompamusic/trompa-ce-client/tree/v0.1/demo",
        # Who this data came from
        contributor="https://musicbrainz.org",
        # The specific page that this data came from
        source="https://musicbrainz.org/artist/8d610e51-64b4-4654-b8df-064b0fb7a9d9",
        # The mimetype of `source`
        format_="text/html",
        # the html <title> of `source`
        title="Gustav Mahler - MusicBrainz",
        # The following fields are optional - fill them in if they are available
        name="Gustav Mahler",
        birth_date="1860-07-07",
        death_date="1911-05-18",
        family_name="Mahler",
        given_name="Gustav",
        gender="male",
        # The language of `source`
        language="en"
    )

    description = """<b>Gustav Mahler</b> (7 July 1860 – 18 May 1911) was an Austro-Bohemian Romantic composer, and one
     of the leading conductors of his generation. As a composer he acted as a bridge between the 19th century 
     Austro-German tradition and the modernism of the early 20th century. While in his lifetime his status as a 
     conductor was established beyond question, his own music gained wide popularity only after periods of relative 
     neglect, which included a ban on its performance in much of Europe during the Nazi era. After 1945 his 
     compositions were rediscovered by a new generation of listeners; Mahler then became one of the most frequently 
     performed and recorded of all composers, a position he has sustained into the 21st century. In 2016, 
     a BBC Music Magazine survey of 151 conductors ranked three of his symphonies in the top ten symphonies of 
     all time."""

    mutation_wikidata = person.mutation_create_person(
        creator="https://github.com/trompamusic/trompa-ce-client/tree/v0.1/demo",
        contributor="https://www.wikidata.org",
        source="https://www.wikidata.org/wiki/Q7304",
        format_="text/html",
        title="Gustav Mahler - Wikidata",
        name="Gustav Mahler",
        birth_date="1860-07-07",
        death_date="1911-05-18",
        family_name="Mahler",
        given_name="Gustav",
        gender="male",
        language="en",
        # From wikidata, language en, we use Wikipedia's extract API to get the first paragraph
        description=description,
        # The first image linked from wikidata
        image="https://upload.wikimedia.org/wikipedia/commons/b/b7/Gustav-Mahler-Kohut.jpg"
    )

    # A more basic record with just required fields
    mutation_viaf = person.mutation_create_person(
        creator="https://github.com/trompamusic/trompa-ce-client/tree/v0.1/demo",
        contributor="https://viaf.org",
        source="https://viaf.org/viaf/61732497/",
        format_="text/html",
        title="61732497"
    )

    print("\nPerson - Musicbrainz\n")
    if print_queries:
        print(mutation_musicbrainz)
    if submit_queries:
        pass

    print("\nPerson - Wikidata\n")
    if print_queries:
        print(mutation_wikidata)
    if submit_queries:
        pass

    print("\nPerson - VIAF\n")
    if print_queries:
        print(mutation_viaf)
    if submit_queries:
        pass

    # skos:exactMatch
    # These three Person objects refer to the same person, therefore we should join them together.
    # We use the relation skos:exactMatch, created with the MergePersonExactMatch mutation.
    # We use the Merge variant to ensure that we don't create the same relationship more than once.
    # Explicitly create this link in all directions between all objects

    # TODO: Ideally we should submit the above queries, get real ids, and then use them in this query
    person_identifiers = ["1fc48b62-0b6d-4f43-8ed5-e1c3280c6530", "a911036d-0549-41d8-86cd-d756dfa1d8a4",
                          "8e706d4b-6a70-46e6-8613-9db63d3f8d57"]

    print("\nPerson - Person exactMatch\n")
    for fr, to in itertools.permutations(person_identifiers, 2):
        mutation_match = person.mutation_person_add_exact_match_person(fr, to)
        if print_queries:
            print(mutation_match)
        if submit_queries:
            pass


if __name__ == '__main__':
    from demo import args
    main(args.args.print, args.args.submit)
