L = int(input())
answer_str = str(input())
answer = 0

for i in range(L):
    answer += (ord(answer_str[i])-96) * (31 ** i)
print(answer % 1234567891)