songList = []
albumList = []
from pymongo import Connection
Connection=Connection('mongo.stuycs.org')
db = Connection.admin
res=db.authenticate('ml7','ml7')
db = Connection['MIBO']
Accounts = db.Accounts
SongRatings = db.SongRatings
AlbumRatings = db.AlbumRatings


def saveInfo(username, password):
    if Accounts.find({'usernames':username}).count() == 0:
        Accounts.insert({'usernames':username,'passwords':password})
        return True
    else:
        return False


def verifyLogin(username, password):
    if Accounts.find({'usernames':username,'passwords':password}).count() != 0:
        return True
    else:
        return False
def returnAllAccounts():
    accounts = []
    for account in Accounts.find():
        accounts.append('Username: '+str(account['usernames'])+'Password: '+str(account['passwords']))
    return accounts

 
#basic login method that verifies input username and password


def addSongRating(song,artist,rating,comment):
    ratingList = SongRatings.find_one({'song':song,'artist':artist})
    commentList = SongRatings.find_one({'song':song,'artist':artist})
    if ratingList == None:
        SongRatings.insert({'song':song,'artist':artist,'rating':[rating],'comment':[comment]})
    else:
        ratingList = ratingList['rating']
        commentList = commentList['comment']
        ratingList.append(rating)
        commentList.append(comment)
        SongRatings.update({'song':song,'artist':artist},{'$set':{'comment':commentList,'rating':ratingList}})

def addAlbumrating(album,artist,rating,comment):
    ratingList = AlbumRatings.find_one({'album':album,'artist':artist})
    commentList = AlbumRatings.find_one({'album':album,'artist':artist})
    if ratingList == None:
        AlbumRatings.insert({'album':album,'artist':artist,'rating':[rating],'comment':[comment]})
    else:
        ratingList = ratingList['rating']
        commentList = commentList['comment']
        ratingList.append(rating)
        commentList.append(comment)
        AlbumRatings.update({'album':album,'artist':artist},{'$set':{'comment':commentList,'rating':ratingList}})

    
def getSongRating(song,artist):
    return SongRatings.find_one({'song':song,'artist':artist})
def getAlbumRating(album,artist):
    return AlbumRatings.find_one({'album':album,'artist':artist})
#will return the rating of the song/album


def addSongRatingForUsername(username,password,song,artist,rating,comment):
    temp = ();
    temp.append(song)
    temp.append(artist)
    temp.append(rating)
    temp.append(comment)
    songList = Accounts.find_one({'usernames':username}):
    if songList == None:
        Accounts.insert({'usernames':username,'songlist':songlist})
    else:
        songList = songList['songlist']
        songList.append(temp)
        Accounts.update({'usernames':username},{'$set':{'songlist':songList}})
        



if __name__ == '__main__':
    pass;
