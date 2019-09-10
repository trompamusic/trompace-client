import mutations
from mutations.person import mutation_create_artist, mutation_update_artist
from mutations.document import mutation_create_document
from mutations.work import mutation_create_composition
def create_artist_test():
	created_artist = mutation_create_artist("booboo", "booboo", "booboo", "booboo", "booboo", "booboo", "en")

	expected_artist = '\nmutation {\n  \nCreatePerson(\ntitle: "booboo"\nname: "booboo"\npublisher: "booboo"\ncontributor: "booboo"\ncreator: "booboo"\nsource: "booboo"\nsubject: "artist"\ndescription: "booboo"\nformat: "text/html"\nlanguage: en\n) {\n  identifier\n  name\n}\n\n}\n'

	updated_artist = mutation_update_artist("id", publisher = "blah-blah")

	expected_update = '\nmutation {\n  \nUpdatePerson(\n  identifier: "id"\npublisher: "blah-blah"\n) {\n  identifier\n  relation\n}\n\n}\n'

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