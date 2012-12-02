from random import randint
import flickrapi
#This app requires the flickr api to run.
#install with 'sudo apt-get install python-flickrapi'
import urllib2
import simplejson

"""
api.py houses all of our code that deals with web APIs.
The Flickr API will be added soon.
"""
def newArtistName():
    """
    Returns a new artist name (the title of a random wikipedia article).
    Filters out articles that would be bad names- maximum length is 48 chars because of this:
    http://musicmachinery.com/2012/01/07/have-artist-names-been-getting-longer/
    """

    #API call
    request=urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=query&format=json&generator=random&redirects=&grnnamespace=0&grnlimit=1")
    result = simplejson.loads(request.read())

    #figures out which part of the json is the title
    start = str(result).find('title',0)
    if str(result).find("'}}}}") != -1:
        end = str(result).find("'}}}}")
    else:
        end = str(result).find("\"}}}}")
    title = str(result)[start+9:end]
   
    #if the title has weird characters or is too long, return another one
    if title.find("\\u") != -1 or title.find("\\x") != -1 or title.find("(") != -1 or len(title) > 48:
        #print "recursion is awesome"
        return newArtistName()
    else:
        return title

def newAlbumName():
    """
    Returns a new album name (the last three words of a random quote from iheartquotes).
    Filters out quotes that are too short or would be bad names.
    """

    #API Call
    request=urllib2.urlopen("http://www.iheartquotes.com/api/v1/random?format=json&source=literature")
    result = simplejson.loads(request.read())
    
    #figures out which part of the json is the quote
    start = str(result).find('quote',0)
    end = str(result).find(", 'link'", start + 9)
    quote = str(result)[start+9:end-1]

    #formats the quote nicely so we don't get any weird album names
    quote = quote.replace("\\n", " ")
    quote = quote.replace("\\t", "")
    quote = quote[:quote.find("--")]
    quote = quote.strip()
    quote = quote.replace("\"", "")
    quote = quote.replace(".", "")
    
    #if the quote has weird characters or is too short, return another one
    if quote.find("(") != -1 or len(quote.split()) < 5:
        #print "recursion is awesome"
        return newAlbumName()
    quote = quote.split()[-4] + " " + quote.split()[-3] + " " + quote.split()[-2] + " " + quote.split()[-1]
    return quote

def newAlbumPicture():
    """
    Returns the URL of a random flickr image.
    """

    #API Call
    flickr = flickrapi.FlickrAPI(api_key = "c190109eeac99e777f3246f6da0f263a", format = "json")

    #Gets the list of the most recently added public photos on flickr
    recentPhotos = flickr.photos_getRecent()

    #Gets the index of the first photo "id" of the recentPhotos (this will be random, as each call to newAlbumPicture will produce a different list of photos)
    i = str(recentPhotos).find('id')

    #Gets all the photo (with id = "id") attribute values, based off the id, or "start", index
    start = i
    id = str(recentPhotos)[start + 5: start + 15]
    secret = str(recentPhotos)[start + 52: start + 62]
    server = str(recentPhotos)[start + 75: start + 79]
    farm = str(recentPhotos)[start + 89: start + 90]

    #Generates the photo URL based off of the attributes (the "_z" is a letter suffix for "medium image" )
    URL = "http://farm" + str(farm) + ".staticflickr.com/" + str(server) + "/" + str(id) + "_" + str(secret) + "_z" + ".jpg"    
    return URL


if __name__ == '__main__':
    print "Title:" + newArtistName()
    print "Quote:" + newAlbumName()
    print "Image URL:" + newAlbumPicture()


