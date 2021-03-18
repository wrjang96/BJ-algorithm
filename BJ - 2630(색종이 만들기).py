paper = [0]*2
def divide(n,r,c):
    if n == 1:
        if graph[r][c] == 0:
            paper[0] +=1
        else:
            paper[1] += 1
        return
    flag = True
    for i in range(r,r + n,1):
        for j in range(c,c + n,1):
            if graph[r][c] != graph[i][j]:
                flag = False

    if flag == True:
        if graph[i][j] == 0:
            paper[0] +=1
        else:
            paper[1] += 1
    else:
        new_n = n//2
        divide(new_n,r,c)
        divide(new_n, r + new_n, c)
        divide(new_n, r, c+ new_n)
        divide(new_n, r+ new_n, c+ new_n)




N = int(input())
graph = [[0]*N]*N

for i in range(N):
    graph[i] = list(map(int, input().split()))
divide(N,0,0)

print(paper[0])
print(paper[1])