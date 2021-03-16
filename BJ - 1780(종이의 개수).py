cntgraph  = [0] *3
def divide(n, x, y):
    if n == 1:
        if graph[x][y] == - 1:
            cntgraph[0] += 1
        elif graph[x][y] == 0:
            cntgraph[1] += 1
        elif graph[x][y] == 1:
            cntgraph[2] += 1
        return

    flag = True
    for i in range(x, x + n):
        if not flag:
            break
        for j in range(y, y + n):
            if graph[i][j] != graph[x][y]:
                flag = False
                break
    if flag:
        if graph[x][y] == - 1:
            cntgraph[0] += 1
        elif graph[x][y] == 0:
            cntgraph[1] += 1
        elif graph[x][y] == 1:
            cntgraph[2] += 1
    else:
        new_N = n//3
        divide(new_N, x, y)
        divide(new_N, x+ new_N, y)
        divide(new_N, x, y+ new_N)
        divide(new_N, x+ new_N, y+ new_N)
        divide(new_N, x+ new_N*2, y)
        divide(new_N, x, y + new_N*2)
        divide(new_N, x+ new_N*2, y+ new_N*2)
        divide(new_N, x+ new_N, y+ new_N*2)
        divide(new_N, x+ new_N*2, y+ new_N)

N = int(input())
graph = [[0]*N]*N
for i in range(N):
    graph[i] = list(map(int, input().split()))

divide(N,0,0)

for i in range(3):
    print(cntgraph[i])