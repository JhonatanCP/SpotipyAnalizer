import spotipy
import functions as fn
import pandas as pd
import numpy as np

from spotipy.oauth2 import SpotifyClientCredentials


client_id = 'c0106e614a6e4d2ebca46fd5401e7be4'
client_secret = 'dfb41a1a744f416db305ca6185074c2d'

sp = fn.authManager(client_id,client_secret)
playList = fn.serchPlaylistByName(sp,'AllMyMind')
playlist_tracks = fn.getAllItems(sp,playList)

tracks= []

for track in playlist_tracks:

    albumName = track['track']['album']['name']
    trackName = track['track']['name']
    artistsName = track['track']['artists'][0]['name']
    durationMs = track['track']['duration_ms']
    popularity = track['track']['popularity']
    # audio_features = sp.audio_features(track['track']['id'])[0]

    # audio_features.pop('type')
    # audio_features.pop('id')
    # audio_features.pop('uri')
    # audio_features.pop('track_href')
    # audio_features.pop('analysis_url')
    # audio_features.pop('duration_ms')

    tracks.append({'Album Name':albumName,'Track Name': trackName, 'Artist Name': artistsName, 'Duration in ms': durationMs,'Popularity': popularity} )

df2 = pd.DataFrame(tracks)
print(df2)



