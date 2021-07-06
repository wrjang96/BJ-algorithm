from itertools import combinations
N, M = map(int, input().split())
if M == 1:
    for _ in range(1, N + 1):
        print(_)
else:
    arr = [_ for _ in range(1, N + 1)]
    answer_list = list(combinations(arr, M))
    for i in answer_list:
        print(*i)
