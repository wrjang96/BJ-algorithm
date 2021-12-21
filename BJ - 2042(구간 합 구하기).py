import sys
from math import *

def modify(i, val, arr):
    i += size - 1
    arr[i] = val
    while i > 1:
        i //= 2
        arr[i] = arr[i * 2] + arr[i * 2 + 1]

def minimum(left,right,node_left,node_right,node_num):
    if left > node_right or right < node_left:
        return 0
    if left <= node_left and right >= node_right:
        return sum_arr[node_num]
    mid = (node_left + node_right) //2
    return minimum(left,right,node_left,mid,node_num * 2) + minimum(left,right,mid + 1, node_right, node_num *2 + 1)

def init(x):
    for i in range(x-1,0,-1):
        sum_arr[i] = sum_arr[i*2] + sum_arr[i*2 + 1]


input = sys.stdin.readline
N, M, K = map(int, input().split())
size = 2 ** ceil(log(N,2))
size_max = size * 2
sum_arr = [0] * size_max
for i in range(N):
    sum_arr[size + i] =  int(input())

init(size)

for i in range(M + K):
    a, sx, ex = map(int, input().split())
    if a == 2:
        print(minimum(sx-1,ex-1,0,size-1,1))
    elif a ==1:
        modify(sx,ex, sum_arr)