import unittest
import imageDatabase

class TestSequenceFunctions(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		imageDatabase.wipeDatabase()

	def test_addImage(self):
		imageDatabase.addImage("test")
		self.assertEqual(imageDatabase.returnImage("test")['image'], "test")

	def test_addRating(self):
		imageDatabase.wipeDatabase()
		imageDatabase.addImage("test")
		imageDatabase.addRating("test", "4")
		ratings = imageDatabase.returnImage("test")['ratings']
		self.assertEqual(ratings[0], "4")

	def test_getRatings(self):
		imageDatabase.wipeDatabase()
		imageDatabase.addImage("test")
		imageDatabase.addRating("test", "4")
		imageDatabase.addRating("test", "3")
		ratings = imageDatabase.getRatings("test")
		numRatings = len(ratings)
		self.assertEqual(numRatings, 2)
	
	def test_getRating(self):
		imageDatabase.wipeDatabase()
		imageDatabase.addImage("test")
		imageDatabase.addRating("test", "5")
		imageDatabase.addRating("test", "3")
		rating = imageDatabase.getRating("test")
		self.assertEqual(rating, 4)

	def test_removeImage(self):
		imageDatabase.wipeDatabase()
		imageDatabase.addImage("test")
		imageDatabase.removeImage("test")
		self.assertEqual(imageDatabase.returnImage("test"), None)

	def test_deleteRatings(self):
		imageDatabase.wipeDatabase()
		imageDatabase.addImage("test")
		imageDatabase.addRating("test", "4")
		imageDatabase.addRating("test", "3")
		imageDatabase.deleteRatings("test")
		ratings = imageDatabase.getRatings("test")
		numRatings = len(ratings)
		self.assertEqual(numRatings, 0)

	def test_getImages(self):
		imageDatabase.wipeDatabase()
		imageDatabase.addImage("test1")
		imageDatabase.addImage("test2")
		imageDatabase.addImage("test3")
		numImages = imageDatabase.getImages()
		self.assertEqual(len(numImages), 3)
		
	def test_returnImage(self):
		imageDatabase.wipeDatabase()
		imageDatabase.addImage("test1")
		imageDatabase.addImage("test2")
		self.assertEqual(imageDatabase.returnImage("test1")['image'], "test1")

	def test_wipeDatabase(self):
		imageDatabase.addImage("test1")
		imageDatabase.addImage("test2")
		imageDatabase.addImage("test3")
		imageDatabase.wipeDatabase()
		images = imageDatabase.getImages()
		numImages = len(images)
		self.assertEqual(numImages, 0)

	
if __name__ == '__main__':
   unittest.main()
	

		