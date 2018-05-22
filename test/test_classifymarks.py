

import os

import unittest
import classify

class TestClassifyMarks(unittest.Testcase):
	
	def setUp(self):
		data =  open("data.txt")
		
	def tearDown(self):
		del data
		
	def test_getData(self):
		correctAns = [[Jim, 60], [Dhevan, 90], [Sarah, 39]]
		checkAns = classify.getData(data)
		self.assertEqual(checkAns, correctAns)
		 
	def test_thoseInRange(self):
		correctAns = ["Jim", "Sarah"]
		d = classify.getData(data)
		checkAns = classify.thoseInRange(d, 30, 90)
		self.assertEqual(checkAns, correctAns)
		
	
		
		

if __name__ == '__main__':
    unittest.main()
