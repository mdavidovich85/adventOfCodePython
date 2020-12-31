# https://adventofcode.com/2015/day/6
import os
import re
start = "/adventOfCodePython/2015/input/inputDay6.txt"
path=os.path.realpath(start)

#build grid
grid={}
for x in range(1000):
    for y in range(1000):
        coord=str(x)+","+str(y)
        grid[coord]=False

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
            if action.group(1)=="turn off":
                grid[str(x)+","+str(y)]=False
            if action.group(1)=="toggle":
                if grid[str(x)+","+str(y)]==True:
                    grid[str(x)+","+str(y)]=False
                if grid[str(x)+","+str(y)]==False:
                    grid[str(x)+","+str(y)]=True
f.close()

litCount=0
for x in grid:
    if grid[x]==True:
        litCount+=1

print("Part 1 Answer: "+ str(litCount))
