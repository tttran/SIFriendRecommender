#Friend Recommender - Parsing
#Trevor Kinaman
#3/30/2016

import csv
import time

addictionList = ['Alcohol', 'Binge Eating', 'Caffeine', 'Cannabis', 'Cocaine', 'Internet',
                    'Sexual Activity', 'Shopping', 'Nicotine', 'Opioids', 'Pain Relievers',
                    'Stimulants', 'Tranquilizers/Depressants', 'Other']

addictionDict = {"Alcohol (liquor, beer, wine)":0,
                     "Binge eating or other eating disorders":1,
                     "Caffeine (coffee, tea, soda, energy drinks, 5-hour energy)":2,
                     "Cannabis products (marijuana, hashish, hash, THC, pot, grass, weed, reefer, spice, K2)":3,
                     "Cocaine (snorting, IV, freebase, crack)":4,
                     "Excessive preoccupation with activities on the Internet":5,
                     "Excessive sexual activity":6,
                     "Excessive shopping":7,
                     "Nicotine (cigarettes, cigars, smokeless tobacco, pipe tobacco)":8,
                     "Opioids (heroin, opium, morphine, methadone)":9,
                     "Prescription pain relievers (codeine, OxyContin, Tylox, Percodan, Percocet, Demerol, Vicodin, Actiq, Duragesic, Sublimaze, Darvon, Darvocet, Lorcet, Lortab, Dilaudid)":10,
                     "Stimulants (amphetamines, methamphetamine, speed, crystal meth, crank, Dexedrine, methylphenidate, Ritalin, diet pills, bath salts, Adderall)":11,
                     "Tranquilizers/Depressants (barbiturates, benzodiazapines, Ativan, Halcion, Valium, Xanax, Librium, Dalmane, Rohypnol, roofies, Roofinol, GHB, Quaalude, Seconal, reds, Miltown)":12,
                     "Other": 13}

educationList = ["High school diploma or equivalency", "Some college", "Bachelors degree",
                 "Masters degree", "Doctoral degree", "Associates degree"]

educationDict = {"High school diploma or equivalency":0,
                 "Some college":1,
                 "Bachelors degree":2,
                 "Masters degree":3,
                 "Doctoral degree":4,
                 "Associates degree":5}

incomeList = ["Less than $30,000", "$30,000 - $49,999", "$50,000 - $69,999",
              "$70,000 - $89,999", "$90,000 - $149,999", "$150,000 and above"]

incomeDict = {"Less than $30,000":0,
              "$30,000 - $49,999":1,
              "$50,000 - $69,999":2,
              "$70,000 - $89,999":3,
              "$90,000 - $149,999":4,
              "$150,000 and above":5}

months = {"January":1, "February":2, "March":3, "April":4, "May":5,
              "June":6, "July":7, "August":8, "September":9, "October":10,
              "November":11, "December":12}

genders = {"Male":0, "Female":1}

todaysMonth = time.strftime("%B")
todaysYear = time.strftime("%Y")

#input: string of the user's addiction from the dictionary
#dictionaryKey: "What was your p... []"
#output: list - [0, 0, 0, 1, 0,..., 0] list of addictions, 1 for their addiction
def parseAddiction(str):
    list = [0] * len(addictionDict)
    if(str in addictionDict):
        list[addictionDict[str]] = 1
    else:
        list[addictionDict["Other"]] = 1
    return(list)

#input: string for month and string for year from dictionary    
#dictionaryKeys: "Month of Birth:... []" and "Year of birth: []"
#output: list - [54] list of 1 number, age of the user
def parseAge(month, year):
    age = int(todaysYear) - int(year)
    if(int(months[todaysMonth]) < int(months[month])):
        age -= 1
    return([age])

#input: string of the user's gender from the dictionary
#dictionaryKey: "Gender:\n\n\n\n\t&nb... []"
#output: list - [0, 1, 0] list of genders, 1 for their gender
def parseGender(str):
    list = [0, 0, 0]
    if(str in genders):
        list[genders[str]] = 1
    else:
        list[2] = 1
    return(list)

#input: string of the user's education level from the dictionary
#dictionaryKey: "Education: []"
#output: list - [0, 0, 0, 1, 0,..., 0] list of educations, 1 for their education
def parseEducation(str):
    list = [0] * len(educationDict)
    if(str in educationDict):
        list[educationDict[str]] = 1
    return(list)

#input: string of the user's income from the dictionary
#dictionaryKey: "Household Incom... []"
#output: list - [0, 0, 0, 1, 0,..., 0] list of incomes, 1 for their income
def parseIncome(str):
    list = [0] * len(incomeDict)
    if(str in incomeDict):
        list[incomeDict[str]] = 1
    return(list)

#main
with open('HomophilyData.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    with open('HomophilyDataParsed.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['id', 'Age'] + ['Male', 'Female', 'Other'] + addictionList + educationList + incomeList)
        for row in reader:
            data = [row["id"]] + parseAge(row["Month of Birth:... []"], row["Year of birth: []"]) + parseGender(row["Gender:\n\n\n\n\t&nb... []"]) + parseAddiction(row["What was your p... []"]) + parseEducation(row["Education: []"]) + parseIncome(row["Household Incom... []"])
            writer.writerow(data)
