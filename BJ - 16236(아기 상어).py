import sys

q = []
N = int(sys.stdin.readline().strip())
visited = [[False] * N for _ in range(N)]
space = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
for i in range(N):
    flag = False
    for j in range(N):
        if space[i][j] == 9:
            q = [[i, j]]
            space[i][j] = 0
            visited[i][j] = True
            flag = True
            break
    if flag:
        break

def level_up():
    global shark_size, shark_eat
    if shark_eat == 0:
        shark_size += 1
        shark_eat = shark_size
    return


# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
distance = 0
result = 0
shark_size, shark_eat = 2, 2
while q:
    distance += 1
    eaten = []
    for _ in range(len(q)):
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # if 0 <= nr < N and 0 <= nc < N and space[nr][nc] <= shark_size and not visited[nr][nc]:
            #     if 0 < space[nr][nc] < shark_size:
            #         eaten.append([nr, nc])
            #         visited[nr][nc] = True
            #     else:
            #         visited[nr][nc] = True
            #         q.append([nr, nc])

            if not(0 <= nr < N) or not(0 <= nc < N): continue
            #if nr < 0 or nr>=N or nc < 0 or nc>=N: continue
            if visited[nr][nc] == True: continue
            print(nr, nc)
            print('fish',space[nr][nc])
            print('size',shark_size)
            if space[nr][nc] > shark_size: continue
            print('z')
            if space[nr][nc] == shark_size:
                print(nr, nc)
                print('x')
                visited[nr][nc] = True
                q.append([nr, nc])
            if 0 <= space[nr][nc] < shark_size:
                print('y')
                visited[nr][nc] = True
                eaten.append([nr, nc])

    if eaten:
        er, ec = N - 1, N - 1
        for e in eaten:
            if e[0] < er:
                er, ec = e[0], e[1]
            elif e[0] == er:
                if e[1] < ec:
                    ec = e[1]

        shark_eat -= 1
        level_up()
        q = [[er, ec]]
        result += distance
        distance = 0
        space[er][ec] = 0
        visited = [[False] * N for _ in range(N)]
        visited[er][ec] = True
print(result)
#
# import sys
# input = sys.stdin.readline
# N = int(input())
# graph = [[0] * N for i in range(N)]
# fish = []
# index =[]
# shark =[]
# shark_size = 2
#
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
#
# for i in range(N):
#     graph[i] = list(map(int,input().split()))
#
# distance =[0]
# def search(graph):
#     queue = []
#     result = []
#     queue.append([shark[0][0], shark[0][1], 0])
#     visited = [[0] * N for i in range(N)]
#     while queue:
#         z,w,time = queue.pop(0)
#         if [z, w] in fish:
#             result.append([time,z,w])
#         for i in range(4):
#             nz = z + dx[i]
#             nw = w + dy[i]
#             if 0 <= nz < N and 0 <= nw < N and visited[nz][nw] == 0 and 0 <= graph[nz][nw] <= shark_size:
#                 visited[nz][nw] = 1
#                 queue.append([nz, nw, time + 1])
#     #print(result)
#     if len(result) !=0:
#         result.sort()
#         time, z, w = result.pop(0)
#         graph[z][w] = 9
#         graph[shark[0][0]][shark[0][1]] = 0
#         return time
#     else:
#         return -1
#
# cnt =0
# while(1):
#     for i in range(N):
#         for j in range(N):
#             if 1 <= graph[i][j] < shark_size:
#                 fish.append([i, j])
#             if graph[i][j] == 9:
#                 shark.append([i, j])
#     tmp = search(graph)
#
#     if tmp == -1:
#         break
#     else:
#         cnt += 1
#         if cnt == shark_size:
#             shark_size += 1
#             if shark_size >7:
#                 shark_size =7
#             cnt =0
#         distance.append(tmp)
#         fish.clear()
#         shark.clear()
#
# print(sum(distance))
