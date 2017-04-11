#Top Down approach to homophily
#Wilson Rhodes & Timothy Tran

#todo, check small world similarity data

import csv

allUsersDemographics = []

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

class skeletonUser:
    def __init__(self, username):
        self.username = username

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
                    usersLattice3.append(currentUser)
                else:
                    usersSmall3.append(currentUser)

def setDemographics():
    with open('DemoLattice.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:

            #add to full demo table for comparisons
            demoUser = skeletonUser(row["ID"])

            demoUser.age = int(row["Age"])
            demoUser.male = int(row["Male"])
            demoUser.female = int(row["Female"])
            demoUser.other = int(row["Other"])

            demoUser.primarySub = row["Primary Sub. Add."]
            demoUser.primAlcohol = int(row["Alcohol"])
            demoUser.primCannabis = int(row["Cannabis"])
            demoUser.primCocaine = int(row["Cocaine"])
            demoUser.primOpiods = int(row["Opiods"])
            demoUser.primPainRel = int(row["Presc. Pain Relivers"])
            demoUser.primStimulants = int(row["Stimulants"])
            demoUser.primTranq = int(row["Traq/Depres."])
            demoUser.primDiss = int(row["Dissociatives"])

            demoUser.secondarySub = row["Secondary Sub. Add."]
            demoUser.secAlcohol = int(row["SAlcohol"])
            demoUser.secCannabis = int(row["SCannabis"])
            demoUser.secCocaine = int(row["SCocaine"])
            demoUser.secOpiods = int(row["SOpiods"])
            demoUser.secPainRel = int(row["SPresc. Pain Relivers"])
            demoUser.secStimulants = int(row["SStimulants"])
            demoUser.secTranq = int(row["STraq/Depres."])
            demoUser.secNico = int(row["SNicotine"])
            demoUser.other = int(row["Other (non-subs)"])

            demoUser.someHighSchool = int(row["Some High School"])
            demoUser.highSchool = int(row["High school diploma or equivalency"])
            demoUser.someCollege = int(row["Some College"])
            demoUser.Associates = int(row["Associates Deg."])
            demoUser.Bachelors = int(row["Bach. Deg."])
            demoUser.Masters = int(row["Mast. Deg."])
            demoUser.Doctoral = int(row["Doc. Deg."])

            demoUser.lessThan30 = int(row["Less than $30,000"])
            demoUser.thirtyTo50 = int(row["$30,000 - $49,999"])
            demoUser.fiftyTo70 = int(row["$50,000 - $69,999"])
            demoUser.seventTo90 = int(row["$70,000 - $89,999"])
            demoUser.ninetyTo150 = int(row["$90,000 - $149,999"])
            demoUser.greaterThan150 = int(row["$150,000 and above"])
            demoUser.preferNotToAns = int(row["Prefer Not to Answer"])

            demoUser.currentSmoker = int(row["Current Smoker"])
            demoUser.exSmoker = int(row["Ex-Smoker"])

            allUsersDemographics.append(demoUser)

            #add to table that contains usable data
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
            #add to full demo table for comparisons
            demoUser = skeletonUser(row["ID"])

            demoUser.age = int(row["Age"])
            demoUser.male = int(row["Male"])
            demoUser.female = int(row["Female"])
            demoUser.other = int(row["Other"])

            demoUser.primarySub = row["Primary Sub. Add."]
            demoUser.primAlcohol = int(row["Alcohol"])
            demoUser.primCannabis = int(row["Cannabis"])
            demoUser.primCocaine = int(row["Cocaine"])
            demoUser.primOpiods = int(row["Opiods"])
            demoUser.primPainRel = int(row["Presc. Pain Relivers"])
            demoUser.primStimulants = int(row["Stimulants"])

            demoUser.secondarySub = row["Secondary Sub. Add."]
            demoUser.secAlcohol = int(row["SAlcohol"])
            demoUser.secCannabis = int(row["SCannabis"])
            demoUser.secCocaine = int(row["SCocaine"])
            demoUser.secOpiods = int(row["SOpiods"])
            demoUser.secPainRel = int(row["SPresc. Pain Relivers"])
            demoUser.secStimulants = int(row["SStimulants"])
            demoUser.secTranq = int(row["STraq/Depres."])
            demoUser.secNico = int(row["SNicotine"])
            demoUser.other = int(row["Other (non-subs)"])

            demoUser.someHighSchool = int(row["Some High School"])
            demoUser.highSchool = int(row["High school diploma or equivalency"])
            demoUser.someCollege = int(row["Some College"])
            demoUser.Associates = int(row["Associates Deg."])
            demoUser.Bachelors = int(row["Bach. Deg."])
            demoUser.Masters = int(row["Mast. Deg."])
            demoUser.Doctoral = int(row["Doc. Deg."])

            demoUser.lessThan30 = int(row["Less than $30,000"])
            demoUser.thirtyTo50 = int(row["$30,000 - $49,999"])
            demoUser.fiftyTo70 = int(row["$50,000 - $69,999"])
            demoUser.seventTo90 = int(row["$70,000 - $89,999"])
            demoUser.ninetyTo150 = int(row["$90,000 - $149,999"])
            demoUser.greaterThan150 = int(row["$150,000 and above"])
            demoUser.preferNotToAns = int(row["Prefer Not to Answer"])

            demoUser.currentSmoker = int(row["Current Smoker"])
            demoUser.exSmoker = int(row["Ex-Smoker"])

            allUsersDemographics.append(demoUser)

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


def setSimilarities():
    #for each user
    for currUser in usersLattice:
        friendCount = 0
        for eachFriend in currUser.friends:
            if eachFriend.username != "null" and eachFriend.username != "unull":
                compareName = eachFriend.username
                compareUser = currUser
                for findFriend in allUsersDemographics:
                    if findFriend.username == compareName:
                        compareUser = findFriend
                        break
                #check this line
                if compareUser != currUser:
                    compareTwoUsers(currUser, compareUser, friendCount)
            friendCount += 1

    for currUser in usersSmall:
        friendCount = 0
        for eachFriend in currUser.friends:
            if eachFriend.username != "null" and eachFriend.username != "unull":
                compareName = eachFriend.username
                compareUser = currUser
                for findFriend in allUsersDemographics:
                    if findFriend.username == compareName:
                        compareUser = findFriend
                        break
                if compareUser != currUser:
                    compareTwoUsers(currUser, compareUser, friendCount)
            friendCount += 1

def compareTwoUsers(user1, user2, friendNumber):
    #check if ages are +- 4
    ageDifference = int(user1.age) - int(user2.age)
    if ageDifference >= -4 and ageDifference <= 4:
        user1.friends[friendNumber].similarAge = True

    if (user1.male == 1 and user2.male == 1) or (user1.female == 1 and user2.female == 1):
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

    print "Among all of the data from both Timepoints we found:\n"
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
    print "\n"
    print "Number of Not Close Users in both networks:",
    print smallNotClose + lattNotClose
    print "Number of Somewhat Close Users in both networks:",
    print smallSomewhat + lattSomewhat
    print "Number of Very Close Users in both networks:",
    print smallClose + lattClose
    print "\n\n"

#combines the two users into the user1 object
#used to combine the timepoint data
#ideally this method is called on two users with the same name
def combineLists(list1, list2):
    for list2User in list2:
        foundMatchUser = False
        for list1User in list1:
            if list1User.username == list2User.username:
                foundMatchUser = True
                for list2Friends in list2User.friends:
                    foundMatchFriend = False
                    if list2Friends.username == "null" or list2Friends.username == "unull":
                        continue
                    for list1Friends in list1User.friends:
                        if list1Friends.username == "null" or list1Friends.username == "unull":
                            continue
                        elif list1Friends.username == list2Friends.username:
                            #if they were close in t3 but not t2 change the closeness to what it is in t3
                            if list1Friends.close == "not close" and list2Friends.close != "not close":
                                list1Friends.close = list2Friends.close
                            foundMatchFriend = True
                    if not foundMatchFriend:
                        list1User.friends.append(list2Friends)
        if not foundMatchUser:
            list1.append(list2User)
    return list1

#print somewhat close and very close friend pairs
def printAllFriends():
    for lattUser in usersLattice:
        if len(lattUser.somewhatCloseFriends) > 0 or len(lattUser.closeFriends) > 0:
            print "User: " + lattUser.username
            print "Somewhat close friends: ",
            for currFriend in lattUser.somewhatCloseFriends:
                print currFriend.username,
            print ""
            print "Close Friends: ",
            for currFriend in lattUser.closeFriends:
                print currFriend.username
            print "\n\n"

    for smallUser in usersSmall:
        if len(smallUser.somewhatCloseFriends) > 0 or len(smallUser.closeFriends) > 0:
            print "User: " + smallUser.username
            print "Somewhat close friends: ",
            for currFriend in smallUser.somewhatCloseFriends:
                print currFriend.username,
            print ""
            print "Close Friends: ",
            for currFriend in smallUser.closeFriends:
                print currFriend.username
            print "\n\n"

#simple bubble sort
def orderList(list):
    for i in range(len(list)):
        for j in range(len(list)-1-i):
            parsedUsername1 = list[j].username[1:]
            parsedUsername2 = list[j+1].username[1:]
            if int(parsedUsername1) > int(parsedUsername2):
                list[j], list[j+1] = list[j+1], list[j]

def createStatistics():
    numSimilarAge = 0
    numSameGender = 0
    numSamePrimary = 0
    numSameSecondary = 0
    numSameEducation = 0
    numSameIncome = 0
    numSameCurrentSmoker = 0
    numSameExSmoker = 0

    for lattUser in usersLattice:
        for eachFriend in lattUser.somewhatCloseFriends:
            if eachFriend.similarAge == True:
                numSimilarAge += 1
            if eachFriend.sameGender == True:
                numSameGender += 1
            if eachFriend.samePrimarySub == True:
                numSamePrimary += 1
            if eachFriend.sameSecondarySub == True:
                numSameSecondary += 1
            if eachFriend.sameEducation == True:
                numSameEducation += 1
            if eachFriend.sameIncome == True:
                numSameIncome += 1
            if eachFriend.sameCurrentSmoker == True:
                numSameCurrentSmoker += 1
            if eachFriend.sameExSmoker == True:
                numSameExSmoker += 1

        for eachFriend in lattUser.closeFriends:
            if eachFriend.similarAge == True:
                numSimilarAge += 1
            if eachFriend.sameGender == True:
                numSameGender += 1
            if eachFriend.samePrimarySub == True:
                numSamePrimary += 1
            if eachFriend.sameSecondarySub == True:
                numSameSecondary += 1
            if eachFriend.sameEducation == True:
                numSameEducation += 1
            if eachFriend.sameIncome == True:
                numSameIncome += 1
            if eachFriend.sameCurrentSmoker == True:
                numSameCurrentSmoker += 1
            if eachFriend.sameExSmoker == True:
                numSameExSmoker += 1

    print "Lattice Network Statistics, 44 total relationships"
    print "-------------------------------------------------"
    print "Number with a similar age:",
    print numSimilarAge
    print "Number with the same gender:",
    print numSameGender
    print "Number with the same primary addiction:",
    print numSamePrimary
    print "Number with the same secondary addiction:",
    print numSameSecondary
    print "Number with the same education level:",
    print numSameEducation
    print "Number with the same income level:",
    print numSameIncome
    print "Number that were both current smokers:",
    print numSameCurrentSmoker
    print "Number that were both ex smokers:",
    print numSameExSmoker
    print "\n"

    numSimilarAge2 = 0
    numSameGender2 = 0
    numSamePrimary2 = 0
    numSameSecondary2 = 0
    numSameEducation2 = 0
    numSameIncome2 = 0
    numSameCurrentSmoker2 = 0
    numSameExSmoker2 = 0

    for smallUser in usersSmall:
        for eachFriend in smallUser.somewhatCloseFriends:
            if eachFriend.similarAge == True:
                numSimilarAge2 += 1
            if eachFriend.sameGender == True:
                numSameGender2 += 1
            if eachFriend.samePrimarySub == True:
                numSamePrimary2 += 1
            if eachFriend.sameSecondarySub == True:
                numSameSecondary2 += 1
            if eachFriend.sameEducation == True:
                numSameEducation2 += 1
            if eachFriend.sameIncome == True:
                numSameIncome2 += 1
            if eachFriend.sameCurrentSmoker == True:
                numSameCurrentSmoker2 += 1
            if eachFriend.sameExSmoker == True:
                numSameExSmoker2 += 1

        for eachFriend in smallUser.closeFriends:
            if eachFriend.similarAge == True:
                numSimilarAge2 += 1
            if eachFriend.sameGender == True:
                numSameGender2 += 1
            if eachFriend.samePrimarySub == True:
                numSamePrimary2 += 1
            if eachFriend.sameSecondarySub == True:
                numSameSecondary2 += 1
            if eachFriend.sameEducation == True:
                numSameEducation2 += 1
            if eachFriend.sameIncome == True:
                numSameIncome2 += 1
            if eachFriend.sameCurrentSmoker == True:
                numSameCurrentSmoker2 += 1
            if eachFriend.sameExSmoker == True:
                numSameExSmoker2 += 1

    print "Small World Network Statistics, 33 total relationships"
    print "-------------------------------------------------"
    print "Number with a similar age:",
    print numSimilarAge2
    print "Number with the same gender:",
    print numSameGender2
    print "Number with the same primary addiction:",
    print numSamePrimary2
    print "Number with the same secondary addiction:",
    print numSameSecondary2
    print "Number with the same education level:",
    print numSameEducation2
    print "Number with the same income level:",
    print numSameIncome2
    print "Number that were both current smokers:",
    print numSameCurrentSmoker2
    print "Number that were both ex smokers:",
    print numSameExSmoker2
    print "\n"

    print "Combined Statistics, 77 total relationships"
    print "-------------------------------------------------"
    print "Number with a similar age:",
    print numSimilarAge + numSimilarAge2
    print "Number with the same gender:",
    print numSameGender + numSameGender2
    print "Number with the same primary addiction:",
    print numSamePrimary + numSamePrimary2
    print "Number with the same secondary addiction:",
    print numSameSecondary + numSameSecondary2
    print "Number with the same education level:",
    print numSameEducation + numSameEducation2
    print "Number with the same income level:",
    print numSameIncome + numSameIncome2
    print "Number that were both current smokers:",
    print numSameCurrentSmoker + numSameCurrentSmoker2
    print "Number that were both ex smokers:",
    print numSameExSmoker + numSameExSmoker2

#main
setFriends(2)
setFriends(3)
usersLattice = combineLists(usersLattice2, usersLattice3)
usersSmall = combineLists(usersSmall2, usersSmall3)
setDemographics()
setSimilarities()
tallyCloseness()

orderList(usersLattice)
orderList(usersSmall)
orderList(allUsersDemographics)
#printAllFriends()

createStatistics()
