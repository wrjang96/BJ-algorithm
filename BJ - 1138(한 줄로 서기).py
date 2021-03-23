N = int(input())
array = list(map(int, input().split()))
answer = [0]*N
for i in range(N):
    tmp = array[i]
    cnt =0
    for j in range(N):
        if cnt == tmp and answer[j] == 0:
            answer[j] += i + 1
            break
        elif answer[j] == 0:
            cnt +=1

for i in range(len(answer)):
    print(answer[i], end =' ')

