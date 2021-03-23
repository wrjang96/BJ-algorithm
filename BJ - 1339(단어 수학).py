N = int(input())
alpha = [0] * 27
while N:
    word = str(input().split())
    for i in range(len(word)-4, 0, -1):
        alpha[ord(word[len(word) - i-2])- 65] += 10 ** (i-1)
    N -= 1

alpha.sort(reverse = True)
answer =0
for i in range(9, 0, -1):
    answer += alpha[9-i] * i
print(answer)