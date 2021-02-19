import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline
N = int(input())
graph = list(map(int,input().split()))
flag = [graph[0],graph[1],graph[2],graph[3],graph[4],graph[5]]

if N ==1:
    graph.sort()
    graph.pop(-1)
    print(sum(graph))
else:
    dice = []
    dice.append(min(graph[0],graph[5]))
    dice.append(min(graph[1], graph[4]))
    dice.append(min(graph[2], graph[3]))
    #print(dice)
    mini1 = sum(dice)
    mini2 = int (1e9)
    for data in range(3):
        mini2 = min(mini2, mini1 - dice[data])
    graph.sort()
    # print(mini1,mini2)
    print((4 * mini1) + (8 * N - 12) * mini2 + (5 * N * N - 16 * N + 12) * graph[0])