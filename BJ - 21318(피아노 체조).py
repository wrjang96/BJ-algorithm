import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
sum_arr = [0] * N
for i in range(1,len(arr)):
    if arr[i] < arr[i-1]:
        sum_arr[i] +=1
    sum_arr[i] += sum_arr[i-1]

M = int(input())
for i in range(M):
    start,end = map(int,input().split())
    print(sum_arr[end-1] - sum_arr[start-1])
