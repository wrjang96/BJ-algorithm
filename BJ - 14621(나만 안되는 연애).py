N, M = map(int, input().split())
al_arr = list(map(str, input().split()))
root = [i for i in range(N + 1)]
path = []
while M:
    start, end , weight = map(int, input().split())
    temp_start = start - 1
    temp_end = end - 1
    if al_arr[temp_start] != al_arr[temp_end]:
        path.append([start, end , weight])
    M -= 1
path.sort(key = lambda x: x[2])

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

answer = 0
count = 0
for s, e, w in path:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            root[sRoot] = eRoot
        else:
            root[eRoot] = sRoot
        answer += w
        count += 1

if count != N - 1:
    print(-1)
else:
    print(answer)
