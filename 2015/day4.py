import hashlib

input1="ckczppom"
number=1
while 1:
    input2=str(number)
    str2hash=input1+input2
    result=hashlib.md5(str2hash.encode())
    if result.hexdigest()[0:5]=="00000":
        break
    else:
        number+=1

print("Answer: "+str(input1)+str(input2))

input1="ckczppom"
number=1
while 1:
    input2=str(number)
    str2hash=input1+input2
    result=hashlib.md5(str2hash.encode())
    if result.hexdigest()[0:6]=="000000":
        break
    else:
        number+=1

print("Answer: "+str(input1)+str(input2))