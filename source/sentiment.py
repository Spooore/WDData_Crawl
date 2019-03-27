import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '74f770b5e1244273b2a9ec31040a3628'
client_secret = 'aaa03eb6c6a249b48486c9fc5ac144b2'

def GetTrackId(_title,_artist):
    title = _title
    artist = _artist

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp.trace=False
    search_querry = title + ' ' + artist
    result = sp.search(search_querry)
    for i in result['tracks']['items']:
        if (i['artists'][0]['name'] == artist) and (i['name'] == title):
            return (i['uri'])
    else:
        try:
            return (result['tracks']['items'][0]['uri'])
        except:
            return ("Cannot Find URI")


def GetMood(_id):
    output=[]
    if _id=="Cannot Find URI":
        output.append(str(-1))
        output.append(str(-1))
        return output
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp.trace=False
    features = sp.audio_features(_id)
    output.append(str(features[0]['energy']))
    output.append(str(features[0]['valence']))
    return output