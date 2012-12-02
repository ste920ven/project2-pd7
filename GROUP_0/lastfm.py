import json
import urllib2

apikey="84eab4b0fd50899cd57ed395c3a628dc"

#3 different charts: album, track, artist, but i just used the chart for track
track_url="http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag=disco&api_key=439d19b5d282ca8a3285bd9258be7e72&format=json"
album_url="http://ws.audioscrobbler.com/2.0/?method=tag.gettopalbums&tag=disco&api_key=439d19b5d282ca8a3285bd9258be7e72&format=json"

def create_album():
    album={}
    request=urllib2.urlopen(album_url)
    result=json.loads(request.read())
    for item in result["topalbums"]["album"]:
        album_title=item["name"].encode('ascii','ignore')
        album[album_title]={"image":item["image"][3]["#text"].encode('ascii','ignore'),"rank":item["@attr"]["rank"].encode('ascii','ignore'),"url":item["url"].encode('ascii','ignore'),"artist":item["artist"]["name"],"artist url":item["artist"]["url"].encode('ascii','ignore')}
    return album

def create_song():
    song={}
    request=urllib2.urlopen(track_url)
    result=json.loads(request.read())
    for item in result["toptracks"]["track"]:
        song_title=item["name"].encode('ascii','ignore')
        song[song_title]={"artist":item["artist"]["name"].encode('ascii','ignore'),"image":item["image"][3]["#text"].encode('ascii','ignore'),"url":item["url"].encode('ascii','ignore'),"artist url":item["artist"]["url"].encode('ascii','ignore'),"rank":item["@attr"]["rank"].encode('ascii','ignore')}
    return song

def create_album_images():
    album=create_album()
    images=[]
    for key in album.keys():
        images.append(album[key]["image"])
    return images

def create_song_images():
    song=create_song()
    images=[]
    for key in song.keys():
        images.append(song[key]["image"])
    return images
if __name__ == "__main__":
    pass
