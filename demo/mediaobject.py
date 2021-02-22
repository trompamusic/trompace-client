from trompace.mutations import mediaobject, musiccomposition


def main(print_queries: bool, submit_queries: bool):

    mutation_work = musiccomposition.mutation_create_music_composition(
        # These 5 fields are required:
        # Who created the item in the CE, either a link to the version of the software,
        #  or if not possible, https://trompamusic.eu
        creator="https://github.com/trompamusic/trompa-ce-client/tree/master/demo",
        # Who this data came from
        contributor="https://www.cpdl.org",
        # The specific page that this data came from
        source="https://www.cpdl.org/wiki/index.php/A_este_sol_peregrino_(Tom%C3%A1s_de_Torrej%C3%B3n_y_Velasco)",
        # The mimetype of `source`
        format_="text/html",
        # the html <title> of `source`
        title="A este sol peregrino (Tomás de Torrejón y Velasco) - ChoralWiki",
        name="A este sol peregrino (Tomás de Torrejón y Velasco)",
        language="en",
        inlanguage="es"
    )

    print("\nMusicComposition - work\n")
    if print_queries:
        print(mutation_work)
    if submit_queries:
        pass

    # PDF score from CPDL
    cpdl_pdf = mediaobject.mutation_create_media_object(
        # These 4 fields are required:
        # Who created the item in the CE, either a link to the version of the software,
        #  or if not possible, https://trompamusic.eu
        creator="https://github.com/trompamusic/trompa-ce-client/tree/master/demo",
        # Who this data came from
        contributor="https://www.cpdl.org",
        # The URL to a webpage that describes this MediaObject. CPDL Mediawiki has html pages for each file
        # If there is no associated webpage for this object, you can set it to the same value as `url`
        source="https://www.cpdl.org/wiki/index.php/File:Torrejon-A_este_sol_peregrino.pdf",
        # The <title> of `source`
        title="File:Torrejon-A este sol peregrino.pdf - ChoralWiki",
        name="Torrejon-A este sol peregrino.pdf",
        # The mimetype of `source`
        format_="text/html",
        # Specifically for CPDL, we set URL to the same as `source`
        url="https://www.cpdl.org/wiki/index.php/File:Torrejon-A_este_sol_peregrino.pdf",
        # A url that gives direct access to the bytes that make up this file.
        # In the case of CPDL we look this up by the API
        contenturl="https://www.cpdl.org/wiki/images/b/b5/Torrejon-A_este_sol_peregrino.pdf",
        # mimetype of contenturl
        encodingformat="application/pdf",
    )

    # MusicXML score from CPDL. The structure of the fields is the same as for PDF
    cpdl_musicxml = mediaobject.mutation_create_media_object(
        creator="https://github.com/trompamusic/trompa-ce-client/tree/master/demo",
        # Who this data came from
        contributor="https://www.cpdl.org",
        # The URL to a webpage that describes this MediaObject. CPDL Mediawiki has html pages for each file
        # If there is no associated webpage for this object, you can set it to the same value as `url`
        source="https://www.cpdl.org/wiki/index.php/File:Torrejon-A_este_sol_peregrino.mxl",
        # The <title> of `source`
        title="File:Torrejon-A_este_sol_peregrino.mxl - ChoralWiki",
        name="Torrejon-A_este_sol_peregrino.mxl",
        # The mimetype of `source`
        format_="text/html",
        # Specifically for CPDL, we set URL to the same as `source`
        url="https://www.cpdl.org/wiki/index.php/File:Torrejon-A_este_sol_peregrino.mxl",
        # A url that gives direct access to the bytes that make up this file.
        # In the case of CPDL we look this up by the API
        contenturl="https://www.cpdl.org/wiki/images/a/a3/Torrejon-A_este_sol_peregrino.mxl",
        # mimetype of contenturl
        encodingformat="application/vnd.recordare.musicxml+xml",
    )

    print("\nMediaObject - CPDL PDF file\n")
    if print_queries:
        print(cpdl_pdf)
    if submit_queries:
        pass

    print("\nMediaObject - CPDL MusicXML file\n")
    if print_queries:
        print(cpdl_musicxml)
    if submit_queries:
        pass

    work_id = "64a1383c-a85b-4574-aa9c-eda917e5fd2c"
    pdf_id = "2799ea6c-161a-4379-883e-24e6cf117c11"
    xml_id = "5a6e8fb2-c922-49aa-89eb-07506210e697"
    # Both the PDF and MusicXML are examples of the MusicComposition
    example_of_work_pdf = mediaobject.mutation_merge_mediaobject_example_of_work(pdf_id, work_identifier=work_id)
    example_of_work_xml = mediaobject.mutation_merge_mediaobject_example_of_work(xml_id, work_identifier=work_id)

    print("\nMediaObject - MusicComposition exampleOfWork\n")
    if print_queries:
        print(example_of_work_pdf)
        print(example_of_work_xml)
    if submit_queries:
        pass

    # In the case of CPDL, we know that scores are written in an editor and then rendered to PDF.
    # Therefore, the PDF wasDerivedFrom the xml (http://www.w3.org/ns/prov#wasDerivedFrom)
    pdf_derived_from_xml = mediaobject.mutation_merge_media_object_wasderivedfrom(pdf_id, xml_id)
    print("\nMediaObject - MediaObject wasDerivedFrom\n")
    if print_queries:
        print(pdf_derived_from_xml)
    if submit_queries:
        pass

    # Audio rendering of a score
    cpdl_mp3 = mediaobject.mutation_create_media_object(
        creator="https://github.com/trompamusic/trompa-ce-client/tree/master/demo",
        # Who this data came from
        contributor="https://www.voctrolabs.com/",
        name="Torrejon-A_este_sol_peregrino",
        title="Torrejon-A_este_sol_peregrino",
        # In the case that we don't have a distinct source or url, we can set
        # all fields to the same value as contenturl
        source="https://my-bucket.s3.us-west-2.amazonaws.com/a_este_sol_peregrino.mp3",
        # The mimetype of `source`
        format_="audio/mpeg",
        url="https://my-bucket.s3.us-west-2.amazonaws.com/a_este_sol_peregrino.mp3",
        # A url that gives direct access to the bytes that make up this file.
        contenturl="https://my-bucket.s3.us-west-2.amazonaws.com/a_este_sol_peregrino.mp3",
        # mimetype of contenturl
        encodingformat="audio/mpeg",
    )
    print("\nMediaObject - MP3 rendering\n")
    if print_queries:
        print(cpdl_mp3)
    if submit_queries:
        pass

    mp3_id = "5db9bb3b-2653-427a-968a-d446e657f305"
    # Like the PDF and XML, the mp3 is an Example of the composition
    example_of_work_mp3 = mediaobject.mutation_merge_mediaobject_example_of_work(mp3_id, work_identifier=work_id)

    print("\nMediaObject - MusicComposition exampleOfWork\n")
    if print_queries:
        print(example_of_work_mp3)
    if submit_queries:
        pass

    # Additionally, we should link the mp3 to the musicxml score that was used as the input.
    # For completeness we set two relations, schema:encoding and prov:wasDerivedFrom
    # TODO: The arguments for these two methods are reversed, I'm not sure if it's a good idea
    mp3_derived_from_xml = mediaobject.mutation_merge_media_object_wasderivedfrom(mp3_id, xml_id)
    xml_encoding_mp3 = mediaobject.mutation_merge_media_object_encoding(xml_id, mp3_id)

    print("\nMediaObject - MediaObject relations\n")
    if print_queries:
        print(mp3_derived_from_xml)
        print(xml_encoding_mp3)
    if submit_queries:
        pass

    #########
    # IMSLP #
    #########
    imslp_musiccomposition = musiccomposition.mutation_create_music_composition(
        creator="https://github.com/trompamusic/trompa-ce-client/tree/master/demo",
        contributor="https://imslp.org",
        # The specific page that this data came from
        source="https://imslp.org/wiki/Variations_and_Fugue_in_E-flat_major,_Op.35_(Beethoven,_Ludwig_van)",
        # The mimetype of `source`
        format_="text/html",
        # the html <title> of `source`
        title="Variations and Fugue in E-flat major, Op.35 (Beethoven, Ludwig van) - IMSLP: Free Sheet Music PDF Download",
        name="Variations and Fugue in E-flat major, Op.35",
        language="en",
    )

    # MusicXML score from IMSLP
    # TODO: Note that this isn't actually a score of the MusicComposition above, but is included as an example
    imslp_musicxml = mediaobject.mutation_create_media_object(
        creator="https://github.com/trompamusic/trompa-ce-client/tree/master/demo",
        # Who this data came from
        contributor="https://imslp.org",
        # The URL to a webpage that describes this MediaObject. CPDL Mediawiki has html pages for each file
        # If there is no associated webpage for this object, you can set it to the same value as `url`
        source="https://imslp.org/wiki/File:PMLP580712-07_affer_opem.zip",
        # The <title> of `source`
        title="File:PMLP580712-07 affer opem.zip - IMSLP: Free Sheet Music PDF Download",
        # The mimetype of `source`
        format_="text/html",
        name="PMLP580712-07_affer_opem.zip",
        # Specifically for IMSLP, we set URL to the "permalink" of this file, which is
        # its "reverse lookup" url, redirecting to the page of the composition with an anchor ref
        # to the file itself. In the case of this example, this is
        # https://imslp.org/wiki/Affer_opem_(Lange,_Gregor)#IMSLP359599
        url="https://imslp.org/wiki/Special:ReverseLookup/359599",
        # A url that gives direct access to the bytes that make up this file.
        # In IMSLP, we don't link directly to files, because downloads on IMSLP are behind a disclaimer.
        # We expect that users would go from `source` and derive this themselves.
        # XML scores for IMSLP are often provided in ZIP files. We use the arcp hash-based identifier
        # (https://s11.no/2018/arcp.html#hash-based) to refer to a specific file inside the archive:
        # The sha256 of PMLP580712-07_affer_opem.zip is f0a962e51b53c9f5de92c13e191dc87cc0f2a435745911b4d58a52446299be16
        # base64 is ZjBhOTYyZTUxYjUzYzlmNWRlOTJjMTNlMTkxZGM4N2NjMGYyYTQzNTc0NTkxMWI0ZDU4YTUyNDQ2Mjk5YmUxNg==
        # and the path to the xml file inside the zip archive is /07_affer_opem.xml
        contenturl="arcp://ni,sha-256;ZjBhOTYyZTUxYjUzYzlmNWRlOTJjMTNlMTkxZGM4N2NjMGYyYTQzNTc0NTkxMWI0ZDU4YTUyNDQ2Mjk5YmUxNg==/07_affer_opem.xml",
        # mimetype of contenturl
        encodingformat="application/vnd.recordare.musicxml+xml",
    )

    # PDF Score from IMSLP
    imslp_pdf = mediaobject.mutation_create_media_object(
        creator="https://github.com/trompamusic/trompa-ce-client/tree/master/demo",
        # Who this data came from
        contributor="https://imslp.org",
        # The URL to a webpage that describes this MediaObject. CPDL Mediawiki has html pages for each file
        # If there is no associated webpage for this object, you can set it to the same value as `url`
        source="https://imslp.org/wiki/File:PMLP05827-Beethoven_Werke_Breitkopf_Serie_17_No_163_Op_35.pdf",
        # The <title> of `source`
        title="File:PMLP05827-Beethoven Werke Breitkopf Serie 17 No 163 Op 35.pdf - IMSLP: Free Sheet Music PDF Download",
        # The mimetype of `source`
        format_="text/html",
        name="PMLP05827-Beethoven Werke Breitkopf Serie 17 No 163 Op 35.pdf",
        # Specifically for IMSLP, we set URL to the "permalink" of this file, which is
        # its "reverse lookup" url, redirecting to the page of the composition with an anchor ref
        # to the file itself. In the case of this example, this is
        # https://imslp.org/wiki/Variations_and_Fugue_in_E-flat_major,_Op.35_(Beethoven,_Ludwig_van)#IMSLP52946
        url="https://imslp.org/wiki/Special:ReverseLookup/52946",
        # In IMSLP, we don't link directly to files with contenturl, because downloads on IMSLP are behind a disclaimer.
        # We expect that users would go from `source` and derive this themselves.
        # Because of this, we don't include the contenturl field
    )

    # Manually created MEI score
    imslp_mei = mediaobject.mutation_create_media_object(
        creator="https://github.com/trompamusic/trompa-ce-client/tree/master/demo",
        # Who this data came from
        contributor="https://iwk.mdw.ac.at",
        # URL on the web that matches contentUrl
        source="https://github.com/trompamusic-encodings/Beethoven_Op35_BreitkopfHaertel/blob/master/Beethoven_Op35.mei",
        # The <title> of `source`
        title="Beethoven_Op35_BreitkopfHaertel/Beethoven_Op35.mei at master · trompamusic-encodings/Beethoven_Op35_BreitkopfHaertel",
        # The mimetype of `source`
        format_="text/html",
        name="Beethoven_Op35.mei",
        # The page that describes the resource
        url="https://github.com/trompamusic-encodings/Beethoven_WoO80_BreitkopfHaertel",
        contenturl="https://raw.githubusercontent.com/trompamusic-encodings/Beethoven_Op35_BreitkopfHaertel/master/Beethoven_Op35.mei"
    )

    print("\nIMSLP MusicComposition and MediaObjects\n")
    if print_queries:
        print(imslp_musiccomposition)
        print(imslp_pdf)
        print(imslp_musicxml)
        print(imslp_mei)
    if submit_queries:
        pass

    work_id = "ddcaf601-80ea-49a9-ba7e-7f27b37da512"
    pdf_id = "a0ea5add-e30a-4fcc-ace3-25c6b8d2d307"
    xml_id = "66e70b8d-9d45-499a-ad91-1967caf66967"
    mei_id = "6d5491f7-6f74-4e77-814a-9f8ce4555a93"

    # All of the MediaObjects are examples of the MusicComposition
    example_of_work_pdf = mediaobject.mutation_merge_mediaobject_example_of_work(pdf_id, work_identifier=work_id)
    example_of_work_xml = mediaobject.mutation_merge_mediaobject_example_of_work(xml_id, work_identifier=work_id)
    example_of_work_mei = mediaobject.mutation_merge_mediaobject_example_of_work(mei_id, work_identifier=work_id)

    print("\nMediaObject - MusicComposition exampleOfWork\n")
    if print_queries:
        print(example_of_work_pdf)
        print(example_of_work_xml)
        print(example_of_work_mei)
    if submit_queries:
        pass

    # Add a relation between the XML and PDF only if you know that it is valid (see CPDL)

    # The MEI was created by transcribing the PDF, therefore it is is an encoding of the PDF
    pdf_encoding_mei = mediaobject.mutation_merge_media_object_encoding(pdf_id, mediaobject_derivative_identifier=mei_id)
    print("\nMediaObject - MediaObject encoding\n")
    if print_queries:
        print(pdf_encoding_mei)
    if submit_queries:
        pass

if __name__ == '__main__':
    from demo import args
    main(args.args.print, args.args.submit)
