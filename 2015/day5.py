# https://adventofcode.com/2015/day/5
import os
start = "/adventOfCodePython/2015/input/inputDay5.txt"
path=os.path.realpath(start)
# defaults to read
vowels = "AaEeIiOoUu"
pairs=["ab","cd","pq","xy"]
f = open(path)

def Check_Vow(string, vowels): 
    final = [each for each in string if each in vowels] 
    return final

niceCount=0
while True:
    line=f.readline()
    if not line:
        break
    # check if 3 or more vowels
    if len(Check_Vow(line,vowels))>=3:
        #check if there's a double letter e.g. 'dd'
        prevLetter=line[0]
        doubleMatch=False
        for letter in range(len(line)-1):
            thisLetter=line[letter+1]
            if prevLetter==thisLetter:
                doubleMatch=True
            prevLetter=thisLetter
            #check for letter pairs
        prevLetter=line[0]
        pairMatch=False        
        if doubleMatch==True:
            for letter in range(len(line)-1):
                thisLetter=line[letter+1]
                if prevLetter+thisLetter in pairs:
                    pairMatch=True
                prevLetter=thisLetter
            if pairMatch!=True:
                niceCount+=1        

f.close()

print("Part 1 Answer: "+ str(niceCount))