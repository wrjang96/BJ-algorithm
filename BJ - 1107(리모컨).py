from sys import stdin
end = int(stdin.readline())
start = 100
N = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
panel = [0]*10
for i in range(len(arr)):
    temp = arr.pop()
    panel[temp] = 1

total =0
index =1
flag = abs(end - start)
answer =0
for i in range(1000001):
    i = str(i)
    flag1 = True
    for j in range(len(i)):
        tmp = int(i[j])
        if panel[tmp] ==1:
            flag1 = False
            break
    if flag1 == True:
        flag = min(flag, len(i) + abs((int(i) - end)))

print(flag)
