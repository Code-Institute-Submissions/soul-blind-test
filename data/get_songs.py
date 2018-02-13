#This script helps me create an array of songs&artists that I will randomly select for the blind test

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint

client_credentials_manager = SpotifyClientCredentials(client_id='5f72500ee6974d9bb1eba4a7e91e3255', client_secret='ae1f2e296e094e778fe385837ab2d48e')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


#Create a dictionary of selected soul music artists and their spotify ids
featured_artists = {
    'aretha' : '7nwUJBm0HE4ZxD3f5cy5ok',
    'ray' : '1eYhYunlNJlDoQhtYBvPsi',
    'ronettes' : '7CyeXFnOrfC1N6z4naIpgo',
    'supremes' : '57bUPid8xztkieZfS7OlEV',
    'marvin' : '3koiLjNrgRTNbOwViDipeA',
    'stevie' : '7guDJrEfX3qb6FEbdPA5qi',
    'etta' : '0iOVhN3tnSvgDbcg25JoJb',
    'otis' : '60df5JBRRPcnSpsIMxxwQm',
    'bill' : '1ThoqLcyIYvZn7iWbj8fsj',
    'al':'3dkbV4qihUeMsqN4vBGg93',
    'tempt': '3RwQ26hR2tJtA8F9p2n7jG',
    'sam': '6hnWRPzGGKiapVX1UCdEAC',
    'nina': '7G1GBhoKtEPnP86X2PvEYO'
}

#This array will contain a list of the top 10 tracks for each featured artiste
list_of_tracks = []

#loops over each artist and adds the relevant info to my list of track array if they have a preview url 
for artist, key in featured_artists.items():
    tracks = sp.artist_top_tracks(key)
    for track in tracks["tracks"]: 
        if track['preview_url'] :
            track_dict = {}
            track_dict['title'] = track['name']
            track_dict['artist'] = track['artists'][0]['name']
            track_dict['preview_url'] = track['preview_url']
            track_dict['album_name'] = track["album"]["name"]
            track_dict["album_img"] = track["album"]["images"][0]
            list_of_tracks.append(track_dict)

with open('data/songs.py', 'w') as f:
    f.write("songs_array={}".format(list_of_tracks))





