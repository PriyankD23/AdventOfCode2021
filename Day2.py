import pandas as pd 
import numpy as np 
import os

# set working directory as the current file dir
os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv('Day2Input.csv')

#part1
x = df.groupby('direction')['value'].sum()

horiz_v = x[1]
depth_v = x[0]-x[2]
part1 = horiz_v*depth_v

print(f'Part21 ans:{part1}')

#part2

horiz = 0
depth = 0
aim=0


for i in range(len(df)):
    if(i==0 and df['direction'].iloc[i]=='forward'):
        aim=0
        horiz=horiz+df['value'].iloc[i]
    elif(i!=0 and df['direction'].iloc[i]=='forward'):
        horiz=horiz+df['value'].iloc[i]
        depth =depth+aim*df['value'].iloc[i]
    elif(i!=0 and df['direction'].iloc[i]=='down'):
        aim = aim+df['value'].iloc[i]
    else:
        aim = aim-df['value'].iloc[i]

part2 = horiz*depth

print(f'Part2 ans:{part2}')




        