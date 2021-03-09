from sys import stdin

N = int(stdin.readline())
scale = list(map(int,stdin.readline().split()))
scale.sort()
target = 1
for i in range(N):
    if target < scale[i]:
        break
    target += scale[i]

print(target)
