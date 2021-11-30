input_string = str(input())
stack = 1
answer = 0
flag = input_string[0]
for i in range(1, len(input_string)):
    if input_string[i] == "(":
        stack += 1
    elif input_string[i] == ")":
        stack -= 1
        if flag == "(":
            answer += stack
        else:
            answer +=1
    flag = input_string[i]


print(answer)