king_pos, stone_pos, movement = map(str, input().split())
dx = [0,0,1,-1,-1,-1,1,1]
dy = [1,-1,0,0,1,-1,1,-1]

command = ["R","L","B","T","RT","LT","RB","LB"]
chess_graph = [[0] * 8 for _ in range(8)]
kx = 8 - int(king_pos[1]); ky = ord(king_pos[0]) - 65
chess_graph[kx][ky] = 1
sx = 8 - int(stone_pos[1]); sy = ord(stone_pos[0]) - 65
chess_graph[sx][sy] = 2

for i in range(int(movement)):
    temp = str(input())
    nx = kx + dx[command.index(temp)]
    ny = ky + dy[command.index(temp)]
    if 0<= nx < 8 and 0<= ny < 8 and chess_graph[nx][ny] == 0:
        chess_graph[nx][ny] = 1
        chess_graph[kx][ky] = 0
        kx = nx;
        ky = ny
    elif 0 <= nx < 8 and 0 <= ny < 8 and chess_graph[nx][ny] == 2:
        nsx = sx + dx[command.index(temp)]
        nsy = sy + dy[command.index(temp)]
        if 0 <= nsx < 8 and 0 <= nsy < 8 and chess_graph[nsx][nsy] == 0:
            chess_graph[nsx][nsy] = 2;
            chess_graph[sx][sy] = 0;
            chess_graph[nx][ny] = 1;
            chess_graph[kx][ky] = 0;
            sx = nsx;
            sy = nsy;
            kx = nx;
            ky = ny

print(chr(65 + ky) + str(8 - kx))
print(chr(65 + sy) + str(8 - sx))
