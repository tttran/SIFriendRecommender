import unittest
from topDown import friend

class TestFriend(unittest.TestCase):
	def testConstructor(self):
		fN = friend("")
		self.assertEqual("null", fN.username)
		
		fA = friend("a")
		self.assertEqual("a", fA.username)
		self.assertFalse(fA.similarAge)
		self.assertFalse(fA.sameGender)
		self.assertFalse(fA.samePrimarySub)
		self.assertFalse(fA.sameSecondarySub)
		self.assertFalse(fA.sameEducation)
		self.assertFalse(fA.sameIncome)
		self.assertFalse(fA.sameCurrentSmoker)
		self.assertFalse(fA.sameExSmoker)
		self.assertEqual("", fA.close)

unittest.main()