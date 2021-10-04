import sys
input = sys.stdin.readline
V, E = map(int, input().split())
root = [i for i in range(V + 1)]
tree = []
while E:
    start, end, weight = map(int, input().split())
    tree.append([start, end, weight])
    E -= 1

tree.sort(key = lambda x : x[2])
def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

answer = 0
for s,e,w in tree:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            root[sRoot] = eRoot
        else:
            root[eRoot] = sRoot
        answer += w

print(answer)