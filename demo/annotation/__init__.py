from demo import send_query_and_get_id
from trompace.mutations import audioobject
from trompace.queries import audioobject as query_audioobject


def audio_file_liebestraum(print_queries, submit_queries):
    # A file that we're annotating

    contenturl = "https://trompa-mtg.upf.edu/data/anno-component-test/SMC_005.wav"

    get_audio = query_audioobject.query_audioobject(contenturl=contenturl)
    if submit_queries:
        audio_id = send_query_and_get_id(get_audio, "AudioObject")
        if audio_id:
            print("get AudioObject")
            if print_queries:
                print(get_audio)
            return audio_id[0]

    audio = audioobject.mutation_create_audioobject(
        name="Liebestraum No. 3",
        title="Liebestraum No. 3",
        creator="https://github.com/trompamusic/audio-annotator",
        contributor="https://mtg.upf.edu/",
        source=contenturl,
        format_="audio/wav",
        encodingformat="audio/wav",
        contenturl=contenturl
    )

    audio_id = "audio-node-id"
    print("AudioObject")
    if print_queries:
        print(audio)
    if submit_queries:
        audio_id = send_query_and_get_id(audio, "CreateAudioObject")

    return audio_id


def audio_file_pierri_etude(print_queries, submit_queries):
    # A file that we're annotating

    contenturl = "https://trompa-mtg.upf.edu/data/anno-component-test/SMC_015.wav"

    get_audio = query_audioobject.query_audioobject(contenturl=contenturl)
    if submit_queries:
        audio_id = send_query_and_get_id(get_audio, "AudioObject")
        if audio_id:
            print("get AudioObject")
            if print_queries:
                print(get_audio)
            return audio_id[0]

    audio = audioobject.mutation_create_audioobject(
        name="Pierri Etude no. 4",
        title="Pierri Etude no. 4",
        creator="https://github.com/trompamusic/audio-annotator",
        contributor="https://mtg.upf.edu/",
        source=contenturl,
        format_="audio/wav",
        encodingformat="audio/wav",
        contenturl=contenturl
    )

    audio_id = "audio-node-id"
    print("AudioObject")
    if print_queries:
        print(audio)
    if submit_queries:
        audio_id = send_query_and_get_id(audio, "CreateAudioObject")

    return audio_id
