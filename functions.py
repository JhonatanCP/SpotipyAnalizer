import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def authManager(cliendId,secretId):
    auth_manager = SpotifyClientCredentials(client_id=cliendId, client_secret=secretId)
    return spotipy.Spotify(auth_manager=auth_manager)

def serchPlaylistByName(spotifyAuth,playlistName):
    playlists = spotifyAuth.search(q=playlistName, type='playlist')['playlists']['items']
    playlist_id = playlists[0]['id']
    return spotifyAuth.playlist_tracks(playlist_id, offset=0)

def getAllItems(spotifyAuth,playList):
    playlist_tracks = []
    cont = 0
    playlist_tracks += playList['items']

    print("Obteniendo Items....\n")
    while playList['next']:
        cont +=1
        playList = spotifyAuth.next(playList)
        playlist_tracks += playList['items']
        print(f"..Page {cont}..\n")
    print("Playlist completa")

    return playlist_tracks