import sys
input = sys.stdin.readline

database ={}
times = input().split()
cnt = 0
for time in times:
    hour, min = time.split(":")
    if cnt == 0:
        S = int(hour) * 60 + int(min)
    if cnt == 1:
        E = int(hour) * 60 + int(min)
    if cnt == 2:
        Q = int(hour) * 60 + int(min)
    cnt += 1

while 1:
    try:
        line = input()
        time, name = line.split()
        hour, min = time.split(":")
        chat_time = int(hour) * 60 + int(min)
        if chat_time <= S:
            database[name] = 1
        elif E <= chat_time and chat_time <= Q:
            database[name] = 0
    except:
        break

ans = 0
for key, value in database.items():
    if value == 0:
        ans +=1
print(ans)

