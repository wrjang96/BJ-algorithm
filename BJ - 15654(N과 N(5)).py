from itertools import permutations
N, M = map(int,input().split())
input_arr = list(map(int,input().split()))
input_arr.sort()
answer = list(permutations(input_arr, M))
for i in range(len(answer)):
    print(*answer[i])
