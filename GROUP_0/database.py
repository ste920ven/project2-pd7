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
        Accounts.insert({'usernames':username,'passwords':password,'songList':[],'albumList':[]})
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


def addSongRating(username,song,artist,rating,comment):
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
    addSongRatingForUsername(username,song,artist,rating,comment)

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
    addAlbumRatingForUsername(username,album,artist,rating,comment)

    
def getSongRating(song,artist):
    return SongRatings.find_one({'song':song,'artist':artist})
def getAlbumRating(album,artist):
    return AlbumRatings.find_one({'album':album,'artist':artist})
#will return the rating of the song/album


def addSongRatingForUsername(username,song,artist,rating,comment):
    temp = song,artist,rating,comment
    songList = Accounts.find_one({'usernames':username})
    if songList == None:
        songList = [temp]
        Accounts.update({'usernames':username},{'$set':{'songList':songList}})
    else:
        songList = songList['songList']
        if songList == None:
            songList = [temp]
            Accounts.update({'usernames':username},{'$set':{'songList':songList}})
        else:
            songList.append(temp)
            Accounts.update({'usernames':username},{'$set':{'songList':songList}})

def addAlbumRatingForUsername(username,album,artist,rating,comment):
    temp = album,artist,rating,comment
    albumList = Accounts.find_one({'usernames':username})
    if albumList == None:
        albumList = [temp]
        Accounts.update({'usernames':username},{'$set':{'albumList':albumList}})
    else:
        albumList = albumList['albumList']
        if albumList == None:
            albumList = [temp]
            Accounts.update({'usernames':username},{'$set':{'albumList':albumList}})
        else:
            albumList.append(temp)
            Accounts.update({'usernames':username},{'$set':{'albumList':albumList}})


def getSongRatingsByUser(username):
    return Accounts.find_one({'usernames':username})['songList']

def getAlbumRatingsByUser(username):
    return Accounts.find_one({'usernames':username})['albumList']



if __name__ == '__main__':
    pass
