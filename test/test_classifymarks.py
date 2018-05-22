

import os

import unittest 

import classify #not recognising classify as a module even though I've set up the init file in the classify directory.


class TestClassifyMarks(unittest.TestCase):
	

	def setUp(self):
		data = open("data.txt")

	def tearDown(self):
		del data

	def test_getData(self):
		correctAns = [[1335987, 60], [1433596, 90], [1235465, 39]]
		checkAns = classify.getData(data)
		self.assertEqual(checkAns, correctAns)
		 
	def test_thoseInRange(self):
		correctAns = [1335987, 1235465]
		d = classify.getData(data)
		checkAns = classify.thoseInRange(d, 30, 90)
		self.assertEqual(checkAns, correctAns)

		correctAns = ["none"]
		checkAns = classify.thoseInRange([], 30, 90)
		self.assertEqual(checkAns, correctAns)


	
	#def test_show_Ranges(self):
		#Not finished
		

if __name__ == '__main__':
    unittest.main()

