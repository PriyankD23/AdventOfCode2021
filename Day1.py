import pandas as pd 
import numpy as np 

Data = pd.read_csv('Day1Input.csv')  #getInput

#################### DAY 1 ########################################
Tag = []
for i in range(len(Data)):
    if(i==0):
        Tag.append("NA")
    else:
        if(Data['Depth'].iloc[i]>Data['Depth'].iloc[i-1]):
            Tag.append('Increasing')
        elif(Data['Depth'].iloc[i]==Data['Depth'].iloc[i-1]):
            Tag.append('NA')
        else:
            Tag.append('Decreasing')

Data['Tag'] = Tag

Count_Increasing = Data['Tag'].value_counts()['Increasing']
print(Count_Increasing)
