from sys import stdin
N = int(stdin.readline())
arr =[]
priority =0
while(N):
    age, name= map(str,stdin.readline().split())
    age = int(age)
    priority +=1
    arr.append([age,priority, name])
    N-=1
arr.sort()

for j in range(len(arr)):
    print(arr[j][0], arr[j][2])