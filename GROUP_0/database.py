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
    addSongRatingForUsername(username,song,artist,rating,comment)
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


def addAlbumrating(username,album,artist,rating,comment):
    addAlbumRatingForUsername(username,album,artist,rating,comment)
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
    tmp= SongRatings.find_one({'song':song,'artist':artist})
    return tmp
def getAlbumRating(album,artist):
    tmp= AlbumRatings.find_one({'album':album,'artist':artist})
    return tmp


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

def getAverageRating(album,artist):
    ratings=getAlbumRating(album,artist)["rating"]
    sum=0
    for item in ratings:
        sum=int(item)+sum
    average=sum/(len(ratings)+1)
    return average

def getAverageSongRating(song,artist):
    ratings=getSongRating(song,artist)["rating"]
    sum=0
    for item in ratings:
        sum=int(item)+sum
    average=sum/(len(ratings)+1)
    return average



def getSongRatingsByUser(username):
    return Accounts.find_one({'usernames':username})['songList']

def getAlbumRatingsByUser(username):
    return Accounts.find_one({'usernames':username})['albumList']



if __name__ == '__main__':
    for stuff in Accounts.find():
        print stuff
