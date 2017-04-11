#Top Down approach to homophily
#Wilson Rhodes & Timothy Tran


import csv

usersLattice2 = []
usersSmall2 = []

usersLattice3 = []
usersSmall3 = []

usersLattice = []
usersSmall = []

class friend:
    def __init__(self, usrnme):
        self.username = usrnme
        self.similarAge = False
        self.sameGender = False
        self.samePrimarySub = False
        self.sameSecondarySub = False
        self.sameEducation = False
        self.sameIncome = False
        self.sameCurrentSmoker = False
        self.sameExSmoker = False
        self.closeToUser = ""

class user:
    def __init__(self, username, friend1, friend2, friend3, friend4, friend5, friend6):
        self.username = username
        self.somewhatCloseFriends = []
        self.closeFriends = []

        friendOne = friend(friend1)
        friendTwo = friend(friend2)
        friendThree = friend(friend3)
        friendFour = friend(friend4)
        friendFive = friend(friend5)
        friendSix = friend(friend6)
        self.friends = [friendOne, friendTwo, friendThree, friendFour, friendFive, friendSix]

        self.age = 0
        self.male = 0
        self.female = 0
        self.other = 0

        self.primarySub = ""
        self.primAlcohol = 0
        self.primCannabis = 0
        self.primCocaine = 0
        self.primOpiods = 0
        self.primPainRel = 0
        self.primStimulants = 0
        self.primTranq = 0
        self.primDiss = 0

        self.secondarySub = ""
        self.secAlcohol = 0
        self.secCannabis = 0
        self.secCocaine = 0
        self.secOpiods = 0
        self.secPainRel = 0
        self.secStimulants = 0
        self.secTranq = 0
        self.secNico = 0
        self.other = 0

        self.someHighSchool = 0
        self.highSchool = 0
        self.someCollege = 0
        self.Associates = 0
        self.Bachelors = 0
        self.Masters = 0
        self.Doctoral = 0

        self.lessThan30 = 0
        self.thirtyTo50 = 0
        self.fiftyTo70 = 0
        self.seventyTo90 = 0
        self.ninetyTo150 = 0
        self.greaterThan150 = 0
        self.preferNotToAns = 0

        self.currentSmoker = 0
        self.exSmoker = 0

    def setCloseness(self, howClose1, howClose2, howClose3, howClose4, howClose5, howClose6):
        self.friends[0].close = howClose1
        self.friends[1].close = howClose2
        self.friends[2].close = howClose3
        self.friends[3].close = howClose4
        self.friends[4].close = howClose5
        self.friends[5].close = howClose6

    def printFriends(self):
        for currFriend in self.friends:
            print currFriend.username

    def printCloseness(self):
        for currFriend in self.friends:
            print currFriend.close

    def printDemographics(self):
        print self.username

        print self.age
        print self.male
        print self.female
        print self.other

        print self.primarySub
        print self.primAlcohol
        print self.primCannabis
        print self.primCocaine
        print self.primOpiods
        print self.primPainRel
        print self.primStimulants
        print self.primTranq
        print self.primDiss

        print self.secondarySub
        print self.secAlcohol
        print self.secCannabis
        print self.secCocaine
        print self.secOpiods
        print self.secPainRel
        print self.secStimulants
        print self.secTranq
        print self.secNico
        print self.other

        print self.someHighSchool
        print self.highSchool
        print self.someCollege
        print self.Associates
        print self.Bachelors
        print self.Masters
        print self.Doctoral

        print self.lessThan30
        print self.thirtyTo50
        print self.fiftyTo70
        print self.seventTo90
        print self.ninetyTo150
        print self.greaterThan150
        print self.preferNotToAns

        print self.currentSmoker
        print self.exSmoker

    def printSimilarities(self):
        for currFriend in self.friends:
            print currFriend.username
            print currFriend.similarAge
            print currFriend.sameGender
            print currFriend.samePrimarySub
            print currFriend.sameSecondarySub
            print currFriend.sameEducation
            print currFriend.sameIncome
            print currFriend.sameCurrentSmoker
            print currFriend.sameExSmoker


