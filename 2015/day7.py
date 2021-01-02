# https://adventofcode.com/2015/day/7
import os
import re
from pathlib import Path

path = Path(__file__).parent / "input/inputDay7.txt"

f = open(path)

while True:
    line=f.readline()
    if not line:
        break

f.close()