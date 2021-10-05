from itertools import combinations
import math
N = int(input())
stars = []
root = [i for i in range(N)]
for i in range(N):
    x, y = map(float, input().split())
    stars.append([x,y,i])

distances = list(combinations(stars,2))
stellar = []
for distance in distances:
    stellar.append([distance[0][2],distance[1][2],round(math.sqrt(math.pow(distance[0][0] - distance[1][0],2) + math.pow(distance[0][1] - distance[1][1],2)),2)])
stellar.sort(key = lambda x : x[2])

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]
answer = 0
for s, e, w in stellar:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            root[sRoot] = eRoot
        else:
            root[eRoot] = sRoot
        answer += w

print(answer)