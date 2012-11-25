usernames = []
passwords = []
#songRatings = []
#albumRatings = []
songList = []
albumList = []


def saveInfo(username, password):
    if username in usernames:
        return false
    else:
        usernames.append(username)

    passwords.append(password)



#We will take input on from the register page and "save" it by putting the username and password in their respective lists


def verifyLogin(username, password):
    if username in usernames:                                       
        if password in passwords:
            i = usernames.index(username)        #@Brian <---- what I was talking about
            if passwords[i]==password:
                return true
            else:
                return false
                

 
#basic login method that verifies input username and password


def addSong(song):


def addAlbum(album):


def addSongRating(song):
    
def addAlbumRating(album):
        

def getSongRating(song):

def getAlbumRating(album):

#will return the rating of the song/album
    




        
    
