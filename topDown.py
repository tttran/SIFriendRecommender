#Top Down approach to homophily
#Wilson Rhodes

#in the demoLattice table, everyone is listed as has a secondary substance addiction
#but not everyone has a secondary substance listed, bad data
#ex u4014

#sorry Matt code is a little ugly

import csv

#this list holds the skeletonUser objects
allUsersDemographics = []

#these lists are used for t2 is we are doing both timepoints
usersLattice2 = []
usersSmall2 = []

#these lists are used for t3 is we are doing both timepoints
usersLattice3 = []
usersSmall3 = []

#these are the defualt lists that all of the methods use
#if we are using both timepoints, the above four lists are combined into
#these lists. See my note above the setFriends method for more info
usersLattice = []
usersSmall = []

#when a user lists another user as a close friend, the username pair is put
#into this list with the user that listed the other user first
oneWayFriendships = []

#class that stores the username of a friend and their demographics
class friend:
    def __init__(self, usrnme):
        #if blank set to null
        if usrnme == "":
            usrnme = "null"
        self.username = usrnme
        self.similarAge = False
        self.sameGender = False
        self.samePrimarySub = False
        self.sameSecondarySub = False
        self.sameEducation = False
        self.sameIncome = False
        self.sameCurrentSmoker = False
        self.sameExSmoker = False
        self.close = ""

#main class, stores a users friends and demographics
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

    #easy method to see the closeness of their friends to what we read from the csv
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

#this class is used for user comparisons
#some users are not in the survey but were listed as a friends and in this case
#we can't directly compare users because they don't have a user object
#this class circumvents that by creating a skeletonUser object that contains
#all users even if they weren't in the survey for comparison
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

#if using both timepoints put t2 data in usersLattice2 and usersSmall2
#and t3 data in usersLattice3 and usersSmall3
#then call the combine timepoints method
#if only using one timepoint put the data from that timepoint into
#usersLattice and usersSmall and don't call the combine method

