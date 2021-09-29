N = int(input())
budget_list = list(map(int, input().split()))
budget_limit = int(input())

left_point = 0
# min(budget_list)로 설정해서 틀림
right_point = max(budget_list)
while left_point <= right_point:
    answer = 0
    temp_ans = 0
    mid = (left_point + right_point) // 2
    for i in range(N):
        if budget_list[i] <= mid:
            answer += budget_list[i]
        else:
            answer += mid
    if answer > budget_limit:
        right_point = mid - 1
    elif answer <= budget_limit:
        left_point = mid + 1
print(right_point)

# 10
# 1 1 1 1 11 11 11 11 11 100
# 100