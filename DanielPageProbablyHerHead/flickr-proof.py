from random import randint
import flickrapi
#NOTE: This app requires the flickr api to run.
#Install with 'sudo apt-get install python-flickrapi'
api_key = "c190109eeac99e777f3246f6da0f263a"
api_secret = "f595faa22722ff96"

#Gets a list of the URLs of the most recent public photos uploaded to Flickr (I thought #this would be the best way to access random photos)

def getRecentPhotos(recentPhotoList):
	photoURLs = []
	for photo in recentPhotoList:
	   photoURLs.append("http://" + str(farm(photo['farm'])) + ".staticflickr.com/" + str(photo['server']) + "/" + str(photo['id'])+ "_" + str(photo['secret']) + ".jpg")
	return photoURLs

#Picks a random photo URL, given a list of photo URLs
def pickRandomPhoto(URLList):
	randNum = randint(0,len(URLListList)-1)
	print URLList[randNum]

def main():
	print "Random Photo URL:"
	flickr = flickrapi.FlickrApi(api_key = "c190109eeac99e777f3246f6da0f263a", format = "json")	
	photoList = flickr.photos_getRecent()
	pickRandomPhoto(getRecentPhotos(photoList))

if __name__ == '__main__':
	main()

#flickr = flickrapi.FlickrAPI(api_key, format='json')
#print flickr.photos_getRecent()