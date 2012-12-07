#!usr/bin/python                                                                                                                               

from pymongo import Connection
Connection = Connection('mongo.stuycs.org')

def connect():
        """ Handles connecting to mongo.stuycs.org, authentication, and connecting to our (Group_6) database. Returns our database.    
        """
        DB = Connection.admin
        res = DB.authenticate('ml7','ml7')
        DB = Connection['Group_6']
        return DB       
        


def getTaglist():
        """ Returns a list of all of the tags used
        """
        DB = connect()
        list = DB.tags.find({"tag" : "tag"})[0]['tags']
        print list
        return list
        
        

def getTags(picture):
        """ Returns a list of tags associated with a picture
        """
        DB = connect()
        tags = DB.pictures.find({"picture" : picture})[0]['tags']
        print tags
        return tags
        
def addTag(picture,tag):
        """ Adds a tag to the picture
        """
        DB = connect()
        DB.pictures.update({"picture" : picture}, {"$push": {"tags":tag}})
        DB.tags.update({"tag":"tag"},{"$push":{"tags":tag}})

def getComments(picture):
        """ Returns a list of all the comments associated with the picture
        """
        DB = connect()
        comments = DB.pictures.find({"picture" : picture})[0]['comments']
        print comments
        return comments

def addComment(picture,comment):
        """ Adds a comment to the picture
        """
        DB = connect()
        DB.pictures.update({"picture" : picture},{"$push":{"comments":comment}})

def getPictures(tag):
        """ Returns a list of pictures with the tag
        """
        ans = []
        DB = connect()
        # ans=[x["picture"] for x in collection.find({"tags":tag})]
        for x in DB.pictures.find():
            picture = x["tags"]
            if tag in picture:
                ans.append(x["picture"])
        print ans
        return ans

def addPicture(picture):
        """ Adds a picture to the database
        """
        DB = connect()
        DB.pictures.insert({"picture":picture,"comments":[],"tags":["Sandy"]})

        
if __name__=="__main__":
    mydb = db()
    print mydb.db
    mydb.addPicture("http://b.vimeocdn.com/ps/101/290/1012902_300.jpg");

