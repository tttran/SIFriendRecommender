import pandas
import numpy as np

#import files
users = pandas.read_csv('users.csv')
tp3 = pandas.read_csv('TimePoint3.csv')

#Name column headings, add u to user value
pandas.set_option('precision', 0)

#Remove unneeded columns and rename column headings
tp3.drop(tp3.columns[[0, 1]], axis=1, inplace=True)
tp3.drop(tp3.columns[7:18], axis=1, inplace=True)
tp3.drop(tp3.columns[8:19], axis=1, inplace=True)
tp3.drop(tp3.columns[9:20], axis=1, inplace=True)
tp3.drop(tp3.columns[10:21], axis=1, inplace=True)
tp3.drop(tp3.columns[11:22], axis=1, inplace=True)
tp3.drop(tp3.columns[12:23], axis=1, inplace=True)
tp3.columns = ["username", "Buddy1", "Buddy2", "Buddy3", "Buddy4", "Buddy5", "Buddy6", "Close1", "Close2", "Close3", "Close4", "Close5", "Close6"]

#convert to string
tp3.Buddy1 = tp3.Buddy1.astype(str)
tp3.Buddy2 = tp3.Buddy2.astype(str)
tp3.Buddy3 = tp3.Buddy3.astype(str)
tp3.Buddy4 = tp3.Buddy4.astype(str)
tp3.Buddy5 = tp3.Buddy5.astype(str)
tp3.Buddy6 = tp3.Buddy6.astype(str)

#add u before user and buddy numbers
tp3['Buddy1'] = 'u' + tp3.Buddy1 
tp3['Buddy2'] = 'u' + tp3.Buddy2
tp3['Buddy3'] = 'u' + tp3.Buddy3
tp3['Buddy4'] = 'u' + tp3.Buddy4
tp3['Buddy5'] = 'u' + tp3.Buddy5
tp3['Buddy6'] = 'u' + tp3.Buddy6

#remove the decimal .0 from values
def trim_fraction(text):
    if '.0' in text:
        return text[:text.rfind('.0')]
    return text
tp3.Buddy1 = tp3.Buddy1.apply(trim_fraction)
tp3.Buddy2 = tp3.Buddy2.apply(trim_fraction)
tp3.Buddy3 = tp3.Buddy3.apply(trim_fraction)
tp3.Buddy4 = tp3.Buddy4.apply(trim_fraction)
tp3.Buddy5 = tp3.Buddy5.apply(trim_fraction)
tp3.Buddy6 = tp3.Buddy6.apply(trim_fraction)


#Sort the users buddy table to order first by UID and then decending by the Self value to find user sets - a user and their 6+ buddies
users = users.sort_values(['uid', 'self'], ascending=[True, False])

#create empty arrays, table = will hold each user from users and the buddies they have
#row = an empty array representing each row in the table
table = []
row = []

#Go through the users table, change to format containing a particular user and their buddies
for index, record in users.iterrows(): 
    if record.self == 1:
        if len(row) != 0:
            table.append(row)
            row = []
        row.append(record['nick'])
    else:
        row.append(record['nick'])
table.append(row)

#Change headers of table to match that of timepoint3
headers = []
for i in range(66):
    if i == 0:
        headers.append("user")
    else:
        headers.append("buddy" + str(i))
    
#turn table into a dataframe
table2 = pandas.DataFrame(table, columns=headers)

#create empty array to represent the similar buddies that both timepoint3 and users, aka table2 share
same = []
close = []

#go through table2 and find all the buddies that a user also lists in timepoint3
for index, rows in table2.iterrows():
    tp3Same = tp3.loc[tp3.username == rows.user].as_matrix()
    tp3Same = tp3Same[:,1:] #remove username from row to just look at buddies
    tp3Same = tp3Same.ravel() #remove empty array values
    tp3Same = list(tp3Same) #convert to list to add commas
    table2Same = rows.as_matrix()
    table2Same = table2Same[1:] #remove username from row to just look at buddies
    table2Same = list(table2Same) #convert to list to add commas
    table2Same = [x for x in table2Same if x is not None] #remove "none" vlaues to compare
    intersection = [x for x in tp3Same if x in table2Same] #find similar values
    #add the full values of tp3 to a close array, keeping these values for later
    close.append(tp3Same)
    same.append(intersection)
    
#convert to dataframe
same = pandas.DataFrame(same)

#add a username column back in that was removed earlier to examine buddies
names = []
for i in range(256):
    names.append("u" + str(4001+ i))
same["user"] = [num for num in names]

#Move user column to the front
cols = same.columns.tolist()
cols = cols[-1:] + cols[:-1]
same = same[cols]

#name columns
same.columns = ["user","buddy1","buddy2","buddy3","buddy4","buddy5","buddy6"]
same['number'] = same.count(axis=1)-1

#Create Close Data Frame showing closeness of buddies
close = pandas.DataFrame(close)
close.columns = ["buddy1","buddy2","buddy3","buddy4","buddy5","buddy6","Close1","Close2","Close3","Close4","Close5","Close6"]


#Add closeness to the same data frame
same['Closeness1'] = close.Close1
same['Closeness2'] = close.Close2
same['Closeness3'] = close.Close3
same['Closeness4'] = close.Close4
same['Closeness5'] = close.Close5
same['Closeness6'] = close.Close6
same = same[["user","buddy1", "Closeness1", "buddy2","Closeness2","buddy3","Closeness3","buddy4","Closeness4", "buddy5","Closeness5","buddy6", "Closeness6"]]


#same.to_csv("sameClose.csv")
#same

#follow the same steps as above, but to find the difference in table2 and timepoint3
different = []


tp3Diff = tp3.drop('Close1', 1)
tp3Diff = tp3Diff.drop('Close2', 1)
tp3Diff = tp3Diff.drop('Close3', 1)
tp3Diff = tp3Diff.drop('Close4', 1)
tp3Diff = tp3Diff.drop('Close5', 1)
tp3Diff = tp3Diff.drop('Close6', 1)


for index, rows in table2.iterrows():
    tp3Same = tp3Diff.loc[tp3.username == rows.user].as_matrix()
    tp3Same = tp3Same[:,1:]
    tp3Same = tp3Same.ravel()
    tp3Same = list(tp3Same)
    table2Same = rows.as_matrix()
    table2Same = table2Same[1:]
    table2Same = list(table2Same)
    table2Same = [x for x in table2Same if x is not None]
    intersection = [x for x in tp3Same if x not in table2Same]
    different.append(intersection)

different = pandas.DataFrame(different)

names2 = []
for i in range(256):
    names2.append("u" + str(4001+ i))

different["user"] = [num for num in names2]

cols2 = different.columns.tolist()
cols2 = cols2[-1:] + cols2[:-1]
different = different[cols2]

different.columns = ["user","buddy1","buddy2","buddy3","buddy4","buddy5","buddy6"]

different['number'] = different.count(axis=1)-1
#different.to_csv("different.csv")
#different