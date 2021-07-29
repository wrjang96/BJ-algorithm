from itertools import combinations_with_replacement

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr) #순서대로 나오게 정렬 먼저

for numbers in list(combinations_with_replacement(arr, M)):
    for num in numbers:
        print(num, end=' ')
    print()