def setFriends(timepoint):
    if timepoint == 2:
        with open('Timepoint2AllData.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                currentUser = user(row["username"], row["Recovery Buddy [1]"], row["Recovery Buddy [2]"], row["Recovery Buddy [3]"], row["Recovery Buddy [4]"], row["Recovery Buddy [5]"], row["Recovery Buddy [6]"])
                parsedUsername = row["username"]
                parsedUsername = parsedUsername[1:]
                currentUser.setCloseness(row["How close to you feel to Buddy 1"], row["How close to you feel to Buddy 2"], row["How close to you feel to Buddy 3"], row["How close to you feel to Buddy 4"], row["How close to you feel to Buddy 5"], row["How close to you feel to Buddy 6"])
                if int(parsedUsername) <= 4128:
                    usersLattice2.append(currentUser)
                else:
                    usersSmall2.append(currentUser)

    if timepoint == 3:
        with open('Timepoint3AllData.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                currentUser = user(row["username"], "u"+row["Recovery Buddy [1]"], "u"+row["Recovery Buddy [2]"], "u"+row["Recovery Buddy [3]"], "u"+row["Recovery Buddy [4]"], "u"+row["Recovery Buddy [5]"], "u"+row["Recovery Buddy [6]"])
                parsedUsername = row["username"]
                parsedUsername = parsedUsername[1:]
                currentUser.setCloseness(row["How close to you feel to Buddy 1"], row["How close to you feel to Buddy 2"], row["How close to you feel to Buddy 3"], row["How close to you feel to Buddy 4"], row["How close to you feel to Buddy 5"], row["How close to you feel to Buddy 6"])
                if int(parsedUsername) <= 4128:
                    usersLattice.append(currentUser)
                else:
                    usersSmall.append(currentUser)

def setDemographics():
    with open('DemoLattice.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:

            foundUser = False
            for checkUser in usersLattice:
                if row["ID"] == checkUser.username:
                    currentUser = checkUser
                    foundUser = True
                    break

            if not foundUser:
                continue

            currentUser.age = int(row["Age"])
            currentUser.male = int(row["Male"])
            currentUser.female = int(row["Female"])
            currentUser.other = int(row["Other"])

            currentUser.primarySub = row["Primary Sub. Add."]
            currentUser.primAlcohol = int(row["Alcohol"])
            currentUser.primCannabis = int(row["Cannabis"])
            currentUser.primCocaine = int(row["Cocaine"])
            currentUser.primOpiods = int(row["Opiods"])
            currentUser.primPainRel = int(row["Presc. Pain Relivers"])
            currentUser.primStimulants = int(row["Stimulants"])
            currentUser.primTranq = int(row["Traq/Depres."])
            currentUser.primDiss = int(row["Dissociatives"])

            currentUser.secondarySub = row["Secondary Sub. Add."]
            currentUser.secAlcohol = int(row["SAlcohol"])
            currentUser.secCannabis = int(row["SCannabis"])
            currentUser.secCocaine = int(row["SCocaine"])
            currentUser.secOpiods = int(row["SOpiods"])
            currentUser.secPainRel = int(row["SPresc. Pain Relivers"])
            currentUser.secStimulants = int(row["SStimulants"])
            currentUser.secTranq = int(row["STraq/Depres."])
            currentUser.secNico = int(row["SNicotine"])
            currentUser.other = int(row["Other (non-subs)"])

            currentUser.someHighSchool = int(row["Some High School"])
            currentUser.highSchool = int(row["High school diploma or equivalency"])
            currentUser.someCollege = int(row["Some College"])
            currentUser.Associates = int(row["Associates Deg."])
            currentUser.Bachelors = int(row["Bach. Deg."])
            currentUser.Masters = int(row["Mast. Deg."])
            currentUser.Doctoral = int(row["Doc. Deg."])

            currentUser.lessThan30 = int(row["Less than $30,000"])
            currentUser.thirtyTo50 = int(row["$30,000 - $49,999"])
            currentUser.fiftyTo70 = int(row["$50,000 - $69,999"])
            currentUser.seventTo90 = int(row["$70,000 - $89,999"])
            currentUser.ninetyTo150 = int(row["$90,000 - $149,999"])
            currentUser.greaterThan150 = int(row["$150,000 and above"])
            currentUser.preferNotToAns = int(row["Prefer Not to Answer"])

            currentUser.currentSmoker = int(row["Current Smoker"])
            currentUser.exSmoker = int(row["Ex-Smoker"])

    with open('DemoSmall.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:

            foundUser = False
            for checkUser in usersSmall:
                if row["ID"] == checkUser.username:
                    currentUser = checkUser
                    foundUser = True
                    break

            if not foundUser:
                continue

            currentUser.age = int(row["Age"])
            currentUser.male = int(row["Male"])
            currentUser.female = int(row["Female"])
            currentUser.other = int(row["Other"])

            currentUser.primarySub = row["Primary Sub. Add."]
            currentUser.primAlcohol = int(row["Alcohol"])
            currentUser.primCannabis = int(row["Cannabis"])
            currentUser.primCocaine = int(row["Cocaine"])
            currentUser.primOpiods = int(row["Opiods"])
            currentUser.primPainRel = int(row["Presc. Pain Relivers"])
            currentUser.primStimulants = int(row["Stimulants"])

            currentUser.secondarySub = row["Secondary Sub. Add."]
            currentUser.secAlcohol = int(row["SAlcohol"])
            currentUser.secCannabis = int(row["SCannabis"])
            currentUser.secCocaine = int(row["SCocaine"])
            currentUser.secOpiods = int(row["SOpiods"])
            currentUser.secPainRel = int(row["SPresc. Pain Relivers"])
            currentUser.secStimulants = int(row["SStimulants"])
            currentUser.secTranq = int(row["STraq/Depres."])
            currentUser.secNico = int(row["SNicotine"])
            currentUser.other = int(row["Other (non-subs)"])

            currentUser.someHighSchool = int(row["Some High School"])
            currentUser.highSchool = int(row["High school diploma or equivalency"])
            currentUser.someCollege = int(row["Some College"])
            currentUser.Associates = int(row["Associates Deg."])
            currentUser.Bachelors = int(row["Bach. Deg."])
            currentUser.Masters = int(row["Mast. Deg."])
            currentUser.Doctoral = int(row["Doc. Deg."])

            currentUser.lessThan30 = int(row["Less than $30,000"])
            currentUser.thirtyTo50 = int(row["$30,000 - $49,999"])
            currentUser.fiftyTo70 = int(row["$50,000 - $69,999"])
            currentUser.seventTo90 = int(row["$70,000 - $89,999"])
            currentUser.ninetyTo150 = int(row["$90,000 - $149,999"])
            currentUser.greaterThan150 = int(row["$150,000 and above"])
            currentUser.preferNotToAns = int(row["Prefer Not to Answer"])

            currentUser.currentSmoker = int(row["Current Smoker"])
            currentUser.exSmoker = int(row["Ex-Smoker"])

#this method needs work to work with both timepoints, will throw errors on timepoint 3 data b/c of formatting differences
def setSimilarities(timepoint):
    #for each user
    for currUser in usersLattice:
        friendCount = 0
        for eachFriend in currUser.friends:
            if eachFriend.username != "null" and eachFriend.username != "unull":
                compareName = eachFriend.username
                compareUser = currUser
                for findFriend in usersLattice:
                    if findFriend.username == compareName:
                        compareUser = findFriend
                        break
                compareTwoUsers(currUser, compareUser, 1)
            friendCount += 1

    for currUser in usersSmall:
        friendCount = 0
        for eachFriend in currUser.friends:
            if eachFriend.username != "null" and eachFriend.username != "unull":
                compareName = eachFriend.username
                compareUser = currUser
                for findFriend in usersSmall:
                    if findFriend.username == compareName:
                        compareUser = findFriend
                        break
                compareTwoUsers(currUser, compareUser, friendCount)
            friendCount += 1

def compareTwoUsers(user1, user2, friendNumber):
    #check if ages are +- 4
    ageDifference = int(user1.age) - int(user2.age)
    if ageDifference >= -4 and ageDifference <= 4:
        user1.friends[friendNumber].similarAge = True

    if user1.male == 1 and user2.male == 1 or user1.female == 1 and user2.female == 1:
        user1.friends[friendNumber].sameGender = True

    #check primary substance
    if user1.primAlcohol == 1 and user2.primAlcohol == 1 or user1.primCannabis == 1 and user2.primCannabis == 1 or user1.primCocaine == 1 and user2.primCocaine == 1 or user1.primOpiods == 1 and user2.primOpiods == 1 or user1.primPainRel == 1 and user2.primPainRel == 1 or user1.primStimulants == 1 and user2.primStimulants == 1:
        user1.friends[friendNumber].samePrimarySub = True

    #check secondary substance
    if user1.secAlcohol == 1 and user2.secAlcohol == 1 or user1.secCannabis == 1 and user2.secCannabis == 1 or user1.secCocaine == 1 and user2.secCocaine == 1 or user1.secOpiods == 1 and user2.secOpiods == 1 or user1.secPainRel == 1 and user2.secPainRel == 1 or user1.secStimulants == 1 and user2.secStimulants == 1 or user1.secNico == 1 and user2.secNico == 1:
        user1.friends[friendNumber].sameSecondarySub = True

    #check education
    if user1.someHighSchool == 1 and user2.someHighSchool == 1 or user1.highSchool == 1 and user2.highSchool == 1 or user1.Associates == 1 and user2.Associates == 1 or user1.Bachelors == 1 and user2.Bachelors == 1 or user1.Associates == 1 and user2.Associates == 1 or user1.Masters == 1 and user2.Masters == 1 or user1.Doctoral == 1 and user2.Doctoral== 1:
        user1.friends[friendNumber].sameEducation = True

    #check income
    if user1.lessThan30 == 1 and user2.lessThan30 == 1 or user1.thirtyTo50 == 1 and user2.thirtyTo50 == 1 or user1.fiftyTo70 == 1 and user2.fiftyTo70 == 1 or user1.seventyTo90 == 1 and user2.seventyTo90 == 1 or user1.ninetyTo150 == 1 and user2.ninetyTo150 == 1 or user1.greaterThan150 == 1 and user2.greaterThan150 == 1:
        user1.friends[friendNumber].sameIncome = True

    #check current smoker
    if user1.currentSmoker == 1 and user2.currentSmoker == 1:
        user1.friends[friendNumber].sameCurrentSmoker = True

    #check ex smoker
    if user1.exSmoker == 1 and user2.exSmoker == 1:
        user1.friends[friendNumber].sameExSmoker = True

def tallyCloseness():
    lattNotClose = 0
    lattSomewhat = 0
    lattClose = 0
    for lattUser in usersLattice:
        for currFriend in lattUser.friends:
            if currFriend.username != "null" and currFriend.username != "unull":
                if currFriend.close == "not close":
                    lattNotClose += 1
                elif currFriend.close == "somewhat close":
                    lattUser.somewhatCloseFriends.append(currFriend)
                    lattSomewhat += 1
                elif currFriend.close == "very close":
                    lattUser.closeFriends.append(currFriend)
                    lattClose += 1

    smallNotClose = 0
    smallSomewhat = 0
    smallClose = 0
    for smallUser in usersSmall:
        for currFriend in smallUser.friends:
            if currFriend.username != "null" and currFriend.username != "unull":
                if currFriend.close == "not close":
                    smallNotClose += 1
                elif currFriend.close == "somewhat close":
                    smallUser.somewhatCloseFriends.append(currFriend)
                    smallSomewhat += 1
                elif currFriend.close == "very close":
                    smallUser.closeFriends.append(currFriend)
                    smallClose += 1

    print "Among all of the data from Timepoint 2 we found:\n"
    print "Number of Not Close Users in the Lattice Network:",
    print lattNotClose
    print "Number of Somewhat Close Users in the Lattice Network:",
    print lattSomewhat
    print "Number of Very Close Users in the Lattice Network:",
    print lattClose
    print "\n"
    print "Number of Not Close Users in the Small World Network:",
    print smallNotClose
    print "Number of Somewhat Close Users in the Small World Network:",
    print smallSomewhat
    print "Number of Very Close Users in the Small World Network:",
    print smallClose

#combines the two users into the user1 object
#used to combine the timepoint data
#ideally this method is called on two users with the same name
def combineTwoUsers(user1, user2):
    print "topKek"

#main
#setFriends(2)
#setDemographics()
#setSimilarities(2)
#tallyCloseness()

setFriends(3)
setDemographics()
setSimilarities(3)
tallyCloseness()

#print somewhat close and very close friend pairs
for lattUser in usersLattice:
    if len(lattUser.somewhatCloseFriends) > 0 or len(lattUser.closeFriends) > 0:
        print "User: " + lattUser.username
        print "Somewhat close friends: ",
        for currFriend in lattUser.somewhatCloseFriends:
            print currFriend.username
        print "Close Friends: ",
        for currFriend in lattUser.closeFriends:
            print currFriend.username
        print "\n\n"

for smallUser in usersSmall:
    if len(smallUser.somewhatCloseFriends) > 0 or len(smallUser.closeFriends) > 0:
        print "User: " + smallUser.username
        print "Somewhat close friends: ",
        for currFriend in smallUser.somewhatCloseFriends:
            print currFriend.username
        print "Close Friends: ",
        for currFriend in smallUser.closeFriends:
            print currFriend.username
        print "\n\n"
#print usersLattice[0].username
#print usersLattice[0].female
#print usersLattice[52].username
#print usersLattice[52].female
#for user in usersLattice:
#    user.printFriends()
