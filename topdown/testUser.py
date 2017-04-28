import unittest
import sys
import StringIO
from topDown import user

class TestUser(unittest.TestCase):	
	def testConstructor(self):
		u = user("a", "1", "2", "3", "4", "5", "6")
		self.assertEqual("a", u.username)
		
		self.assertEqual([], u.somewhatCloseFriends)
		self.assertEqual([], u.closeFriends)
		self.assertEqual(6, len(u.friends))

		self.assertEqual(0, u.age)
		self.assertEqual(0, u.male)
		self.assertEqual(0, u.other)

		self.assertEqual("", u.primarySub)
		self.assertEqual(0, u.primAlcohol)
		self.assertEqual(0, u.primCannabis)
		self.assertEqual(0, u.primCocaine)
		self.assertEqual(0, u.primOpiods)
		self.assertEqual(0, u.primPainRel)
		self.assertEqual(0, u.primStimulants)
		self.assertEqual(0, u.primTranq)
		self.assertEqual(0, u.primDiss)

		self.assertEqual("", u.secondarySub)
		self.assertEqual(0, u.secAlcohol)
		self.assertEqual(0, u.secCannabis)
		self.assertEqual(0, u.secCocaine)
		self.assertEqual(0, u.secOpiods)
		self.assertEqual(0, u.secPainRel)
		self.assertEqual(0, u.secStimulants)
		self.assertEqual(0, u.secTranq)
		self.assertEqual(0, u.secNico)
		self.assertEqual(0, u.other)

		self.assertEqual(0, u.someHighSchool)
		self.assertEqual(0, u.highSchool)
		self.assertEqual(0, u.someCollege)
		self.assertEqual(0, u.Associates)
		self.assertEqual(0, u.Bachelors)
		self.assertEqual(0, u.Masters)
		self.assertEqual(0, u.Doctoral)
		
		self.assertEqual(0, u.lessThan30)
		self.assertEqual(0, u.thirtyTo50)
		self.assertEqual(0, u.fiftyTo70)
		self.assertEqual(0, u.seventyTo90)
		self.assertEqual(0, u.ninetyTo150)
		self.assertEqual(0, u.greaterThan150)
		self.assertEqual(0, u.preferNotToAns)

		self.assertEqual(0, u.currentSmoker)
		self.assertEqual(0, u.exSmoker)

	def testSetCloseness(self):
		u = user("a", "1", "2", "3", "4", "5", "6")
		f1 = u.friends[0]
		f2 = u.friends[0]
		f3 = u.friends[0]
		f4 = u.friends[0]
		f5 = u.friends[0]
		f6 = u.friends[0]
		self.assertEqual(f1.close, "")
		self.assertEqual(f2.close, "")
		self.assertEqual(f3.close, "")
		self.assertEqual(f4.close, "")
		self.assertEqual(f5.close, "")
		self.assertEqual(f6.close, "")

		u.setCloseness("close", "close", "close", "close", "close", "close")
		self.assertEqual(f1.close, "close")
		self.assertEqual(f2.close, "close")
		self.assertEqual(f3.close, "close")
		self.assertEqual(f4.close, "close")
		self.assertEqual(f5.close, "close")
		self.assertEqual(f6.close, "close")

	def testPrintFriends(self):
		capturedOutput = StringIO.StringIO()        
		sys.stdout = capturedOutput
		u = user("a", "1", "2", "3", "4", "5", "6")
		u.printFriends()
		self.assertEqual("1\n2\n3\n4\n5\n6\n", capturedOutput.getvalue())

	def testPrintFriends(self):
		capturedOutput = StringIO.StringIO()        
		sys.stdout = capturedOutput
		u = user("a", "1", "2", "3", "4", "5", "6")
		u.setCloseness("close", "close", "close", "close", "close", "close")
		u.printCloseness()
		self.assertEqual("close\nclose\nclose\nclose\nclose\nclose\n", capturedOutput.getvalue())

	def testPrintDemographics(self):
		capturedOutput = StringIO.StringIO()        
		sys.stdout = capturedOutput
		u = user("a", "1", "2", "3", "4", "5", "6")
		u.printDemographics()
		self.assertEqual(78, len(capturedOutput.getvalue()))

	def testPrintSimilarities(self):
		capturedOutput = StringIO.StringIO()        
		sys.stdout = capturedOutput
		u = user("a", "1", "2", "3", "4", "5", "6")
		u.printSimilarities()
		self.assertEqual(300, len(capturedOutput.getvalue()))

unittest.main()