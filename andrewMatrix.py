# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 10:32:25 2016

@author: Andrew
"""

import pandas as pd
import math
import csv

myfile = pd.read_csv("HomophilyDataParsed.csv")
matrix_file = open("andrewMatrix1.csv",'wb')

writer = csv.writer(matrix_file)

def main():
    euclidArr = []
    finalResult = []
    for x in range(len(myfile)):
        euclidArr = []
        count = 0
        for y in range(len(myfile)):
            if(count == 0):
                print("X:",x)
                count = count + 1
            fRow = myfile.iloc[[x]]
            sRow = myfile.iloc[[y]]
            euclidArr.append(euclid(fRow, sRow))
        finalResult.append(euclidArr)
    writer.writerows(finalResult)

def sd(arr, mean):
    val = 0    
    length = len(arr)
    for x in range(length):
        temp = float(arr[x]) - mean
        squared = temp**2
        val = val + squared
    variance = val/length
    standardDeviation = math.sqrt(variance)
    return standardDeviation

def calcMean(arr):
    val = 0
    length = len(arr)
    for x in range(length):
        val = val + float(arr[x])
    m = val / length
    return m

def euclid(row1, row2):
    age1 = row1.iloc[0,1]
    age2 = row2.iloc[0,1]
    if(age1 - age2 < 5):
        val = 0
    else:
        val = 1
    for x in range(2,len(row1.columns)):
        subVal = float(row1.iloc[0,x]) - float(row2.iloc[0,x])
        squareIt = subVal**2
        val = val + squareIt
    retVal = math.sqrt(val)
    return retVal
    
main()            
matrix_file.close()