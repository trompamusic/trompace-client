from demo import send_query_and_get_id
from trompace.mutations import audioobject
from trompace import queries


def audio_file_liebestraum(print_queries, submit_queries):
    # A file that we're annotating

    audio = audioobject.mutation_create_audioobject(
        name="Liebestraum No. 3",
        title="Liebestraum No. 3",
        creator="https://github.com/trompamusic/audio-annotator",
        contributor="https://mtg.upf.edu/",
        source="https://trompa-mtg.upf.edu/data/anno-component-test/SMC_005.wav",
        format_="audio/wav",
        encodingformat="audio/wav",
        contenturl="https://trompa-mtg.upf.edu/data/anno-component-test/SMC_005.wav"
    )

    audio_id = "audio-node-id"
    print("AudioObject")
    if print_queries:
        print(audio)
    if submit_queries:
        audio_id = send_query_and_get_id(audio, "CreateAudioObject")

    return audio_id
