import re
temp = input()
ans = re.compile('(pi|ka|chu)+')
if ans.fullmatch(temp):
    print('YES')
else:
    print('NO')