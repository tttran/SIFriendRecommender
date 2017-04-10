#Top Down approach to homophily
#Wilson Rhodes & Timothy Tran

import csv

usersLattice = []
usersSmall = []

class user:
    def __init__(self, username, friend1, friend2, friend3, friend4, friend5, friend6):
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
        self.seventTo90 = 0
        self.ninetyTo150 = 0
        self.greaterThan150 = 0
        self.preferNotToAns = 0

        self.currentSmoker = 0
        self.exSmoker = 0

        self.friend1 = friend1
        self.similarAge1 = False
        self.samePrimarySub1 = False
        self.sameSecondarySub1 = False
        self.sameEducation1 = False
        self.sameIncome1 = False
        self.sameCurrentSmoker1 = False
        self.sameExSmoker1 = False

        self.friend2 = friend2
        self.similarAge2 = False
        self.samePrimarySub2 = False
        self.sameSecondarySub2 = False
        self.sameEducation2 = False
        self.sameIncome2 = False
        self.sameCurrentSmoker2 = False
        self.sameExSmoker2 = False

        self.friend3 = friend3
        self.similarAge3 = False
        self.samePrimarySub3 = False
        self.sameSecondarySub3 = False
        self.sameEducation3 = False
        self.sameIncome3 = False
        self.sameCurrentSmoker3 = False
        self.sameExSmoker3 = False

        self.friend4 = friend4
        self.similarAge4 = False
        self.samePrimarySub4 = False
        self.sameSecondarySub4 = False
        self.sameEducation4 = False
        self.sameIncome4 = False
        self.sameCurrentSmoker4 = False
        self.sameExSmoker4 = False

        self.friend5 = friend5
        self.similarAge5 = False
        self.samePrimarySub5 = False
        self.sameSecondarySub5 = False
        self.sameEducation5 = False
        self.sameIncome5 = False
        self.sameCurrentSmoker5 = False
        self.sameExSmoker5 = False

        self.friend6 = friend6
        self.similarAge6 = False
        self.samePrimarySub6 = False
        self.sameSecondarySub6 = False
        self.sameEducation6 = False
        self.sameIncome6 = False
        self.sameCurrentSmoker6 = False
        self.sameExSmoker6 = False

    def printFriends(self):
        print self.friend1
        print self.friend2
        print self.friend3
        print self.friend4
        print self.friend5
        print self.friend6

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

def setFriends():
    with open('Timepoint2Clean.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            currentUser = user(row["username"], row["Recovery Buddy [1]"], row["Recovery Buddy [2]"], row["Recovery Buddy [3]"], row["Recovery Buddy [4]"], row["Recovery Buddy [5]"], row["Recovery Buddy [6]"])
            parsedUsername = row["username"]
            parsedUsername = parsedUsername[1:]
            if(int(parsedUsername) <= 4128):
                usersLattice.append(currentUser)
            else:
                usersSmall.append(currentUser)

def setSimilarities():
    with open('DemoLattice.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:

            for checkUser in usersLattice:
                if row["ID"] == checkUser.username:
                    currentUser = checkUser
                    break

            currentUser.age = row["Age"]
            currentUser.male = row["Male"]
            currentUser.female = row["Female"]
            currentUser.other = row["Other"]

            currentUser.primarySub = row["Primary Sub. Add."]
            currentUser.primAlcohol = row["Alcohol"]
            currentUser.primCannabis = row["Cannabis"]
            currentUser.primCocaine = row["Cocaine"]
            currentUser.primOpiods = row["Opiods"]
            currentUser.primPainRel = row["Presc. Pain Relivers"]
            currentUser.primStimulants = row["Stimulants"]
            currentUser.primTranq = row["Traq/Depres."]
            currentUser.primDiss = row["Dissociatives"]

            currentUser.secondarySub = row["Secondary Sub. Add."]
            currentUser.secAlcohol = row["SAlcohol"]
            currentUser.secCannabis = row["SCannabis"]
            currentUser.secCocaine = row["SCocaine"]
            currentUser.secOpiods = row["SOpiods"]
            currentUser.secPainRel = row["SPresc. Pain Relivers"]
            currentUser.secStimulants = row["Stimulants"]
            currentUser.secTranq = row["Traq/Depres."]
            currentUser.secNico = row["SNicotine"]
            currentUser.other = row["Other (non-subs)"]

            currentUser.someHighSchool = row["Some High School"]
            currentUser.highSchool = row["High school diploma or equivalency"]
            currentUser.someCollege = row["Some College"]
            currentUser.Associates = row["Associates Deg."]
            currentUser.Bachelors = row["Bach. Deg."]
            currentUser.Masters = row["Mast. Deg."]
            currentUser.Doctoral = row["Doc. Deg."]

            currentUser.lessThan30 = row["Less than $30,000"]
            currentUser.thirtyTo50 = row["$30,000 - $49,999"]
            currentUser.fiftyTo70 = row["$50,000 - $69,999"]
            currentUser.seventTo90 = row["$70,000 - $89,999"]
            currentUser.ninetyTo150 = row["$90,000 - $149,999"]
            currentUser.greaterThan150 = row["$150,000 and above"]
            currentUser.preferNotToAns = row["Prefer Not to Answer"]

            currentUser.currentSmoker = row["Current Smoker"]
            currentUser.exSmoker = row["Ex-Smoker"]

#main
setFriends()
setSimilarities()
usersLattice[2].printDemographics()
#for user in usersLattice:
#    user.printFriends()
