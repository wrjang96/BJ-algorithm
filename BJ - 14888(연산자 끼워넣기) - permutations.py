from itertools import permutations
N = int(input())
tmp = []
A = list(map(int, input().split()))
cal = list(map(int, input().split()))
for i in range(4):
    if i == 0:
        for j in range(cal[i]):
            tmp.append("+")
    if i == 1:
        for j in range(cal[i]):
            tmp.append("-")
    if i == 2:
        for j in range(cal[i]):
            tmp.append("*")
    if i == 3:
        for j in range(cal[i]):
            tmp.append("//")
tmp2 = permutations(tmp, sum(cal))
tmp2 = list(set(tmp2))
min = 10 ** 22
max = 10 ** 22 * -1
ans_arr= []
for i in tmp2:
    ans = A[0]
    cnt = 1
    for j in i:
        if j == "+":
            ans += A[cnt]
        elif j == "-":
            ans -= A[cnt]
        elif j == "*":
            ans *= A[cnt]
        else:
            # ans = int(ans/A[cnt])
            if ans < 0: # 조건 잘못 읽음
                ans *= -1
                ans = ans // A[cnt]
                ans *= -1
            else:
                ans = ans // A[cnt]
        cnt +=1
    if min > ans:
        min = ans
    if max < ans:
        max = ans
print(max)
print(min)