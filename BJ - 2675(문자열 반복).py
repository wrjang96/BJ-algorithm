testcase = int(input())

while testcase:
    newstring = ''
    num, string = map(str,input().split())
    #print(num,string)
    for i in range(0,len(string),1):
        newstring +=string[i]*int(num)
    print(newstring)
    testcase -=1