#currently set up to only user t3 data
#creates all of the user objects for use later from the csvs
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
        with open('sameClose.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                currentUser = user(row["user"], row["buddy1"], row["buddy2"], row["buddy3"], row["buddy4"], row["buddy5"], row["buddy6"])
                parsedUsername = row["user"]
                parsedUsername = parsedUsername[1:]
                currentUser.setCloseness(row["Closeness1"], row["Closeness2"], row["Closeness3"], row["Closeness4"], row["Closeness5"], row["Closeness6"])
                if int(parsedUsername) <= 4128:
                    usersLattice.append(currentUser)
                else:
                    usersSmall.append(currentUser)

#creates all of the skeleton user objects for demographic comparison
#also updates the user objects with their demographics
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

#sets the similarity characteristics for all users and their friends
#ex "sameIncome" would be set to True
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

#this method does the heavy lifting for set similarities
#this is the method that actually does the comparing between users
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
    if user1.someHighSchool == 1 and user2.someHighSchool == 1 or user1.highSchool == 1 and user2.highSchool == 1 or user1.someCollege == 1 and user2.someCollege == 1 or user1.Bachelors == 1 and user2.Bachelors == 1 or user1.Associates == 1 and user2.Associates == 1 or user1.Masters == 1 and user2.Masters == 1 or user1.Doctoral == 1 and user2.Doctoral== 1:
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

#this method gets the number of not close, somewhat close, and very close friends for all usersLattice
#then adds them together and outputs the total numbers
def tallyCloseness(toWrite):
    writer = open(toWrite, 'a')

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
                    oneWayFriendships.append((lattUser.username, currFriend.username))
                    lattSomewhat += 1
                elif currFriend.close == "very close":
                    lattUser.closeFriends.append(currFriend)
                    oneWayFriendships.append((lattUser.username, currFriend.username))
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
                    oneWayFriendships.append((smallUser.username, currFriend.username))
                    smallSomewhat += 1
                elif currFriend.close == "very close":
                    smallUser.closeFriends.append(currFriend)
                    oneWayFriendships.append((smallUser.username, currFriend.username))
                    smallClose += 1

    writer.write("Among all of the data from Timepoint 3 we found:\n")
    writer.write("Number of Not Close Users in the Lattice Network: ")
    writer.write(str(lattNotClose))
    writer.write("\n")
    writer.write("Number of Somewhat Close Users in the Lattice Network: ")
    writer.write(str(lattSomewhat))
    writer.write("\n")
    writer.write("Number of Very Close Users in the Lattice Network: ")
    writer.write(str(lattClose))
    writer.write("\n")
    writer.write("\n\n")
    writer.write("Number of Not Close Users in the Small World Network: ")
    writer.write(str(smallNotClose))
    writer.write("\n")
    writer.write("Number of Somewhat Close Users in the Small World Network: ")
    writer.write(str(smallSomewhat))
    writer.write("\n")
    writer.write("Number of Very Close Users in the Small World Network: ")
    writer.write(str(smallClose))
    writer.write("\n\n")
    writer.write("Number of Not Close Users in both networks: ")
    writer.write(str(smallNotClose + lattNotClose))
    writer.write("\n")
    writer.write("Number of Somewhat Close Users in both networks: ")
    writer.write(str(smallSomewhat + lattSomewhat))
    writer.write("\n")
    writer.write("Number of Very Close Users in both networks: ")
    writer.write(str(smallClose + lattClose))
    writer.write("\n\n\n")

#combines the two users into the user1 object
#used to combine the timepoint data
#ideally this method is called on two users with the same name
#this method is currently useless because we are only using t3 data
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
#used for debugging, can be useful though, not currently called anywhere
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

#prints the statistics of similarity for all users
#totals them up and prints the number of similarities between close friends
def createStatistics(toWrite):
    writer = open(toWrite, 'a')

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

    writer.write("Lattice Network Statistics, 23 total relationships\n")
    writer.write("-------------------------------------------------\n")
    writer.write("Number with a similar age: ")
    writer.write(str(numSimilarAge))
    writer.write("\n")
    writer.write("Number with the same gender: ")
    writer.write(str(numSameGender))
    writer.write("\n")
    writer.write("Number with the same primary addiction: ")
    writer.write(str(numSamePrimary))
    writer.write("\n")
    writer.write("Number with the same secondary addiction: ")
    writer.write(str(numSameSecondary))
    writer.write("\n")
    writer.write("Number with the same education level: ")
    writer.write(str(numSameEducation))
    writer.write("\n")
    writer.write("Number with the same income level: ")
    writer.write(str(numSameIncome))
    writer.write("\n")
    writer.write("Number that were both current smokers: ")
    writer.write(str(numSameCurrentSmoker))
    writer.write("\n")
    writer.write("Number that were both ex smokers: ")
    writer.write(str(numSameExSmoker))
    writer.write("\n\n")

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

    writer.write("Small World Network Statistics, 32 total relationships\n")
    writer.write("-------------------------------------------------\n")
    writer.write("Number with a similar age: ")
    writer.write(str(numSimilarAge2))
    writer.write("\n")
    writer.write("Number with the same gender: ")
    writer.write(str(numSameGender2))
    writer.write("\n")
    writer.write("Number with the same primary addiction: ")
    writer.write(str(numSamePrimary2))
    writer.write("\n")
    writer.write("Number with the same secondary addiction: ")
    writer.write(str(numSameSecondary2))
    writer.write("\n")
    writer.write("Number with the same education level: ")
    writer.write(str(numSameEducation2))
    writer.write("\n")
    writer.write("Number with the same income level: ")
    writer.write(str(numSameIncome2))
    writer.write("\n")
    writer.write("Number that were both current smokers: ")
    writer.write(str(numSameCurrentSmoker2))
    writer.write("\n")
    writer.write("Number that were both ex smokers: ")
    writer.write(str(numSameExSmoker2))
    writer.write("\n\n")

    writer.write("Combined Statistics, 55 total relationships\n")
    writer.write("-------------------------------------------------\n")
    writer.write("Number with a similar age: ")
    writer.write(str(numSimilarAge + numSimilarAge2))
    writer.write("\n")
    writer.write("Number with the same gender: ")
    writer.write(str(numSameGender + numSameGender2))
    writer.write("\n")
    writer.write("Number with the same primary addiction: ")
    writer.write(str(numSamePrimary + numSamePrimary2))
    writer.write("\n")
    writer.write("Number with the same secondary addiction: ")
    writer.write(str(numSameSecondary + numSameSecondary2))
    writer.write("\n")
    writer.write("Number with the same education level: ")
    writer.write(str(numSameEducation + numSameEducation2))
    writer.write("\n")
    writer.write("Number with the same income level: ")
    writer.write(str(numSameIncome + numSameIncome2))
    writer.write("\n")
    writer.write("Number that were both current smokers: ")
    writer.write(str(numSameCurrentSmoker + numSameCurrentSmoker2))
    writer.write("\n")
    writer.write("Number that were both ex smokers: ")
    writer.write(str(numSameExSmoker + numSameExSmoker2))
    writer.write("\n\n")

#adds up the number of entries we had to remove because the data was bad
#does this using the csvs of bad and good friendships that Mary created
def sumRemovedEntries(toWrite):
    writer = open(toWrite, 'a')
    sumSame = 0
    sumDifferent = 0
    total = 0
    for currUser in usersLattice:
        for currFriend in currUser.friends:
            if currFriend.username == "null" and currFriend.close != "":
                sumDifferent += 1
            elif currFriend.username != "null":
                sumSame += 1

    for currUser in usersSmall:
        for currFriend in currUser.friends:
            if currFriend.username == "null" and currFriend.close != "":
                sumDifferent += 1
            elif currFriend.username != "null":
                sumSame += 1

    total = sumSame + sumDifferent

    writer.write("We had to remove ")
    writer.write(str(sumDifferent))
    writer.write(" out of ")
    writer.write(str(total))
    writer.write(" for a total of ")
    writer.write(str(sumSame))
    writer.write(" good entries.\n")

#searches the list of oneWayFriendships for reciprocal friends
#then creates a new list and prints stats about 1 and 2 way friendships
def printTwoWayFriendships(toWrite):
    writer = open(toWrite, 'a')
    twoWayFriendships = []

    for relationship in oneWayFriendships:
        firstUser, secondUser = relationship
        for relationship2 in oneWayFriendships:
            firstUser2, secondUser2 = relationship2
            if firstUser == secondUser2 and secondUser ==firstUser2:
                twoWayFriendships.append((firstUser, secondUser))
    writer.write("The number of one-way friendships we found is ")
    writer.write(str(len(oneWayFriendships) - len(twoWayFriendships)))
    writer.write("\n")
    writer.write("The number of two-way friendships we found is ")
    #divide by two because we counted each two way friendship twice
    writer.write(str(len(twoWayFriendships)/2))
    writer.write("\n")
    writer.write("For a total of ")
    writer.write(str((len(oneWayFriendships) - len(twoWayFriendships) + len(twoWayFriendships)/2)))
    writer.write(" friendships")
    #use to see which friendshships were two way, duplicates
    #writer.write(twoWayFriendships)

#clear the file so we can write to it
def clearFile(toClear):
    open(toClear, 'w').close()

#main, actually executes the methods
clearFile('Timepoint3Statistics.txt')
setFriends(3)
setDemographics()
setSimilarities()
tallyCloseness('Timepoint3Statistics.txt')

orderList(usersLattice)
orderList(usersSmall)
orderList(allUsersDemographics)

createStatistics('Timepoint3Statistics.txt')
sumRemovedEntries('Timepoint3Statistics.txt')

printTwoWayFriendships('Timepoint3Statistics.txt')
