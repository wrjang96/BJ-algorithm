import bisect

T = int(input())
N = int(input())
A = list(map(int, input().split()))
A_sum = []
for i in range(N):
    for j in range(i, N):
        A_sum.append(sum(A[i:j+1]))

M = int(input())
B = list(map(int, input().split()))
B_sum = []
for i in range(M):
    for j in range(i, M):
        B_sum.append(sum(B[i:j+1]))
B_sum.sort()

ans_cnt = 0
for tmp in A_sum:
    ans_cnt += bisect.bisect_right(B_sum, T - tmp) - bisect.bisect_left(B_sum, T-tmp)
print(ans_cnt)