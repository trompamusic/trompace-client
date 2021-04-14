from typing import Optional
from trompace.config import config
from trompace.connection import submit_query
from trompace.client import client_itemlist
from trompace.mutations import musicplaylist as mutations_playlist
from trompace.exceptions import QueryException, IDNotFoundException


def create_musicplaylist_node(title: str, contributor: str, creator: str, 
                              source: str, format_: str, name: str = None, 
                              language: str = None, num_tracks: int = None):
    """Create a MusicPlaylist object and return the corresponding identifier.
    (https://schema.org/MusicPlaylist)

    Arguments:
        name: The name of the MusicPlaylist object.
        creator: The person, organization or service who created the 
                 thing the web resource is about.
        contributor: A person, an organization, or a service responsible f
                     for contributing the MusicPlaylist to the web resource. 
                     This can be either a name or a base URL.
        format_: A MimeType of the format of the page describing the MusicPlaylist.
        source: The URL of the web resource about this MusicPlaylist.
        title: The title of the resource indicated by `source`
        numTracks: The number of tracks in the MusicPlaylist
    Raises:
        QueryException if the query fails to execute
    Returns:
        The identifier of the MusicPlaylist object created
    """

    mutation = mutations_playlist.mutation_create_musicplaylist(
                                                    title=title,
                                                    contributor=contributor, 
                                                    creator=creator, 
                                                    source=source, 
                                                    format_=format_,
                                                    name=name, 
                                                    language=language, 
                                                    num_tracks=num_tracks)

    resp = submit_query(mutation)
    result = resp.get("data", {}).get("CreateMusicPlaylist")

    if result:
        playlist_id = result["identifier"]
    else:
        raise QueryException(resp['errors'])

    return playlist_id


def merge_musicplaylist_itemlist(playlist_id: str, itemlist_id:str ):
    """Add a ItemList to a MusicPlaylist based on the identifiers.
    (https://schema.org/MusicPlaylist)

    Arguments:
        playlist_id: the MusicPlaylist identifier.
        itemlist_id: the ItemList identifier.
    Raises:
        QueryException if the query fails to execute
    """

    mutation = mutations_playlist.mutation_merge_musicplaylist_itemlist(playlist_identifier=playlist_id,
                                                                        itemlist_identifier=itemlist_id)
    resp = submit_query(mutation)
    result = resp.get("data", {})

    if not result:
        raise QueryException(resp['errors'])


def create_playlist(title: str, contributor: str, creator: str, ordered: bool,
                    source: str, format_: str, description: str, recordings_ids: list = None, 
                    name: str = None, language: str = None, num_tracks: int = None):
    """
    """
    listitems = []
    ids_mode = True
    if not recordings_ids:
        raise ValueError("must provide recording_ids")
    elif num_tracks:
        if num_tracks != len(recordings_ids):
            raise ValueError("num_tracks does not match with input recordings")
    elif not num_tracks:
        num_tracks = len(recordings_ids)
    
    not_found = client_itemlist.get_nonexistent_listitem_nodes(recordings_ids)
    if not_found:
        raise IDNotFoundException(not_found)
    else:
        [listitems.append(x) for x in recordings_ids if x not in listitems]


    playlist_id = create_musicplaylist_node(title=title,
                                            contributor=contributor, 
                                            creator=creator, 
                                            source=source, 
                                            format_=format_,
                                            name=name, 
                                            language=language, 
                                            num_tracks=num_tracks)


    
    itemlist_id = client_itemlist.create_itemlist_node(creator=creator,
                                                       contributor=contributor,
                                                       name=name,
                                                       description=description,
                                                       ordered=ordered)

    merge_musicplaylist_itemlist(playlist_id, itemlist_id)


    listitems_ids = client_itemlist.create_sequence_listitem_nodes(name=name,
                                                                    listitems=listitems,
                                                                    ids_mode=ids_mode,
                                                                    contributor=contributor)

    client_itemlist.merge_sequence_itemlist_itemlistelement_nodes(itemlist_id=itemlist_id,
                                                                  element_ids=listitems_ids)

    client_itemlist.merge_sequence_listitem_nextitem_nodes(listitem_ids=listitems_ids)


    client_itemlist.merge_sequence_listitem_item_nodes(listitem_ids=listitems_ids,
                                                       item_ids=recordings_ids)
