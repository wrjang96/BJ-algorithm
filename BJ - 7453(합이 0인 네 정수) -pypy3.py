import sys
input = sys.stdin.readline

N = int(input())
A = []
B = []
C = []
D = []

while N:
    a, b, c ,d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    N -= 1
    
sum_of_A_and_B = {}

for temp_a in A:
    for temp_b in B:
        temp_sum = temp_a + temp_b
        if temp_sum not in sum_of_A_and_B.keys():
            sum_of_A_and_B[temp_sum] = 1
        else:
            sum_of_A_and_B[temp_sum] += 1

ans = 0
for temp_c in C:
    for temp_d in D:
        temp_sum = (temp_c + temp_d) * - 1
        if temp_sum in sum_of_A_and_B.keys():
            ans += sum_of_A_and_B[temp_sum]
print(ans)