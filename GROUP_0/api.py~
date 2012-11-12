import json
import urllib2

apikey="nxs4nu8b9u3ekhuv5gfynr7s"

#3 different charts: album, track, artist, but i just used the chart for track
track_url="http://api.emusic.com/track/charts?apiKey=nxs4nu8b9u3ekhuv5gfynr7s&format=json"
album_url="http://api.emusic.com/album/charts?apiKey=nxs4nu8b9u3ekhuv5gfynr7s&format=json"
artist_url="http://api.emusic.com/artist/charts?apiKey=nxs4nu8b9u3ekhuv5gfynr7s&format=json"

#a dictionary called song that has song_title as key. Whenever you search for a song title, the dictionary will return song's album, artist, genre, label, and image of the album.
def create_song_dict():
    request=urllib2.urlopen(track_url)
    result=json.loads(request.read())
    song={}
    for item in result["tracks"]:
        song_title=item["name"]
        album=item["album"]
        song[song_title]={"album":album["name"],"artist":album["artist"]["name"],"genre":album["genre"]["name"],"label":album["label"]["name"],"image":album["image"],"id":album["id"], "song url":album["url"]}
    #print song
    return song
<<<<<<< HEAD
def print_song_title():
    x = create_song_dict()
    a=[]
    for p in x:
       if a == None:
            a = [p]
       else:
            a.append(p)
    return a
'''
def create_rating_dict():
    rating_url="http://api.emusic.com/album/ratings?apiKey=nxs4nu8b9u3ekhuv5gfynr7s&format=json&albumId="
    for key in song.keys():
        new_url=rating_url+str(song[key]["id"])
        print new_url
        break
        request=urllib2.urlopen(new_url)
        result=json.loads(request.read())
        song[key]["rating"]=result["album"]["ratings"]["communityRating"]["average"]
    for key in song.keys():
        print song[key]["ratings"]

create_song_dict()
create_rating_dict()

'''

if __name__ == "__main__":
    print print_song_title()
=======
>>>>>>> a4dce0fedd5aefada73635623a3a0e4c9520b6dc
