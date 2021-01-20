from collections import deque
A, B = map(int, input().split())
ans = -1 # 바꿀 수 없는 경우
my_d = deque([(A,1)])

while my_d:
    nx, cnt = my_d.popleft()
    if nx == B:
        ans = cnt
        break
    if nx*2 <=B:
        my_d.append((nx*2,cnt+1))
    if nx*10+1 <=B:
        my_d.append((nx*10+1,cnt+1))

print(cnt)
