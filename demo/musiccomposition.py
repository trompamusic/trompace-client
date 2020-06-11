import itertools

from trompace.mutations import musiccomposition


def main(print_queries: bool, submit_queries: bool):
    # A symphony
    mutation_symphony = musiccomposition.mutation_create_music_composition(
        # These 5 fields are required:
        # Who created the item in the CE, either a link to the version of the software,
        #  or if not possible, https://trompamusic.eu
        creator="https://github.com/trompamusic/trompa-ce-client/tree/master/demo",
        # Who this data came from
        contributor="https://musicbrainz.org",
        # The specific page that this data came from
        source="https://musicbrainz.org/work/5b8cb51a-6b4f-48b7-888d-c7f1e812dfba",
        # The mimetype of `source`
        format_="text/html",
        # the html <title> of `source`
        title="Symphony no. 1 in D major “Titan” - MusicBrainz",
        name="Symphony no. 1 in D major “Titan”",
        language="en"
    )

    # The first movement of the above symphony
    mutation_part = musiccomposition.mutation_create_music_composition(
        # These 5 fields are required:
        # Who created the item in the CE, either a link to the version of the software,
        #  or if not possible, https://trompamusic.eu
        creator="https://github.com/trompamusic/trompa-ce-client/tree/master/demo",
        # Who this data came from
        contributor="https://musicbrainz.org",
        # The specific page that this data came from
        source="https://musicbrainz.org/work/f969bc33-3297-335b-9dcb-1840bfea4781",
        # The mimetype of `source`
        format_="text/html",
        # the html <title> of `source`
        title="Symphony no. 1 in D major “Titan”: I. Langsam. Schleppend - MusicBrainz",
        name="Symphony no. 1 in D major “Titan”: I. Langsam. Schleppend",
        language="en",
        # First movement - position 1
        position=1
    )

    print("\nMusicComposition - symphony\n")
    if print_queries:
        print(mutation_symphony)
    if submit_queries:
        pass

    print("\nMusicComposition - movement\n")
    if print_queries:
        print(mutation_part)
    if submit_queries:
        pass

    # TODO: These ids are just for demonstration, ideally we would get them from the mutations and link the real items
    symphony_id = "ca75c580-104f-4701-8101-0a6023c791b9"
    part_id = "89a0319c-bd4b-4e19-b34e-528d3aba7cca"
    composer_id = "a6900369-b474-40d2-b8fc-724136b48bc0"

    # The composer is the composer of both the symphony and the movement
    mutation_symp_composer = musiccomposition.mutation_merge_music_composition_composer(symphony_id, composer_id)
    mutation_part_composer = musiccomposition.mutation_merge_music_composition_composer(part_id, composer_id)

    print("\nMusicComposition symphony - Person composer\n")
    if print_queries:
        print(mutation_symp_composer)
    if submit_queries:
        pass

    print("\nMusicComposition part - Person composer\n")
    if print_queries:
        print(mutation_part_composer)
    if submit_queries:
        pass

    # Mark that the movement is a part of the symphony
    # This is a property on CreativeWork, and has an inverse isPartOf
    mutation_has_part = musiccomposition.mutation_merge_music_composition_has_part(symphony_id, part_id)
    # This is a property on MusicComposition and is more specific, but has no inverse
    mutation_composition = musiccomposition.mutation_merge_music_composition_included_composition(symphony_id, part_id)

    print("\nMusicComposition hasPart\n")
    if print_queries:
        print(mutation_has_part)
    if submit_queries:
        pass

    print("\nMusicComposition includedComposition\n")
    if print_queries:
        print(mutation_composition)
    if submit_queries:
        pass

    """
query {
  MusicComposition(identifier:"3611b2c6-ea83-407f-881d-cc429e385b79") {
    identifier
    name
    source
    hasPart {
      ... on MusicComposition {
        identifier
        name
        source
        position
      }
    }
    includedComposition {
      ... on MusicComposition {
        identifier
        name
        source
        position
      }
    }
    composer {
      ... on Person {
        identifier
        name
        source
      }
    }
  }
}


query {
  MusicComposition(identifier:"1643bf5e-3040-475d-9f51-3e0c3a64452e") {
    identifier
    name
    source
    position
    isPartOf {
      ... on MusicComposition {
        identifier
        name
        source
      }
    }
  }
}
    """

    # Languages
    # MusicCompositions have 2 language fields, 'language', which is the language that `source` is written in,
    # and 'inLanguage`, which is the language that any lyrics are written in. In some cases we could have
    # two nodes referring to the same composition, but with a different name and language
    mutation_de = musiccomposition.mutation_create_music_composition(
        # These 5 fields are required:
        # Who created the item in the CE, either a link to the version of the software,
        #  or if not possible, https://trompamusic.eu
        creator="https://github.com/trompamusic/trompa-ce-client/tree/master/demo",
        # Who this data came from
        contributor="https://musicbrainz.org",
        # The specific page that this data came from
        source="https://musicbrainz.org/work/14514e77-f06c-4d24-a4d5-9a5962acae64",
        # The mimetype of `source`
        format_="text/html",
        # the html <title> of `source`
        title="Das Lied von der Erde - MusicBrainz",
        name="Das Lied von der Erde",
        language="de",
        inlanguage="de"
    )

    mutation_en = musiccomposition.mutation_create_music_composition(
        # These 5 fields are required:
        # Who created the item in the CE, either a link to the version of the software,
        #  or if not possible, https://trompamusic.eu
        creator="https://github.com/trompamusic/trompa-ce-client/tree/master/demo",
        # Who this data came from
        contributor="https://musicbrainz.org",
        # The specific page that this data came from
        source="https://musicbrainz.org/work/14514e77-f06c-4d24-a4d5-9a5962acae64",
        # The mimetype of `source`
        format_="text/html",
        # the html <title> of `source`
        title="Das Lied von der Erde - MusicBrainz",
        name="The Song of the Earth",
        language="en",
        inlanguage="de"
    )

    print("\nMusicComposition - de\n")
    if print_queries:
        print(mutation_de)
    if submit_queries:
        pass

    print("\nMusicComposition - en\n")
    if print_queries:
        print(mutation_en)
    if submit_queries:
        pass

    # These two compositions are the same thing, so we should link them as such
    # TODO: These ids are just for demonstration, ideally we would get them from the mutations and link the real items
    work_identifiers = ['c64d93b1-818b-4414-a359-8bf2de08d233', 'e0f2a11d-28c4-41dd-afab-58d490d1b00b']
    print("\nMusicComposition - MusicComposition exactMatch\n")
    for fr, to in itertools.permutations(work_identifiers, 2):
        mutation_match = musiccomposition.mutation_merge_music_composition_exact_match(fr, to)
        if print_queries:
            print(mutation_match)
        if submit_queries:
            pass

    """
query {
  MusicComposition(identifier:"5b27f75d-5414-4230-9210-40c477cf8dd1") {
    identifier
    name
    source
    language
    inLanguage
    exactMatch {
      ... on MusicComposition {
        identifier
        name
        source
        language
        inLanguage
      }
    }
  }
}
    """


if __name__ == '__main__':
    from demo import args
    main(args.args.print, args.args.submit)
