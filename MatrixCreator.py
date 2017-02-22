import csv

def comp(array1,array2):
    addiction = 1
    gender = 1
    education = 1
    salary = 1
    
    #Checking ages 
    age = (array1[0] - array2[0])
    if (age < 5 and age > -5):
        age = 1
    else:
        age = 0
    #Checking if matching genders
    if (array1[1] != array2[1]):
        gender = 0
    elif(array1[2] != array2[2]):
        gender = 0

    #Checking if matching primary addiction
    for y in range(4, 16):
        if (array1[y] != array2[y]):
            addiction = 0


    #Checking education
    for y in range(16, 22):
        if (array1[y] != array2[y]):
            education = 0

    #Checking for salary
    for y in range(22, 28):
        if (array1[y] != array2[y]):
            salary = 0

            
    return (age + gender + addiction + education + salary)/5

data_file = open("HomophilyDataParsed.csv",'r')
matrix_file = open("matrix.csv",'w')

writer = csv.writer(matrix_file)
reader = csv.reader(data_file)
data = [[0 for x in range(257)] for x in range(257)]
data[0][0] = 'id'
x = 0

lines = [[0 for x in range(28)] for x in range(256)]
next(reader)
for row in reader:
    lines[x][0] = int(row[1])
    
    lines[x][1] = int(row[2])
    lines[x][2] = int(row[3])
    lines[x][3] = int(row[4])
    
    lines[x][4] = int(row[5])
    lines[x][5] = int(row[6])
    lines[x][6] = int(row[7])
    lines[x][7] = int(row[8])
    lines[x][8] = int(row[9])
    lines[x][9] = int(row[10])
    lines[x][10] = int(row[11])
    lines[x][11] = int(row[12])
    lines[x][12] = int(row[13])
    lines[x][13] = int(row[14])
    lines[x][14] = int(row[15])
    lines[x][15] = int(row[16])

    lines[x][16] = int(row[17])
    lines[x][17] = int(row[18])
    lines[x][18] = int(row[19])
    lines[x][19] = int(row[20])
    lines[x][20] = int(row[21])
    lines[x][21] = int(row[22])

    lines[x][22] = int(row[23])
    lines[x][23] = int(row[24])
    lines[x][24] = int(row[25])
    lines[x][25] = int(row[26])
    lines[x][26] = int(row[27])
    lines[x][27] = int(row[28])

    data[x+1][0] = int(row[0])
    data[0][x+1] = int(row[0])
    x += 1
data_file.close()

for y in range(256):
    for z in range(y + 1):
        data[z+1][y+1] = round(comp(lines[y], lines[z]), 2)
        data[y+1][z+1] = data[z+1][y+1]

writer.writerows(data)



matrix_file.close()

