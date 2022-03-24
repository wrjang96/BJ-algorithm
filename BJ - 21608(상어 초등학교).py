N = int(input())
class_arr = [[0] * N for i in range(N)]
arr = [[] for i in range(N **2 + 1)]
orders = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def find(num, class_arr, arr):
    visited = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if 0 <= i + dx[k] < N and 0 <= j + dy[k] < N:
                    if class_arr[i + dx[k]][j + dy[k]] in arr[num]:
                        visited[i][j] += 1
    sort_arr =[]
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(4):
                if 0 <= i + dx[k] < N and 0 <= j + dy[k] < N:
                    if class_arr[i + dx[k]][j + dy[k]] ==0:
                        cnt += 1
            if class_arr[i][j] ==0:
                sort_arr.append([visited[i][j] * -1, cnt * -1 , i, j])
    sort_arr.sort()
    class_arr[sort_arr[0][2]][sort_arr[0][3]] = num

def cal(class_arr, arr):
    ans = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(4):
                if 0 <= i + dx[k] < N and 0 <= j + dy[k] < N:
                    if  class_arr[i + dx[k]][j + dy[k]] in arr[class_arr[i][j]] :
                        cnt += 1
            if cnt == 1:
                ans +=1
            if cnt == 2:
                ans += 10
            if cnt == 3:
                ans += 100
            if cnt == 4:
                ans += 1000
    return ans


for i in range(N **2):
    tmp, one, two, three, four = map(int, input().split())
    arr[tmp] = [one, two, three, four]
    orders.append(tmp)

for order in orders:
    find(order, class_arr, arr)

print(cal(class_arr, arr))
