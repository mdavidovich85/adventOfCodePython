import os
start = "/aocPython/2015/input/inputDay3.txt"
path=os.path.realpath(start)
# defaults to read
f = open(path)
position=0
coords = [0,0]
coord_list= ["0,0"]
santa_coords = [0,0]
robot_coords = [0,0]
santa_list= ["0,0"]
robo_list= ["0,0"]
while 1:
    char=f.read(1)
    position+=1
    if char==">":
        coords[0]+=1
        if position%2==0:
            #even number robot
            robot_coords[0]+=1
        else:
            #odd number santa
            santa_coords[0]+=1
    if char=="<":
        coords[0]-=1
        if position%2==0:
            #even number robot
            robot_coords[0]-=1
        else:
            #odd number santa
            santa_coords[0]-=1
    if char=="^":
        coords[1]+=1
        if position%2==0:
            #even number robot
            robot_coords[1]+=1
        else:
            #odd number santa
            santa_coords[1]+=1
    if char=="v":
        coords[1]-=1
        if position%2==0:
            #even number robot
            robot_coords[1]-=1
        else:
            #odd number santa
            santa_coords[1]-=1
    if not char:
        break
    coord_list.append(str(coords[0])+","+str(coords[1]))
    if position%2==0:
        #even number robot
        robo_list.append(str(robot_coords[0])+","+str(robot_coords[1]))
    else:
        #odd number santa
        santa_list.append(str(santa_coords[0])+","+str(santa_coords[1]))

f.close()

print("Part 1 Answer: "+ str(len(set(coord_list))))

santa_list=list(set(santa_list))
robo_list=list(set(robo_list))
combined_list=[]
for element in santa_list:
    combined_list.append(element)

for element in robo_list:
    combined_list.append(element)

print("Part 2 Answer: "+ str(len(set(combined_list))))