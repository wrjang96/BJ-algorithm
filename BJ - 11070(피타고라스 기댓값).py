from sys import stdin
testcase = int(stdin.readline())
result = []
while testcase:
    N, M = map(int, stdin.readline().split())
    graph = [[0, 0] for i in range(N + 1)]
    while M:
        data = list(map(int, stdin.readline().split()))
        graph[data[0]] = [graph[data[0]][0] +data[2],graph[data[0]][1]+ data[3]]
        graph[data[1]] = [graph[data[1]][0] +data[3],graph[data[1]][1]+ data[2]]
        M-=1
    #print(graph)
    for i in range(1,N+1,1):
        if graph[i][0]==0 and graph[i][1] ==0:
            result.append(0)
        else:
            result.append((graph[i][0]**2)*1000//(graph[i][0]**2+graph[i][1]**2))
    #print(result)
    result.sort()
    print(result[-1])
    print(result[0])
    result.clear()
    testcase -= 1