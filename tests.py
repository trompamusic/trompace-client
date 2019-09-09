from person import mutation_artist

def create_artist_test():
	created_artist = mutation_artist("booboo", "booboo", "booboo", "booboo", "booboo", "booboo", "en")

	expected_artist = '\nmutation {\n  \nCreatePerson(\ntitle: "booboo"\nname: "booboo"\npublisher: "booboo"\ncontributor: "booboo"\ncreator: "booboo"\nsource: "booboo"\nsubject: "artist"\ndescription: "booboo"\nformat: "text/html"\nlanguage: en\n) {\n  identifier\n  name\n}\n\n}\n'

	if created_artist == expected_artist:
		print("Artist OK")
	else:
		print(artist_error)


def main():
	create_artist_test()

if __name__ == '__main__':
    main()