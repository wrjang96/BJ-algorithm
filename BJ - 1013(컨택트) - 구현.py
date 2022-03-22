# (100+1+ | 01)+

testcase = int(input())
for i in range(testcase):
    N = input()
    flag = True
    while len(N) > 0:
        if N.startswith("100"):
            N = N[3:]
            while len(N) > 0 and N.startswith('0'):
                N = N[1:]
            if len(N) == 0:
                flag = False
                break
            N = N[1:]
            while len(N) > 0 and N.startswith('1'):
                if len(N) >= 3 and N.startswith('100'):
                    break
                else:
                    N = N[1:]
        elif N.startswith("01"):
            N = N[2:]
        else:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")

