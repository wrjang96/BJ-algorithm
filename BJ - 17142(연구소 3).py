from itertools import combinations
from collections import deque
import sys
from copy import deepcopy

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[0] * N for i in range(N)]
virus = []


def check():
    global maps
    for i in range(N):
        for j in range(N):
            if map[i][j] == 0:
                return False
    return True


def search(com_arr):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    global arr, map
    queue = deque()
    visited = [[0] * N for i in range(N)]
    # queue.extend(com_arr)
    for i in range(len(com_arr)):
        queue.append((com_arr[i][0], com_arr[i][1], 0))
        visited[com_arr[i][0]][com_arr[i][1]] = 1
    ans_cnt = 0
    while queue:
        tx, ty, cnt = queue.popleft()
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < N and 0 <= ny < N and map[nx][ny] != 1 and visited[nx][ny] == 0 and map[nx][ny] !=1:
                visited[nx][ny] = 1
                if map[nx][ny] == 0:
                    map[nx][ny] = 2
                    ans_cnt = cnt + 1
                    if ans_cnt > ans:
                        break
                queue.append((nx, ny, cnt + 1))
    return ans_cnt


target_num = 0
for i in range(N):
    arr[i] = list(map(int, input().split()))
    for j in range(N):
        if arr[i][j] == 2:
            virus.append([i, j])
        elif arr[i][j] == 0:
            target_num += 1
tmp_arrs = list(combinations(virus, M))
ans = int(1e9)
for tmp_arr in tmp_arrs:
    map = deepcopy(arr)
    tmp = search(tmp_arr)
    if check():
        ans = min(ans, tmp)
if ans == int(1e9):
    print(-1)
else:
    print(ans)