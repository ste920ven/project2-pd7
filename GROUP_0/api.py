import json
#from bs4 import BeautifulSoup
import urllib2

'''
apikey="FILDTEOIK2HBORODV"

url="http://developer.echonest.com/api/v4/song/search?api_key=FILDTEOIK2HBORODV&sort=song_hotttnesss-desc&bucket=song_hotttnesss"

request=urllib2.urlopen(url)
result=json.loads(request.read())
print result

#somehow echonest api has some repeated data; when i searched for top songs, the api returns the same song title multiple times
popular_songs=result["response"]["songs"]
popularity=[]
artist=[]
song_title=[]
for item in popular_songs:
    popularity.append(item["song_hotttnesss"])
    artist.append(item["artist_name"])
    song_title.append(item["title"])
'''
apikey="nxs4nu8b9u3ekhuv5gfynr7s"
#3 different charts:album, track, artist
track_url=http://api.emusic.com/track/charts?apiKey=nxs4nu8b9u3ekhuv5gfynr7s&format=json
album_url=http://api.emusic.com/album/charts?apiKey=nxs4nu8b9u3ekhuv5gfynr7s&format=json
artist_url=http://api.emusic.com/artist/charts?apiKey=nxs4nu8b9u3ekhuv5gfynr7s&format=json
