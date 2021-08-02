input_string = str(input())
answer =[]
for i in range(1, len(input_string)):
    for j in range(i+1,len(input_string)):
        #print(input_string[:i][::-1], input_string[i:j][::-1], input_string[j:][::-1])
        answer.append(input_string[:i][::-1] + input_string[i:j][::-1] + input_string[j:][::-1])
answer.sort()
print(answer[0])

