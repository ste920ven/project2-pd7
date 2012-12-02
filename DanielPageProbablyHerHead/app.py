from flask import Flask, render_template, request, redirect, url_for, session
import db
#import api
from random import randint
import urllib2
import simplejson
import flickrapi

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    allAlbums = db.getImages()
    if request.method == 'POST':
         def newAlbumPicture():
             """
             Returns the URL of a random flickr image.
             """
            
             #API Call
             flickr = flickrapi.FlickrAPI(api_key = "c190109eeac99e777f3246f6da0f263a", format = "json")
            
             #To make the photo-picking more random, the "pickedPhotos" list is chosen from the most recent "interesting" photos on flickr 60% of the time, and the most recent public photos 40% of the time
             randNum = randint(0, 9)
             pickedPhotos = []
             if (randNum <= 5):
                 pickedPhotos = flickr.interestingness_getList()
             else: 
                 pickedPhotos = flickr.photos_getRecent()

             #Gets the list of the indices of the "id"s of the first 500 photos from pickedPhotos
             idIndices = []
             k = 0
             i = str(pickedPhotos).find('id')
             while k <= 1000:
                 idIndices.append(i)
                 i = str(pickedPhotos).find('id', i + 200)
                 k = k + 1

             #Randomly chooses a photo id out of the list of 500
             randNum = randint(0, len(idIndices) - 1)
             start = idIndices[randNum]

             #Gets the attributes of the photo whose id was selected
             id = str(pickedPhotos)[start + 5: start + 15]
             secret = str(pickedPhotos)[start + 52: start + 62]
             server = str(pickedPhotos)[start + 75: start + 79]
             farm = str(pickedPhotos)[start + 89: start + 90]

             #Checks if the attributes have valid values
             if (farm.isdigit() and server.isdigit() and id.isdigit()): 
             #Generates the URL based off of the attributes (the "_z" is a letter suffix for "medium image" )
                 URL = "http://farm" + str(farm) + ".staticflickr.com/" + str(server) + "/" + str(id) + "_" + str(secret) + "_z" + ".jpg"
                 return URL
             #If the values are not valid, then generates a new URL
             else:
                 return newAlbumPicture()
            
         button = request.form['button']
         if button == 'Save':
             db.addImage("http://farm9.staticflickr.com/8070/8234964776_708125d9a6_z.jpg")
             return render_template("index.html", allAlbums = allAlbums)
         if button == 'Edit':
             return render_template("index.html", allAlbums = allAlbums)
         if button == 'Generate':
             source = newAlbumPicture()
             return render_template("index.html", allAlbums = allAlbums, source = source)
    else:
        return render_template("index.html", allAlbums = allAlbums)
            
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7202, debug=True)

