from pymongo import Connection

Connection = Connection('mongo.stuycs.org')
db = Connection.admin
res = db.authenticate('ml7','ml7')
db = Connection['z-pd7-DanielPageProbablyHerHead']
collection = db.collection

#Adds an image _url to the db
def addImage(_url):
	collection.insert({'image': str(_url), 'ratings': []})

#Adds a rating '_rating' to the image with the given _url
def addRating(_url, _rating):
	x = collection.find_one({'image': _url})['ratings']
	x.append(_rating)
	collection.update({'image': _url}, {'$set': {'ratings' : x}})

#Returns the list of ratings of the image with the given _url
def getRatings(_url):
	return collection.find_one({'image': _url})['ratings']

#Returns the one (averaged, and rounded to the nearest half) rating of the image with the given _url
def getRating(_url):
	x = getRatings(_url)
        y = 0.0
	for rating in x:
		y = y + int(rating) #cast to int because the ratings are unicode
	z = len(collection.find_one({'image': _url})['ratings'])
	return (round((y / z) * 2, 0) / 2)

#Removes the image with the given _url
def removeImage(_url):
	collection.remove({'image' : _url})

#Removes all the ratings for the image with the given _url
def deleteRatings(_url):
	removeImage(_url)
	addImage(_url)

#Returns all image URLs in the database
def getImages():
	images = []
	results = collection.find()
	for line in results:
		images.append("\"" + line['image'] + "\"")
	return images

#Returns true if the _url is in the db, false otherwise
def isInDb(_url):
	results = collection.find()
	for line in results:
		if (line['image'] == _url):
			return True
		else:
			return False

#Returns the image and ratings with the _url (for unittesting purposes)
def returnImage(_url):
	return collection.find_one({'image' : _url})

#Removes all the image URLs and ratings from the database
def wipeDatabase():
	for line in collection.find():
		removeImage(line['image'])

if __name__ == "__main__":
	wipeDatabase()
	
	
