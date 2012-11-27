import json
import urllib2

apikey="nxs4nu8b9u3ekhuv5gfynr7s"

#3 different charts: album, track, artist, but i just used the chart for track
track_url="http://api.emusic.com/track/charts?apiKey=nxs4nu8b9u3ekhuv5gfynr7s&format=json"
album_url="http://api.emusic.com/album/charts?apiKey=nxs4nu8b9u3ekhuv5gfynr7s&format=json"
artist_url="http://api.emusic.com/artist/charts?apiKey=nxs4nu8b9u3ekhuv5gfynr7s&format=json"


def create_album():
    album={}
    request=urllib2.urlopen(album_url)
    result=json.loads(request.read())
    for item in result["albums"]:
        album_title=item["name"].encode('ascii','ignore')
        album[album_title]={"genre":item["genre"]["name"].encode('ascii','ignore'),"image":item["image"].encode('ascii','ignore'),"label":item["label"]["name"].encode('ascii','ignore'),"ratings":item["ratings"]["communityRating"]["average"].encode('ascii','ignore'),"url":item["url"].encode('ascii','ignore'),"artist":item["artist"]["name"],"date":item["released"]}
    return album

def create_artist():
    artist={}
    request=urllib2.urlopen(artist_url)
    result=json.loads(request.read())
    for item in result["artists"]:
        artist_name=item["name"].encode('ascii','ignore')
        artist[artist_name]={"url":item["url"].encode('ascii','ignore'), "id":item["id"]}
    return artist

def create_song():
    song={}
    request=urllib2.urlopen(track_url)
    result=json.loads(request.read())
    for item in result["tracks"]:
        song_title=item["name"].encode('ascii','ignore')
        album=item["album"]
        song[song_title]={"album":album["name"].encode('ascii','ignore'),"artist":album["artist"]["name"].encode('ascii','ignore'),"genre":album["genre"]["name"].encode('ascii','ignore'),"label":album["label"]["name"].encode('ascii','ignore'),"image":album["image"].encode('ascii','ignore'),"id":album["id"], "url":album["url"].encode('ascii','ignore')}
    return song

