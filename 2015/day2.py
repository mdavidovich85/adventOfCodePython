import os
start = "/adventOfCodePython/2015/input/inputDay2.txt"
path=os.path.realpath(start)
# defaults to read

def sqFt(l,w,h):
    return (2*l*w) + (2*w*h) + (2*h*l)

def extra(l,w,h):
    side1=l*w
    side2=w*h
    side3=l*h
    list = [side1,side2,side3]
    list.sort()
    return list[0]

def ribbon(l,w,h):
    per1=l+l+w+w
    per2=l+l+h+h
    per3=w+w+h+h
    list=[per1,per2,per3]
    list.sort()
    return (list[0] + l*w*h)

f = open(path)
totSqFt=0
totRibb=0
while True:
    line=f.readline()
    if not line:
        break
    else:
        operands=line.split("x")
        leng=int(operands[0])
        wdt=int(operands[1])
        hgt=int(operands[2])
        totSqFt = totSqFt + sqFt(leng,wdt,hgt) + extra(leng,wdt,hgt)
        totRibb= totRibb + ribbon(leng,wdt,hgt)

f.close()

print("Total squre feet needed: " + str(totSqFt))
print("Total ribbon needed: " + str(totRibb))
