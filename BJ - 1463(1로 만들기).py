queue = []
visited = set()
def bfs(start,cnt1):
    queue.append((start,cnt1))
    visited.add((start,cnt1))
    while(1):
        X, cnt = queue.pop(0)
        if (X == 1):
            return cnt
            break
        if (X % 3 == 0):
            if (X // 3, cnt + 1) not in visited:
                queue.append((X // 3, cnt + 1))
                visited.add((X // 3, cnt + 1))
        if (X % 2 == 0):
            if (X // 2, cnt + 1)not in visited:
                visited.add((X // 2, cnt + 1))
                queue.append((X // 2, cnt + 1))
        if (X > 1):
            if (X - 1, cnt + 1) not in visited:
                visited.add((X - 1, cnt + 1))
                queue.append((X - 1, cnt + 1))
        #print(queue)
X = int(input())
print(bfs(X,0))