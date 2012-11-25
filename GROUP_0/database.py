songList = []
albumList = []
from pymongo import Connection
Connection=Connection('mongo.stuycs.org')
db = Connection.admin
res=db.authenticate('ml7','ml7')
db = Connection['MIBO']
collection = db.collection1


def saveInfo(username, password):
    if collection.find({'usernames':username}).count() == 0:
        collection.insert({'usernames':username,'passwords':password})
        return True
    else:
        return False


def verifyLogin(username, password):
    if collection.find({'usernames':username,'passwords':password}).count() != 0:
        return True
    else:
        return False
def returnAllAccounts():
    Accounts = []
    for account in collection.find():
        Accounts.append('Username: '+str(account['usernames'])+'Password: '+str(account['passwords']))
    return Accounts

 
#basic login method that verifies input username and password


def addSong(song):
    pass

def addAlbum(album):
    pass

def addSongRating(song):
    pass
def addAlbumRating(album):
    pass

def getSongRating(song):
    pass
def getAlbumRating(album):
    pass
#will return the rating of the song/album
    


if __name__ == '__main__':
    saveInfo('briantotheyanyan','BY4695')
    saveInfo('briantotheyanyan','brian4695')
    saveInfo('briantotheyanyan','HI')
    saveInfo('IVANISAWESOME','YAH')
    saveInfo('THANKYOUMENGDIFORYOURHELP','YAH')
    print returnAllAccounts()
    print verifyLogin('briantotheyanyan','BY4695')
    print verifyLogin('briantotheyanyan','brian4695')

        
    
