# (100~1~|01)~
import re

s = input()
flag = re.compile('(100+1+|01)+')
m = flag.fullmatch(s)
if m:
    print("SUBMARINE")
else:
    print("NOISE")