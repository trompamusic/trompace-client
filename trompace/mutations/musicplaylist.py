from trompace import StringConstant, check_required_args, docstring_interpolate, filter_none_args
from trompace.constants import SUPPORTED_LANGUAGES
from trompace.exceptions import NotAMimeTypeException, UnsupportedLanguageException
from trompace.mutations.templates import format_link_mutation, format_mutation


MUSICPLAYLIST_ARGS_DOCS = """name: The name of the MusicPlaylist object.
        creator: The person, organization or service who created the thing the web resource is about.
        contributor: A person, an organization, or a service responsible for contributing the MusicPlaylist to the web resource. This can be either a name or a base URL.
        format_: A MimeType of the format of the page describing the MusicPlaylist.
        source: The URL of the web resource about this MusicPlaylist.
        title: The title of the resource indicated by `source`
        numTracks: The number of tracks in the MusicPlaylist
        """


@docstring_interpolate("musicplaylist_args", MUSICPLAYLIST_ARGS_DOCS)
def mutation_create_musicplaylist(*, title: str, contributor: str, creator: str, source: str, format_: str,
                                  name: str = None, language: str = None, num_tracks: int = None):
    """Returns a mutation for creating a MusicPlaylist object.

    Arguments:
        {musicplaylist_args}

    Returns:
        The string for the mutation for creating the MusicPlaylist.
    """

    if "/" not in format_:
        raise NotAMimeTypeException(format_)

    if language is not None and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    args = {
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "format": format_,
        "name": name,
        "numTracks": num_tracks
    }
    if language is not None:
        args["language"] = StringConstant(language.lower())

    args = filter_none_args(args)

    return format_mutation("CreateMusicPlaylist", args)


@docstring_interpolate("musicplaylist_args", MUSICPLAYLIST_ARGS_DOCS)
def mutation_update_musicplaylist(identifier: str, *, title: str, contributor: str, creator: str, source: str,
                                  format_: str, name: str = None, language: str = None, num_tracks: int = None):
    """Returns a mutation for updating a MusicPlaylist object.

    Arguments:
        identifier: The identifier of the MusicPlaylist in the CE to be updated
        {musicplaylist_args}

    Returns:
        The string for the mutation for updating the MusicPlaylist.
    """
    if format_ is not None and "/" not in format_:
        raise NotAMimeTypeException(format_)

    if language is not None and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    args = {
        "identifier": identifier,
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "format": format_,
        "name": name,
        "numTracks": num_tracks
    }
    if language is not None:
        args["language"] = StringConstant(language.lower())

    args = filter_none_args(args)

    return format_mutation("UpdateMusicPlaylist", args)


def mutation_delete_musicplaylist(identifier: str):
    """Returns a mutation for deleting a musicplaylist object based on the identifier.

    Arguments:
        identifier: The unique identifier of the musicplaylist object.

    Returns:
        The string for the mutation for deleting the musicplaylist object based on the identifier.
    """

    return format_mutation("DeleteMusicPlaylist", {"identifier": identifier})


def mutation_merge_musicplaylist_musicrecording(playlist_identifier: str, musicrecording_identifier: str):
    """Returns a mutation for adding a musicrecording as a track of a playlist.

    Arguments:
        playlist_identifier: The unique identifier of the playlist.
        musicrecording_identifier: The unique identifier of the musicrecording that is part of the playlist.

    Returns:
        The string for the mutation for merging a musicrecording as part of a playlist.
    """

    return format_link_mutation("MergeMusicPlaylistTrack", playlist_identifier, musicrecording_identifier)


def mutation_remove_musicplaylist_musicrecording(playlist_identifier: str, musicrecording_identifier: str):
    """Returns a mutation for removing a musicrecording as a track of a playlist.

    Arguments:
        playlist_identifier: The unique identifier of the playlist.
        musicrecording_identifier: The unique identifier of the musicrecording that is part of the playlist.

    Returns:
        The string for the mutation for removing a musicrecording as part of a playlist.
    """

    return format_link_mutation("RemoveMusicPlaylistTrack", playlist_identifier, musicrecording_identifier)


def mutation_merge_musicplaylist_itemlist(playlist_identifier: str, itemlist_identifier: str):
    """Returns a mutation for adding an ItemList of MusicRecordings as the track list of a Playlist.

    Arguments:
        playlist_identifier: The unique identifier of the Playlist.
        itemlist_identifier: The unique identifier of the ItemList that contains the playlist's tracks.

    Returns:
        The string for the mutation for merging an ItemList as part of a playlist.
    """

    return format_link_mutation("MergeMusicPlaylistTrackItemList", playlist_identifier, itemlist_identifier)


def mutation_remove_musicplaylist_itemlist(playlist_identifier: str, itemlist_identifier: str):
    """Returns a mutation for removing an ItemList of MusicRecordings as the track list of a Playlist.

    Arguments:
        playlist_identifier: The unique identifier of the Playlist.
        itemlist_identifier: The unique identifier of the ItemList that contains the playlist's tracks.

    Returns:
        The string for the mutation for removing an ItemList as part of a playlist.
    """

    return format_link_mutation("RemoveMusicPlaylistTrackItemList", playlist_identifier, itemlist_identifier)

