import sys
input = sys.stdin.readline

level = int(input())
tree = list(map(int, input().split()))
ans = [[] for i in range(level)]

def traverse(start, end, level):
    # print(ans)
    if start == end:
        ans[level].append(tree[start])
        return
    mid = (start + end)//2
    ans[level].append(tree[mid])
    traverse(start, mid -1, level + 1)
    traverse(mid + 1, end, level + 1)


traverse(0,len(tree) - 1, 0)
for a in ans:
    print(*a)