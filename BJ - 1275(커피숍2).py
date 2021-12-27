import sys
from math import *

def modify(i, val, arr):
    i += size - 1
    arr[i] = val
    while i > 1:
        i //= 2
        arr[i] = arr[i * 2] + arr[i * 2 + 1]

def sum(left,right,node_left,node_right,node_num):
    if left > node_right or right < node_left:
        return 0
    if left <= node_left and right >= node_right:
        return sum_arr[node_num]
    mid = (node_left + node_right) //2
    return sum(left,right,node_left,mid,node_num * 2) + sum(left,right,mid + 1, node_right, node_num *2 + 1)

def init(x):
    for i in range(x-1,0,-1):
        sum_arr[i] = sum_arr[i*2] + sum_arr[i*2 + 1]


input = sys.stdin.readline
N, Q = map(int, input().split())
size = 2 ** ceil(log(N,2))
size_max = size * 2
sum_arr = [0] * size_max
temp = list(map(int, input().split()))

for i in range(N):
     sum_arr[size + i] = temp[i]

init(size)

for i in range(Q):
    a, b,c,d = map(int, input().split())
    max_val = max(a,b) - 1
    min_val = min(a,b) - 1
    print(sum(min_val,max_val,0,size-1,1))
    modify(c,d, sum_arr)