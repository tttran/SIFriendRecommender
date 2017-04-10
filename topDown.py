#Top Down approach to homophily
#Wilson Rhodes & Timothy Tran


import csv

usersLattice = []
usersSmall = []

class user:
    def __init__(self, username, friend1, friend2, friend3, friend4, friend5, friend6):
        self.username = username
        self.somewhatCloseFriends = []
        self.closeFriends = []

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

        self.friend1 = friend1
        self.similarAge1 = False
        self.sameGender1 = False
        self.samePrimarySub1 = False
        self.sameSecondarySub1 = False
        self.sameEducation1 = False
        self.sameIncome1 = False
        self.sameCurrentSmoker1 = False
        self.sameExSmoker1 = False
        self.close1 = ""

        self.friend2 = friend2
        self.similarAge2 = False
        self.sameGender2 = False
        self.samePrimarySub2 = False
        self.sameSecondarySub2 = False
        self.sameEducation2 = False
        self.sameIncome2 = False
        self.sameCurrentSmoker2 = False
        self.sameExSmoker2 = False
        self.close2 = ""

        self.friend3 = friend3
        self.similarAge3 = False
        self.sameGender3 = False
        self.samePrimarySub3 = False
        self.sameSecondarySub3 = False
        self.sameEducation3 = False
        self.sameIncome3 = False
        self.sameCurrentSmoker3 = False
        self.sameExSmoker3 = False
        self.close3 = ""

        self.friend4 = friend4
        self.similarAge4 = False
        self.sameGender4 = False
        self.samePrimarySub4 = False
        self.sameSecondarySub4 = False
        self.sameEducation4 = False
        self.sameIncome4 = False
        self.sameCurrentSmoker4 = False
        self.sameExSmoker4 = False
        self.close4 = ""

        self.friend5 = friend5
        self.similarAge5 = False
        self.sameGender5 = False
        self.samePrimarySub5 = False
        self.sameSecondarySub5 = False
        self.sameEducation5 = False
        self.sameIncome5 = False
        self.sameCurrentSmoker5 = False
        self.sameExSmoker5 = False
        self.close5 = ""

        self.friend6 = friend6
        self.similarAge6 = False
        self.sameGender6 = False
        self.samePrimarySub6 = False
        self.sameSecondarySub6 = False
        self.sameEducation6 = False
        self.sameIncome6 = False
        self.sameCurrentSmoker6 = False
        self.sameExSmoker6 = False
        self.close6 = ""

    def setCloseness(self, howClose1, howClose2, howClose3, howClose4, howClose5, howClose6):
        self.close1 = howClose1
        self.close2 = howClose2
        self.close3 = howClose3
        self.close4 = howClose4
        self.close5 = howClose5
        self.close6 = howClose6

    def printFriends(self):
        print self.friend1
        print self.friend2
        print self.friend3
        print self.friend4
        print self.friend5
        print self.friend6

    def printCloseness(self):
        print self.close1
        print self.close2
        print self.close3
        print self.close4
        print self.close5
        print self.close6

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

        print self.friend1
        print self.similarAge1
        print self.sameGender1
        print self.samePrimarySub1
        print self.sameSecondarySub1
        print self.sameEducation1
        print self.sameIncome1
        print self.sameCurrentSmoker1
        print self.sameExSmoker1

        print self.friend2
        print self.similarAge2
        print self.sameGender2
        print self.samePrimarySub2
        print self.sameSecondarySub2
        print self.sameEducation2
        print self.sameIncome2
        print self.sameCurrentSmoker2
        print self.sameExSmoker2

        print self.friend3
        print self.similarAge3
        print self.sameGender3
        print self.samePrimarySub3
        print self.sameSecondarySub3
        print self.sameEducation3
        print self.sameIncome3
        print self.sameCurrentSmoker3
        print self.sameExSmoker3

        print self.friend4
        print self.similarAge4
        print self.sameGender4
        print self.samePrimarySub4
        print self.sameSecondarySub4
        print self.sameEducation4
        print self.sameIncome4
        print self.sameCurrentSmoker4
        print self.sameExSmoker4

        print self.friend5
        print self.similarAge5
        print self.sameGender5
        print self.samePrimarySub5
        print self.sameSecondarySub5
        print self.sameEducation5
        print self.sameIncome5
        print self.sameCurrentSmoker5
        print self.sameExSmoker5

        print self.friend6
        print self.similarAge6
        print self.sameGender6
        print self.samePrimarySub6
        print self.sameSecondarySub6
        print self.sameEducation6
        print self.sameIncome6
        print self.sameCurrentSmoker6
        print self.sameExSmoker6

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
                    usersLattice.append(currentUser)
                else:
                    usersSmall.append(currentUser)

    if timepoint == 3:
        with open('Timepoint3AllData.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                currentUser = user(row["username"], row["Recovery Buddy [1]"], row["Recovery Buddy [2]"], row["Recovery Buddy [3]"], row["Recovery Buddy [4]"], row["Recovery Buddy [5]"], row["Recovery Buddy [6]"])
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

            #currentUser.printDemographics()
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
        #if friend is good data
        if currUser.friend1 != "null":
            compareName = currUser.friend1
            compareUser = currUser
            #find compare object
            for findFriend in usersLattice:
                if findFriend.username == compareName:
                    compareUser = findFriend
                    break
            #do comparison
            compareTwoUsers(currUser, compareUser, 1)

        #if friend is good data
        if currUser.friend2 != "null":
            compareName = currUser.friend2
            compareUser = currUser
            #find compare object
            for findFriend in usersLattice:
                if findFriend.username == compareName:
                    compareUser = findFriend
                    break
            #do comparison
            compareTwoUsers(currUser, compareUser, 2)

        #if friend is good data
        if currUser.friend1 != "null":
            compareName = currUser.friend3
            compareUser = currUser
            #find compare object
            for findFriend in usersLattice:
                if findFriend.username == compareName:
                    compareUser = findFriend
                    break
            #do comparison
            compareTwoUsers(currUser, compareUser, 3)

        #if friend is good data
        if currUser.friend4 != "null":
            compareName = currUser.friend4
            compareUser = currUser
            #find compare object
            for findFriend in usersLattice:
                if findFriend.username == compareName:
                    compareUser = findFriend
                    break
            #do comparison
            compareTwoUsers(currUser, compareUser, 4)

        #if friend is good data
        if currUser.friend5 != "null":
            compareName = currUser.friend5
            compareUser = currUser
            #find compare object
            for findFriend in usersLattice:
                if findFriend.username == compareName:
                    compareUser = findFriend
                    break
            #do comparison
            compareTwoUsers(currUser, compareUser, 5)

        #if friend is good data
        if currUser.friend6 != "null":
            compareName = currUser.friend6
            compareUser = currUser
            #find compare object
            for findFriend in usersLattice:
                if findFriend.username == compareName:
                    compareUser = findFriend
                    break
            #do comparison
            compareTwoUsers(currUser, compareUser, 6)

    #for each user
    for currUser in usersSmall:
        #if friend is good data
        if currUser.friend1 != "null":
            compareName = currUser.friend1
            compareUser = currUser
            #find compare object
            for findFriend in usersSmall:
                if findFriend.username == compareName:
                    compareUser = findFriend
                    break
            #do comparison
            compareTwoUsers(currUser, compareUser, 1)

        #if friend is good data
        if currUser.friend2 != "null":
            compareName = currUser.friend2
            compareUser = currUser
            #find compare object
            for findFriend in usersSmall:
                if findFriend.username == compareName:
                    compareUser = findFriend
                    break
            #do comparison
            compareTwoUsers(currUser, compareUser, 2)

        #if friend is good data
        if currUser.friend1 != "null":
            compareName = currUser.friend3
            compareUser = currUser
            #find compare object
            for findFriend in usersSmall:
                if findFriend.username == compareName:
                    compareUser = findFriend
                    break
            #do comparison
            compareTwoUsers(currUser, compareUser, 3)

        #if friend is good data
        if currUser.friend4 != "null":
            compareName = currUser.friend4
            compareUser = currUser
            #find compare object
            for findFriend in usersSmall:
                if findFriend.username == compareName:
                    compareUser = findFriend
                    break
            #do comparison
            compareTwoUsers(currUser, compareUser, 4)

        #if friend is good data
        if currUser.friend5 != "null":
            compareName = currUser.friend5
            compareUser = currUser
            #find compare object
            for findFriend in usersSmall:
                if findFriend.username == compareName:
                    compareUser = findFriend
                    break
            #do comparison
            compareTwoUsers(currUser, compareUser, 5)

        #if friend is good data
        if currUser.friend6 != "null":
            compareName = currUser.friend6
            compareUser = currUser
            #find compare object
            for findFriend in usersSmall:
                if findFriend.username == compareName:
                    compareUser = findFriend
                    break
            #do comparison
            compareTwoUsers(currUser, compareUser, 6)

def compareTwoUsers(user1, user2, friendNumber):
    #check if ages are +- 4
    ageDifference = int(user1.age) - int(user2.age)
    if ageDifference >= -4 and ageDifference <= 4:
        if friendNumber == 1:
            user1.similarAge1 = True
        if friendNumber == 2:
            user1.similarAge2 = True
        if friendNumber == 3:
            user1.similarAge3 = True
        if friendNumber == 4:
            user1.similarAge4 = True
        if friendNumber == 5:
            user1.similarAge5 = True
        if friendNumber == 6:
            user1.similarAge6 = True


    if user1.male == 1 and user2.male == 1 or user1.female == 1 and user2.female == 1:
        if friendNumber == 1:
            user1.sameGender1 = True
        if friendNumber == 2:
            user1.sameGender2 = True
        if friendNumber == 3:
            user1.sameGender3 = True
        if friendNumber == 4:
            user1.sameGender4 = True
        if friendNumber == 5:
            user1.sameGender5 = True
        if friendNumber == 6:
            user1.sameGender6 = True

    #check primary substance
    if user1.primAlcohol == 1 and user2.primAlcohol == 1 or user1.primCannabis == 1 and user2.primCannabis == 1 or user1.primCocaine == 1 and user2.primCocaine == 1 or user1.primOpiods == 1 and user2.primOpiods == 1 or user1.primPainRel == 1 and user2.primPainRel == 1 or user1.primStimulants == 1 and user2.primStimulants == 1:
        if friendNumber == 1:
            user1.samePrimarySub1 = True
        if friendNumber == 2:
            user1.samePrimarySub2 = True
        if friendNumber == 3:
            user1.samePrimarySub3 = True
        if friendNumber == 4:
            user1.samePrimarySub4 = True
        if friendNumber == 5:
            user1.samePrimarySub5 = True
        if friendNumber == 6:
            user1.samePrimarySub6 = True

    #check secondary substance
    if user1.secAlcohol == 1 and user2.secAlcohol == 1 or user1.secCannabis == 1 and user2.secCannabis == 1 or user1.secCocaine == 1 and user2.secCocaine == 1 or user1.secOpiods == 1 and user2.secOpiods == 1 or user1.secPainRel == 1 and user2.secPainRel == 1 or user1.secStimulants == 1 and user2.secStimulants == 1 or user1.secNico == 1 and user2.secNico == 1:
        if friendNumber == 1:
            user1.sameSecondarySub1 = True
        if friendNumber == 2:
            user1.sameSecondarySub2 = True
        if friendNumber == 3:
            user1.sameSecondarySub3 = True
        if friendNumber == 4:
            user1.sameSecondarySub4 = True
        if friendNumber == 5:
            user1.sameSecondarySub5 = True
        if friendNumber == 6:
            user1.sameSecondarySub6 = True

    #check education
    if user1.someHighSchool == 1 and user2.someHighSchool == 1 or user1.highSchool == 1 and user2.highSchool == 1 or user1.Associates == 1 and user2.Associates == 1 or user1.Bachelors == 1 and user2.Bachelors == 1 or user1.Associates == 1 and user2.Associates == 1 or user1.Masters == 1 and user2.Masters == 1 or user1.Doctoral == 1 and user2.Doctoral== 1:
        if friendNumber == 1:
            user1.sameEducation1 = True
        if friendNumber == 2:
            user1.sameEducation2 = True
        if friendNumber == 3:
            user1.sameEducation3 = True
        if friendNumber == 4:
            user1.sameEducation4 = True
        if friendNumber == 5:
            user1.sameEducation5 = True
        if friendNumber == 6:
            user1.sameEducation6 = True

    #check income
    if user1.lessThan30 == 1 and user2.lessThan30 == 1 or user1.thirtyTo50 == 1 and user2.thirtyTo50 == 1 or user1.fiftyTo70 == 1 and user2.fiftyTo70 == 1 or user1.seventyTo90 == 1 and user2.seventyTo90 == 1 or user1.ninetyTo150 == 1 and user2.ninetyTo150 == 1 or user1.greaterThan150 == 1 and user2.greaterThan150 == 1:
        if friendNumber == 1:
            user1.sameIncome1 = True
        if friendNumber == 2:
            user1.sameIncome2 = True
        if friendNumber == 3:
            user1.sameIncome3 = True
        if friendNumber == 4:
            user1.sameIncome4 = True
        if friendNumber == 5:
            user1.sameIncome5 = True
        if friendNumber == 6:
            user1.sameIncome6 = True

    #check current smoker
    if user1.currentSmoker == 1 and user2.currentSmoker == 1:
        if friendNumber == 1:
            user1.sameCurrentSmoker1 = True
        if friendNumber == 2:
            user1.sameCurrentSmoker2 = True
        if friendNumber == 3:
            user1.sameCurrentSmoker3 = True
        if friendNumber == 4:
            user1.sameCurrentSmoker4 = True
        if friendNumber == 5:
            user1.sameCurrentSmoker5 = True
        if friendNumber == 6:
            user1.sameCurrentSmoker6 = True

    #check ex smoker
    if user1.exSmoker == 1 and user2.exSmoker == 1:
        if friendNumber == 1:
            user1.sameExSmoker1 = True
        if friendNumber == 2:
            user1.sameExSmoker2 = True
        if friendNumber == 3:
            user1.sameExSmoker3 = True
        if friendNumber == 4:
            user1.sameExSmoker4 = True
        if friendNumber == 5:
            user1.sameExSmoker5 = True
        if friendNumber == 6:
            user1.sameExSmoker6 = True

def tallyCloseness():
    lattNotClose = 0
    lattSomewhat = 0
    lattClose = 0
    for lattUser in usersLattice:
        if lattUser.friend1 != "null":
            if lattUser.close1 == "not close":
                lattNotClose += 1
            elif lattUser.close1 == "somewhat close":
                lattUser.somewhatCloseFriends.append(lattUser.friend1)
                lattSomewhat += 1
            elif lattUser.close1 == "very close":
                lattUser.closeFriends.append(lattUser.friend1)
                lattClose += 1
        if lattUser.friend2 != "null":
            if lattUser.close2 == "not close":
                lattNotClose += 1
            elif lattUser.close2 == "somewhat close":
                lattUser.somewhatCloseFriends.append(lattUser.friend2)
                lattSomewhat += 1
            elif lattUser.close2 == "very close":
                lattUser.closeFriends.append(lattUser.friend2)
                lattClose += 1
        if lattUser.friend3 != "null":
            if lattUser.close3 == "not close":
                lattNotClose += 1
            elif lattUser.close3 == "somewhat close":
                lattUser.somewhatCloseFriends.append(lattUser.friend3)
                lattSomewhat += 1
            elif lattUser.close3 == "very close":
                lattUser.closeFriends.append(lattUser.friend3)
                lattClose += 1
        if lattUser.friend4 != "null":
            if lattUser.close4 == "not close":
                lattNotClose += 1
            elif lattUser.close4 == "somewhat close":
                lattUser.somewhatCloseFriends.append(lattUser.friend4)
                lattSomewhat += 1
            elif lattUser.close4 == "very close":
                lattUser.closeFriends.append(lattUser.friend4)
                lattClose += 1
        if lattUser.friend5 != "null":
            if lattUser.close5 == "not close":
                lattNotClose += 1
            elif lattUser.close5 == "somewhat close":
                lattUser.somewhatCloseFriends.append(lattUser.friend5)
                lattSomewhat += 1
            elif lattUser.close5 == "very close":
                lattUser.closeFriends.append(lattUser.friend5)
                lattClose += 1
        if lattUser.friend6 != "null":
            if lattUser.close6 == "not close":
                lattNotClose += 1
            elif lattUser.close6 == "somewhat close":
                lattUser.somewhatCloseFriends.append(lattUser.friend6)
                lattSomewhat += 1
            elif lattUser.close6 == "very close":
                lattUser.closeFriends.append(lattUser.friend6)
                lattClose += 1

    smallNotClose = 0
    smallSomewhat = 0
    smallClose = 0
    for smallUser in usersSmall:
        if smallUser.friend1 != "null":
            if smallUser.close1 == "not close":
                smallNotClose += 1
            elif smallUser.close1 == "somewhat close":
                smallUser.somewhatCloseFriends.append(smallUser.friend1)
                smallSomewhat += 1
            elif smallUser.close1 == "very close":
                smallUser.closeFriends.append(smallUser.friend1)
                smallClose += 1
        if smallUser.friend2 != "null":
            if smallUser.close2 == "not close":
                smallNotClose += 1
            elif smallUser.close2 == "somewhat close":
                smallUser.somewhatCloseFriends.append(smallUser.friend2)
                smallSomewhat += 1
            elif smallUser.close2 == "very close":
                smallUser.closeFriends.append(smallUser.friend2)
                smallClose += 1
        if smallUser.friend3 != "null":
            if smallUser.close3 == "not close":
                smallNotClose += 1
            elif smallUser.close3 == "somewhat close":
                smallUser.somewhatCloseFriends.append(smallUser.friend3)
                smallSomewhat += 1
            elif smallUser.close3 == "very close":
                smallUser.closeFriends.append(smallUser.friend3)
                smallClose += 1
        if smallUser.friend4 != "null":
            if smallUser.close4 == "not close":
                smallNotClose += 1
            elif smallUser.close4 == "somewhat close":
                smallUser.somewhatCloseFriends.append(smallUser.friend4)
                smallSomewhat += 1
            elif smallUser.close4 == "very close":
                smallUser.closeFriends.append(smallUser.friend4)
                smallClose += 1
        if smallUser.friend5 != "null":
            if smallUser.close5 == "not close":
                smallNotClose += 1
            elif smallUser.close5 == "somewhat close":
                smallUser.somewhatCloseFriends.append(smallUser.friend5)
                smallSomewhat += 1
            elif smallUser.close5 == "very close":
                smallUser.closeFriends.append(smallUser.friend5)
                smallClose += 1
        if smallUser.friend6 != "null":
            if smallUser.close6 == "not close":
                smallNotClose += 1
            elif smallUser.close6 == "somewhat close":
                smallUser.somewhatCloseFriends.append(smallUser.friend6)
                smallSomewhat += 1
            elif smallUser.close6 == "very close":
                smallUser.closeFriends.append(smallUser.friend6)
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

#main
setFriends(3)
setDemographics()
setSimilarities(3)
tallyCloseness()
#print somewhat close and very close friend pairs
for lattUser in usersLattice:
    if len(lattUser.somewhatCloseFriends) > 0 or len(lattUser.closeFriends) > 0:
        print "User: " + lattUser.username
        print "Somewhat close friends: ",
        print lattUser.somewhatCloseFriends
        print "Close Friends: ",
        print lattUser.closeFriends
        print "\n\n"

for smallUser in usersSmall:
    if len(smallUser.somewhatCloseFriends) > 0 or len(smallUser.closeFriends) > 0:
        print "User: " + smallUser.username
        print "Somewhat close friends: ",
        print smallUser.somewhatCloseFriends
        print "Close Friends: ",
        print smallUser.closeFriends
        print "\n\n"
#print usersLattice[0].username
#print usersLattice[0].female
#print usersLattice[52].username
#print usersLattice[52].female
#for user in usersLattice:
#    user.printFriends()
