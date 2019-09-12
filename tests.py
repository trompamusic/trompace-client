import mutations
from mutations.person import mutation_create_artist, mutation_update_artist, mutation_delete_artist
from mutations.document import mutation_create_document
from mutations.work import mutation_create_composition
from connection import submit_query



def create_artist_test():
    created_artist = mutation_create_artist("A. J. Fynn", "https://www.cpdl.org", "https://www.cpdl.org", "https://www.upf.edu", "https://www.cpdl.org/wiki/index.php/A._J._Fynn", "Born circa 1860Died circa 1920A. J. Fynn was an early 20th Century scholar in literature and anthropology, specializing in the American West and Native American culture. His most notable musical composition was \u201cWhere The Columbines Grow\u201d, which was adopted as the official state song of the US State of Colorado in 1915.View the Wikipedia article on A. J. Fynn.", "en")


    expected_artist = '\nmutation {\n  \nCreatePerson(\ntitle: "A. J. Fynn"\nname: "A. J. Fynn"\npublisher: "https://www.cpdl.org"\ncontributor: "https://www.cpdl.org"\ncreator: "https://www.upf.edu"\nsource: "https://www.cpdl.org/wiki/index.php/A._J._Fynn"\nsubject: "artist"\ndescription: "Born circa 1860Died circa 1920A. J. Fynn was an early 20th Century scholar in literature and anthropology, specializing in the American West and Native American culture. His most notable musical composition was \\u201cWhere The Columbines Grow\\u201d, which was adopted as the official state song of the US State of Colorado in 1915.View the Wikipedia article on A. J. Fynn."\nformat: "text/html"\nlanguage: en\n) {\n  identifier\n  name\n}\n\n}\n'
    updated_artist = mutation_update_artist('2eeca6dd-c62c-490e-beb0-2e3899fca74f', publisher = "Https://www.cpdl.org")

    expected_update = '\nmutation {\n  \nUpdatePerson(\n  identifier: "id"\npublisher: "blah-blah"\n) {\n  identifier\n  relation\n}\n\n}\n'

    delete_artist = mutation_delete_artist('2eeca6dd-c62c-490e-beb0-2e3899fca74f')

    print(delete_artist)



    if created_artist == expected_artist and updated_artist == expected_update:
        print("Artist OK")
    else:
        print("Artist Error")

def create_document_test():

    created_document = mutation_create_document("booboo", "booboo", "booboo", "booboo", "booboo", "booboo", "document",  "en")

    expected_document = '\nmutation {\n  \nCreateDigitalDocument(\n  title: "booboo"\nname: "booboo"\npublisher: "booboo"\ncontributor: "booboo"\ncreator: "booboo"\nsource: "booboo"\nsubject: "document"\ndescription: "booboo"\nformat: "text/html"\nlanguage: en\n) {\n  identifier\n  relation\n}\n\n}\n'

    if created_document == expected_document:
        print("Document OK")
    else:
        print("Document Error")

def create_composition_test():

    created_document = mutation_create_composition("booboo", "booboo", "booboo", "booboo", "booboo", "booboo", "composition", "en")

    expected_document = '\nmutation {\n  \nCreateMusicComposition(\n  title: "booboo"\nname: "booboo"\npublisher: "booboo"\ncontributor: "booboo"\ncreator: "booboo"\nsource: "booboo"\nsubject: "composition"\ndescription: "booboo"\nformat: "text/html"\nlanguage: en\n) {\n  identifier\n  name\n  relation\n}\n\n}\n'

    if created_document == expected_document:
        print("Work OK")
    else:
        print("Work Error")

def main():
    create_artist_test()
    create_document_test()
    create_composition_test()

if __name__ == '__main__':
    main()