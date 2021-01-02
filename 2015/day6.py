# https://adventofcode.com/2015/day/6
import os
import re
from pathlib import Path

path = Path(__file__).parent / "input/inputDay6.txt"

#build grid
grid={}
grid2={}
for x in range(1000):
    for y in range(1000):
        coord=str(x)+","+str(y)
        grid[coord]=False
        grid2[coord]=0

f = open(path)

while True:
    line=f.readline()
    if not line:
        break
    action = re.search('(toggle|turn off|turn on) ([0-9]{1,3}),([0-9]{1,3}) through ([0-9]{1,3}),([0-9]{1,3})',line)
    xstart=int(action.group(2))
    ystart=int(action.group(3))
    xend=int(action.group(4))
    yend=int(action.group(5))

    for x in range(xstart,xend+1):
        for y in range(ystart,yend+1):
            if action.group(1)=="turn on":
                grid[str(x)+","+str(y)]=True
                grid2[str(x)+","+str(y)]+=1
            if action.group(1)=="turn off":
                grid[str(x)+","+str(y)]=False
                grid2[str(x)+","+str(y)]-=1
                if grid2[str(x)+","+str(y)]<0:
                    grid2[str(x)+","+str(y)]=0
            if action.group(1)=="toggle":
                if grid[str(x)+","+str(y)]==True:
                    grid[str(x)+","+str(y)]=False
                elif grid[str(x)+","+str(y)]==False:
                    grid[str(x)+","+str(y)]=True
                grid2[str(x)+","+str(y)]+=2
f.close()

litCount=0
for x in grid:
    if grid[x]==True:
        litCount+=1
brightness=0
for x in grid2:
    if grid2[x]>0:
        brightness+=grid2[x]

print("Part 1 Answer: "+ str(litCount))
print("Part 2 Answer: "+ str(brightness))