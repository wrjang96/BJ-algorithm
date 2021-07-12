first_input = str(input())
sec_input = str(input())
queue = [sec_input]

while True:
    if len(queue[0]) == 0:
        print(0)
        break
    if queue[0] == first_input:
        print(1)
        break
    temp_str = queue.pop(0)
    if temp_str[-1] == "A":
        temp_str = temp_str[:-1]
        queue.append(temp_str)
    elif temp_str[-1] == "B":
        temp_str = temp_str[:-1]
        temp_str = temp_str[::-1]
        queue.append(temp_str)

    #print(temp_str)