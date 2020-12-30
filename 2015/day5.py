import os
start = "/aocPython/2015/input/inputDay5.txt"
path=os.path.realpath(start)
# defaults to read
vowels = "AaEeIiOoUu"
f = open(path)

def Check_Vow(string, vowels): 
    final = [each for each in string if each in vowels] 
    return final

while True:
    line=f.readline()
    if not line:
        break
    if Check_Vow(line,vowels)>=3:
        print("keep checking")


f.close()