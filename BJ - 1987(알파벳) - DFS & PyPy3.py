import sys
input = sys.stdin.readline

def dfs(tmpx, tmpy, tmpcnt, visited):
    global answer
    if answer < tmpcnt:
        answer = tmpcnt
    for i in range(4):
        nx = tmpx + dx[i]
        ny = tmpy + dy[i]
        if 0<= nx < R and 0 <= ny <C and visited[input_map[nx][ny]] == 0 : # and visited_map[nx][ny] == 0
            visited[input_map[nx][ny]] = 1
            dfs(nx,ny,tmpcnt + 1,visited)
            visited[input_map[nx][ny]] = 0

if __name__ == "__main__":
    R, C = map(int, input().split())
    input_map = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(R)]
    visited = [0] * 26
    dx = [1, - 1, 0, 0]
    dy = [0, 0, 1, - 1]
    visited[input_map[0][0]] = 1
    answer = 1
    dfs(0,0,answer, visited)
    print(answer)
