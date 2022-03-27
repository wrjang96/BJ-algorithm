N, K = map(int, input().split())
wires = []
for i in range(N):
    wires.append(int(input()))
start = 1
end = max(wires)
ans = 0
while start <= end:
    mid = (start + end) //2
    # print(start, end, mid)
    cnt = 0
    for wire in wires:
        cnt += (wire //mid)
    if cnt >= K:
        ans = max(ans, mid)
        start = mid + 1
    else:
        end = mid - 1

print(ans)

