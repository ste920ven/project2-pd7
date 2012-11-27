from pymongo import Connection

Connection = Connection('mongo.stuycs.org')
db = Connection.admin
res = db.authenticate('ml7','ml7')
db = Connection['z-pd7-DanielPageProbablyHerHead']
collection = db.collection

#Add's an image _url to the db
def addImage(_url):
	collection.insert({'image': str(_url), 'ratings': []})

#Add's a rating '_rating' to the image with the given _url
def addRating(_url, _rating):
	x = collection.find_one({'image': _url})['ratings']
	x.append(_rating)
	collection.update({'image': _url}, {'$set': {'ratings' : x}})

#Returns the list of ratings of the image with the given _url
def getRatings(_url):
	return collection.find_one({'image': _url})['ratings']

#Returns the one (averaged) rating of the image with the given _url
def getRating(_url):
	x = getRatings(_url);
	return ( sum(x) / collection.find_one({'image': _url})['ratings'].count() )
	