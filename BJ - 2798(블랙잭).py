from itertools import combinations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0

for cards in combinations(numbers, 3):
    if answer < sum(cards) and sum(cards) <= M:
        answer = sum(cards)
print(answer)