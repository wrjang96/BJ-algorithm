N = int(input())    # 센서 개수
K = int(input())    # 집중국 개수
location = list(map(int, input().split()))  # 센서 좌표
gap =[]
location.sort()
for i in range(0,N-1,1):
    gap.append(abs(location[i] - location[i+1]))
gap.sort(reverse = True)
answer =0
for i in range(0,K-1,1):
    if(len(gap)>0):
        del gap[0]
answer = sum(gap)
print(answer)
