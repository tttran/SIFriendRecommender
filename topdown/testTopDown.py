import unittest
import topDown
from topDown import user

class TestTopDown(unittest.TestCase):
	def testSetFriends(self):
		topDown.setFriends(3)
		self.assertNotEqual(0, len(topDown.usersLattice))
		self.assertNotEqual(0, len(topDown.usersSmall))

	def testSetDemographics(self):
		topDown.setDemographics("DemoLattice.csv", "lattice")
		uL = topDown.usersLattice[0]
		self.assertNotEqual(0, uL.age)

		topDown.setDemographics("DemoSmall.csv", "smallWorld")
		uS = topDown.usersSmall[0]
		self.assertNotEqual(0, uS.age)
	
	def testCompareTwoUsers(self):
		uA = user("a", "1", "2", "3", "4", "5", "6")
		uB = user("b", "1", "2", "3", "4", "5", "6")
		uC = user("c", "1", "2", "3", "4", "5", "6")
		
		uA.age = 19
		uB.age = 20
		uC.age = 10
		topDown.compareTwoUsers(uA, uB, 0)
		self.assertTrue(uA.friends[0].similarAge)
		topDown.compareTwoUsers(uA, uC, 1)
		self.assertFalse(uA.friends[1].similarAge)

		uA.male = 1
		uB.male = 1
		uC.male = 0
		topDown.compareTwoUsers(uA, uB, 0)
		self.assertTrue(uA.friends[0].sameGender)
		topDown.compareTwoUsers(uA, uC, 1)
		self.assertFalse(uA.friends[1].sameGender)

		uA.primAlcohol = 1
		uB.primAlcohol = 1
		uC.primAlcohol = 0
		topDown.compareTwoUsers(uA, uB, 0)
		self.assertTrue(uA.friends[0].samePrimarySub)
		topDown.compareTwoUsers(uA, uC, 1)
		self.assertFalse(uA.friends[1].samePrimarySub)

		uA.primAlcohol = 1
		uB.primAlcohol = 1
		uC.primAlcohol = 0
		topDown.compareTwoUsers(uA, uB, 0)
		self.assertTrue(uA.friends[0].samePrimarySub)
		topDown.compareTwoUsers(uA, uC, 1)
		self.assertFalse(uA.friends[1].samePrimarySub)

		uA.secAlcohol = 1
		uB.secAlcohol = 1
		uC.secAlcohol = 0
		topDown.compareTwoUsers(uA, uB, 0)
		self.assertTrue(uA.friends[0].sameSecondarySub)
		topDown.compareTwoUsers(uA, uC, 1)
		self.assertFalse(uA.friends[1].sameSecondarySub)

		uA.someHighSchool = 1
		uB.someHighSchool = 1
		uC.someHighSchool = 0
		topDown.compareTwoUsers(uA, uB, 0)
		self.assertTrue(uA.friends[0].sameEducation)
		topDown.compareTwoUsers(uA, uC, 1)
		self.assertFalse(uA.friends[1].sameEducation)

		uA.lessThan30 = 1
		uB.lessThan30 = 1
		uC.lessThan30 = 0
		topDown.compareTwoUsers(uA, uB, 0)
		self.assertTrue(uA.friends[0].sameIncome)
		topDown.compareTwoUsers(uA, uC, 1)
		self.assertFalse(uA.friends[1].sameIncome)

		uA.currentSmoker = 1
		uB.currentSmoker = 1
		uC.currentSmoker = 0
		topDown.compareTwoUsers(uA, uB, 0)
		self.assertTrue(uA.friends[0].sameCurrentSmoker)
		topDown.compareTwoUsers(uA, uC, 1)
		self.assertFalse(uA.friends[1].sameCurrentSmoker)

		uA.exSmoker = 1
		uB.exSmoker = 1
		uC.exSmoker = 0
		topDown.compareTwoUsers(uA, uB, 0)
		self.assertTrue(uA.friends[0].sameExSmoker)
		topDown.compareTwoUsers(uA, uC, 1)
		self.assertFalse(uA.friends[1].sameExSmoker)

	def testOrderList(self):
		topDown.orderList(topDown.usersLattice)
		u1 = topDown.usersLattice[0]
		u2 = topDown.usersLattice[len(topDown.usersLattice) - 1]
		self.assertTrue(int(u1.username[1:]) < int(u2.username[1:]))

		topDown.orderList(topDown.usersSmall)
		u1 = topDown.usersSmall[0]
		u2 = topDown.usersSmall[len(topDown.usersSmall) - 1]
		self.assertTrue(int(u1.username[1:]) < int(u2.username[1:]))

	def testClearFile(self):
		topDown.clearFile("Timepoint3Statistics.txt")
		topDown.sumRemovedEntries("Timepoint3Statistics.txt")
		self.assertFalse(open("Timepoint3Statistics.txt", "r").read().find("We had to remove"))

	# INTEGRATION TEST
	def testTallyCloseness(self):
		topDown.clearFile("Timepoint3Statistics.txt")
		topDown.setFriends(3)
		topDown.setDemographics("DemoLattice.csv", "lattice")
		topDown.setDemographics("DemoSmall.csv", "smallWorld")
		topDown.setSimilarities()
		topDown.tallyCloseness('Timepoint3Statistics.txt')
		file = open("Timepoint3Statistics.txt", "r")
		self.assertTrue(file.read().find("Number of Not Close Users in the Lattice Network: "))
		self.assertTrue(file.read().find("Number of Somewhat Close Users in the Lattice Network: "))
		self.assertTrue(file.read().find("Number of Very Close Users in the Lattice Network: "))
		self.assertTrue(file.read().find("Number of Not Close Users in the Small World Network: "))
		self.assertTrue(file.read().find("Number of Somewhat Close Users in the Small World Network: "))
		self.assertTrue(file.read().find("Number of Very Close Users in the Small World Network: "))
		self.assertTrue(file.read().find("Number of Not Close Users in both networks: "))
		self.assertTrue(file.read().find("Number of Somewhat Close Users in both networks: "))
		self.assertTrue(file.read().find("Number of Very Close Users in both networks: "))

	# INTEGRATION TEST
	def testCreateStatistics(self):
		topDown.clearFile("Timepoint3Statistics.txt")
		topDown.setFriends(3)
		topDown.setDemographics("DemoLattice.csv", "lattice")
		topDown.setDemographics("DemoSmall.csv", "smallWorld")
		topDown.setSimilarities()
		topDown.tallyCloseness('Timepoint3Statistics.txt')
		topDown.orderList(topDown.usersLattice)
		topDown.orderList(topDown.usersSmall)
		topDown.createStatistics('Timepoint3Statistics.txt')
		file = open("Timepoint3Statistics.txt", "r")
		self.assertTrue(file.read().find("Lattice Network Statistics, 23 total relationships\n"))
		self.assertTrue(file.read().find("-------------------------------------------------\n"))
		self.assertTrue(file.read().find("Lattice Network Statistics, 23 total relationships\n"))
		self.assertTrue(file.read().find("Number with a similar age: "))
		self.assertTrue(file.read().find("Number with the same gender: "))
		self.assertTrue(file.read().find("Number with the same primary addiction: "))
		self.assertTrue(file.read().find("Number with the same secondary addiction: "))
		self.assertTrue(file.read().find("Number with the same education level: "))
		self.assertTrue(file.read().find("Number with the same income level: "))
		self.assertTrue(file.read().find("Number that were both current smokers: "))
		self.assertTrue(file.read().find("Number that were both ex smokers: "))
		self.assertTrue(file.read().find("mall World Network Statistics, 32 total relationships\n"))


	# INTEGRATION TEST
	def testSumRemovedEntries(self):
		topDown.clearFile("Timepoint3Statistics.txt")
		topDown.setFriends(3)
		topDown.setDemographics("DemoLattice.csv", "lattice")
		topDown.setDemographics("DemoSmall.csv", "smallWorld")
		topDown.setSimilarities()
		topDown.tallyCloseness('Timepoint3Statistics.txt')
		topDown.orderList(topDown.usersLattice)
		topDown.orderList(topDown.usersSmall)
		topDown.createStatistics('Timepoint3Statistics.txt')
		topDown.sumRemovedEntries("Timepoint3Statistics.txt")
		self.assertTrue(open("Timepoint3Statistics.txt", "r").read().find("We had to remove "))

	# INTEGRATION TEST
	def testPrintTwoWayFriendships(self):
		topDown.clearFile("Timepoint3Statistics.txt")
		topDown.setFriends(3)
		topDown.setDemographics("DemoLattice.csv", "lattice")
		topDown.setDemographics("DemoSmall.csv", "smallWorld")
		topDown.setSimilarities()
		topDown.tallyCloseness('Timepoint3Statistics.txt')
		topDown.orderList(topDown.usersLattice)
		topDown.orderList(topDown.usersSmall)
		topDown.createStatistics('Timepoint3Statistics.txt')
		topDown.sumRemovedEntries("Timepoint3Statistics.txt")
		topDown.printTwoWayFriendships('Timepoint3Statistics.txt')
		file = open("Timepoint3Statistics.txt", "r")
		self.assertTrue(file.read().find("The number of one-way friendships we found is "))
		self.assertTrue(file.read().find("The number of two-way friendships we found is "))

unittest.main()