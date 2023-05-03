import functions as fn
import pandas as pd
import numpy as np


client_id = "c0106e614a6e4d2ebca46fd5401e7be4"
client_secret = "dfb41a1a744f416db305ca6185074c2d"

sp = fn.authManager(client_id, client_secret)
playList = fn.serchPlaylistByName(sp, "AllMyMind")
playlist_tracks = fn.getAllItems(sp, playList)
tracks = fn.getTracksData(playlist_tracks)

tracksData = pd.DataFrame(tracks)
print(tracksData)

features = fn.getAudioFeatures(sp, tracksData["Id Track"].tolist())
print(len(features))
