import sys
input = sys.stdin.readline
N = int(input())
V = int(input())
computer_network = []
root = [i for i in range(V + 1)]
while V:
    start, end, weight = map(int, input().split())
    start -= 1
    end -= 1
    computer_network.append([start, end, weight])
    V -= 1

computer_network.sort(key = lambda x : x[2])

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

answer = 0
for s, e, w in computer_network:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            root[sRoot] = eRoot
        else:
            root[eRoot] = sRoot
        answer += w
print(answer)