N = int(input())
arr = list(map(int, input().split()))
start = 0
end = N - 1
ans = 2147483647
# int 1e9 보다 큰 범위에 유의할 것
ans_arr = []
while start < end:
    if abs(arr[start] + arr[end]) < ans:
        ans_arr.clear()
        ans_arr.append([arr[start], arr[end]])
        ans = abs(arr[start] + arr[end])
    if arr[start] + arr[end] < 0:
        start += 1
    elif arr[start] + arr[end] > 0:
        end -= 1
    else:
        ans_arr.clear()
        ans_arr.append([arr[start], arr[end]])
        break

print(ans_arr[0][0],ans_arr[0][1])