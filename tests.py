from person import mutation_create_artist
from document import mutation_create_document

def create_artist_test():
	created_artist = mutation_create_artist("booboo", "booboo", "booboo", "booboo", "booboo", "booboo", "en")

	expected_artist = '\nmutation {\n  \nCreatePerson(\ntitle: "booboo"\nname: "booboo"\npublisher: "booboo"\ncontributor: "booboo"\ncreator: "booboo"\nsource: "booboo"\nsubject: "artist"\ndescription: "booboo"\nformat: "text/html"\nlanguage: en\n) {\n  identifier\n  name\n}\n\n}\n'

	if created_artist == expected_artist:
		print("Artist OK")
	else:
		print("Artist Error")

def create_document_test():

	created_document = mutation_create_document("booboo", "booboo", "booboo", "booboo", "booboo", "booboo", "en")

	expected_document = '\nmutation {\n  \nCreateDigitalDocument(\n  title: "booboo"\nname: "booboo"\npublisher: "booboo"\ncontributor: "booboo"\ncreator: "booboo"\nsource: "booboo"\nsubject: "artist"\ndescription: "booboo"\nformat: "text/html"\nlanguage: en\n) {\n  identifier\n  relation\n}\n\n}\n'

	if created_document == expected_document:
		print("Document OK")
	else:
		print("Document Error")
def main():
	create_artist_test()
	create_document_test()

if __name__ == '__main__':
    main()