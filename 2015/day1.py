from pathlib import Path

path = Path(__file__).parent / "input/inputDay1.txt"
f = open(path)
floor=0
position=0
checkFloor=1
while 1:
    char=f.read(1)
    position=position+1
    if char == "(":
        floor=floor+1
    elif char == ")":
        floor=floor-1
    elif not char:
        break

    if floor == -1 and checkFloor==1:
        basementPos = position
        checkFloor = 0

f.close()

print("Floor: "+ str(floor))
print("Basement position: "+ str(basementPos))
