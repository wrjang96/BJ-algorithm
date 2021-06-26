from collections import deque
n = int(input())
for i in range(n):
    input_string = deque(list(map(str, input().split())))
    for j in range(2):
        tmp = input_string.popleft()
        input_string.append(tmp)
    result = " ".join(input_string)
    print(result)


