N, M = map(int,input().split())
up = 1
down = 1
start = 1
end = N
for i in range(M):
    up *= end
    down *= start
    start += 1
    end -= 1

print(up//down)