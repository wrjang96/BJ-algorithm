from sys import stdin
N,M = map(int,stdin.readline().split())
graph = list(map(int,stdin.readline().split()))
plus = []
minus = []
count = []
# A. 플러스 마이너스 나눠서 리스트에 넣음
for i in graph:
    if i>0:
        plus.append(i)
    else:
        minus.append(abs(i)) # 마이너스는 절댓값으로
plus.sort(reverse=True)
minus.sort(reverse=True)

# B. 한번가는 최장길이 구하기
if len(minus)==0 or len(plus)==0:# 1. 둘 중 하나가 리스트 원소 없을 경우 에러 방지
    if len(minus)==0: # 플러스 최장거리 빼기
        for i in range(M):
            if len(plus) == 0:
                break
            if i == 0:
                count.append(plus[i])
                plus.pop(0)
            else:
                plus.pop(0)
    elif len(plus)==0:# 마이너스 최장거리 빼기
        for i in range(M):
            if len(minus) == 0:
                break
            if i == 0:
                count.append(minus[i])
                minus.pop(0)
            else:
                minus.pop(0)

else: # 2. 둘다 리스트 있을 경우
    if (plus[0] > minus[0]): # 2 -1)플러스의 길이가 더 길 경우 플러스의 값 한번 더하기
        for i in range(M):
            if len(plus) == 0:
                break
            if i == 0:
                count.append(plus[i])
                plus.pop(0)
            else:
                plus.pop(0)
    else: # 2 -2)마이너스의 길이가 더 길 경우 마이너스의 값 한번 더하기
        for i in range(M):
            if len(minus) == 0:
                break
            if i == 0:
                count.append(minus[i])
                minus.pop(0)
            else:
                minus.pop(0)

# C. 그 외에 나머지 값은 *2 해서 count 배열에 더함
while(len(minus)>0): # 1. 마이너스 값 *2
    for i in range(M):
        if len(minus)==0:
            break
        if i==0:
            count.append(minus[i] *2)
            minus.pop(0)
        else:
            minus.pop(0)
while(len(plus)>0):# 2. 플러스 값 *2
    for i in range(M):
        if len(plus)==0:
            break
        if i==0:
            count.append(plus[i] *2)
            plus.pop(0)
        else:
            plus.pop(0)
# D. 최종 값의 합 출력
print(sum(count))
