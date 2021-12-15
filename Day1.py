import pandas as pd 
import numpy as np 
import os

# set working directory as the current file dir
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Data = pd.read_csv('Day1Input.csv')  #getInput

def calcTag(lst):
    Tag = []
    for i in range(len(lst)):
        if(i==0):
            Tag.append("NA")
        else:
            if(lst[i]>lst[i-1]):
                Tag.append('Increasing')
            elif(lst[i]==lst[i-1]):
                Tag.append('NA')
            else:
                Tag.append('Decreasing')
    return (Tag.count('Increasing'))

#################### Part 1 ########################################

GetCount_part1 = calcTag(Data['Depth'])

print(GetCount_part1)

#################### Part 2 ########################################
#sliding window algorithm

window = 3
Arr1 = Data['Depth']
Arr2 = []

#start with the first sum value
Sum0 = sum(Arr1[:window])
Arr2.append(Sum0)

for i in range(len(Arr1)-window):
    Sum0 = Sum0-Arr1[i]+Arr1[i+window]
    Arr2.append(Sum0)

GetCount_part2 = calcTag(Arr2)
print(GetCount_part2)


# generate successive difference list
#diff = [Arr2[i + 1] - Arr2[i] for i in range(len(Arr2)-1)]
