from random import randint
import flickrapi
#NOTE: This app requires the flickr api to run.
#Install with 'sudo apt-get install python-flickrapi'
api_key = "c190109eeac99e777f3246f6da0f263a"
api_secret = "f595faa22722ff96"

#Gets a list of the URLs of the most recent public photos uploaded to Flickr (I thought #this would be the best way to access random photos)

def getRecentPhotos(recentPhotoList):
	for photo in recenPhotoList:
	   print "http://farm(photo['farm']).staticflickr.com/(photo['server'])/(photo['id'])_(photo['secret']).jpg"

#Picks a random photo URL, given a list of photo URLs
def pickRandomPhoto(photoList):
	randNum = randint(0,len(photoList)-1)
	print photoList[randNum]

def main():
	print "Random Photo URL:"
	flickr = flickrapi.FlickrAPI(api_key)
	recentPics = flickr.photos_getRecent()
	pickRandomPhoto(getRecentPhotos(recentPics))

#if __name__ == '__main__':
#	main()

flickr = flickrapi.FlickrAPI(api_key, format='json')
print flickr.photos_getRecent()

