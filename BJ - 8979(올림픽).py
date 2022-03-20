import sys
rank = []
input = sys.stdin.readline
N, K = map(int, input().split())
for i in range(N):
    tmp = list(map(int, input().split()))
    rank.append([tmp[1], tmp[2], tmp[3], tmp[0]])

rank.sort(reverse=True)
record = [rank[0][0], rank[0][1], rank[0][2]]
ans,cnt = 1,0
for a,b,c, num in rank:
    cnt+=1
    if [a,b,c] != record:
        ans = cnt
        record = [a,b,c]
    if num == K:
        print(ans)
        break