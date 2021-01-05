# https://adventofcode.com/2015/day/7
import re
import functools
import logging
from pathlib import Path

path = Path(__file__).parent / "input/inputDay7.txt"
logPath = Path(__file__).parent / "logs/logDay7.txt"
f = open(path)

signals={}
while True:
    line=f.readline()
    if not line:
        break
    instruction, key = line.split(" -> ")
    signals[key.strip()]=instruction
f.close
logging.basicConfig(filename=logPath, level=logging.DEBUG)

@functools.lru_cache()
def value(wire):
    logging.debug(wire)
    if wire.isnumeric()==True:
        return int(wire)
    instruction=signals[wire]
    instruction=instruction.split(" ")
    if "NOT" in instruction:
        return ~value(instruction[1]) & 0xffff
    elif "OR" in instruction:
        return value(instruction[0]) | value(instruction[2])
    elif "AND" in instruction:
        return value(instruction[0]) & value(instruction[2])
    elif "RSHIFT" in instruction:
        return value(instruction[0]) >> value(instruction[2])
    elif "LSHIFT" in instruction:
        return value(instruction[0]) << value(instruction[2])
    elif instruction[0].isnumeric()==False:
        return value(instruction[0])  
    else:
        return int(instruction[0])

a=value("a")
print("Part 1 Answer: " + str(a))

signals["b"]=str(a)
value.cache_clear()
print("Part 2 Answer: " + str(value("a")))


