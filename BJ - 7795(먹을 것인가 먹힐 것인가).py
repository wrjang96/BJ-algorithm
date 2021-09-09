testcase = int(input())
# 이분 탐색을 사용해 B에서 A의 한 요소(a) 보다 작은 수들 중에 제일 큰 수의 위치(인덱스)를 찾는 것이 핵심이다.
def binary_search(arr, a):
    s, e = 0, len(arr)-1
    res = -1
    while s <= e:
        m = (s + e) // 2
        if arr[m] < a:
            res = m
            s = m + 1
        else:
            e = m - 1
    return res

while testcase:
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    print(A,B)
    cnt = 0
    for a in A:
        cnt += (binary_search(B, a) + 1)
    print(cnt)
    testcase -= 1