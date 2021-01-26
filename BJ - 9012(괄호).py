from sys import stdin
testcase = int(stdin.readline())

while testcase:
    flag =0
    stack =[]
    temp = stdin.readline().strip()
    for i in range(0,len(temp),1):
        if temp[i] =='(':
            stack.append('(')
        elif temp[i] == ')':
            if len(stack)==0:
                print('NO')
                flag =1
                break
            else:
                stack.pop()
        #print(stack)
    if flag ==0:
        if len(stack) ==0:
            print('YES')
        else:
            print('NO')
    testcase -=1
