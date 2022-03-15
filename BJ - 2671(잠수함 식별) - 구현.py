# (100~1~|01)~

s = input()
flag = True

while len(s)>0:
    if s.startswith('100'):
        s = s[3:]
        while len(s)>0 and s.startswith('0'):
            s = s[1:]
        if len(s) == 0:
            flag = False
            break
        s = s[1:]
        while len(s) > 0 and s.startswith('1'):
            if len(s) >= 3 and s.startswith('100'):
                break
            else:
                s = s[1:]
    elif s.startswith('01'):
        s = s[2:]
    else:
        flag = False
        break

if flag:
    print("SUBMARINE")
else:
    print("NOISE")