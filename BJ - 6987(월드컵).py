import sys
from itertools import combinations
input = sys.stdin.readline
wsum = 0
lsum = 0
game = list(combinations(range(6), 2))
print(game)
# for i in range(4):
#     for j in range(6):
#         w, d, l = map(int, input().split())
#         wsum += w
#         lsum += l
#     if wsum == lsum and
