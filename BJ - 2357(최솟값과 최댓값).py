from math import *
import sys
input = sys.stdin.readline

def maximum(left,right,node_left,node_right,node_num):
    if left > node_right or right < node_left:
        return 0
    if left <= node_left and right >= node_right:
        return maxarr[node_num]
    mid = (node_left + node_right) //2
    return max(maximum(left,right,node_left,mid,node_num * 2),maximum(left,right,mid + 1, node_right, node_num *2 + 1))

def minimum(left,right,node_left,node_right,node_num):
    if left > node_right or right < node_left:
        return 1000000000
    if left <= node_left and right >= node_right:
        return minarr[node_num]
    mid = (node_left + node_right) //2
    return min(minimum(left,right,node_left,mid,node_num * 2),minimum(left,right,mid + 1, node_right, node_num *2 + 1))

def init(x):
    for i in range(x-1,0,-1):
        minarr[i] = min(minarr[i*2], minarr[i*2 + 1])
        maxarr[i] = max(maxarr[i * 2], maxarr[i * 2 + 1])

N, M = map(int, input().split())
size = 2 ** ceil(log(N,2))
size_max = size * 2
minarr = [1000000000] * size_max
maxarr = [0] * size_max
for i in range(N):
    temp = int(input())
    minarr[size + i] = temp
    maxarr[size + i] = temp
init(size)
for i in range(M):
    sx, ex = map(int, input().split())
    print(minimum(sx-1,ex-1,0,size-1,1), end = " ")
    print(maximum(sx-1,ex-1,0,size-1,1))