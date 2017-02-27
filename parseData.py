import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#ax = df[['V1','V2']].plot(kind='bar', title ="V comp", figsize=(15, 10), legend=True, fontsize=12)
#ax.set_xlabel("Hour", fontsize=12)
#ax.set_ylabel("V", fontsize=12)
#plt.show()
df =pd.read_csv("TESModule.csv")
#print(data)
#data.plot.hist()


ax = df[['number_of_people']].plot(kind='bar', title ="TES Modules", figsize=(15, 10), legend=True, fontsize=12)
ax.set_xlabel("Module Number", fontsize=12)
ax.set_ylabel("Number Taken", fontsize=12)
plt.show()