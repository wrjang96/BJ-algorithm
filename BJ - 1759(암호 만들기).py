from itertools import combinations

L, C = map(int, input().split())
alphabet_list = list(map(str, input().split()))
alphabet_list.sort()
temp_answer_list = list(combinations(alphabet_list,L))
vowel = ["a","e","i","o","u"]
answer_list = []
for temp in temp_answer_list:
    v_cnt = 0
    c_cnt = 0
    temp = list(temp)
    for temp_char in temp:
        if temp_char in vowel:
            v_cnt +=1
        else:
            c_cnt += 1
    if v_cnt >=1 and c_cnt >=2:
        temp_str = ""
        for i in range(len(temp)):
            temp_str += temp[i]
        print(temp_str)


# for numbers in temp_answer:
#     print(numbers)
#     temp_numbers = list(numbers)
#     temp_numbers.sort()
#     answer_list.append(temp_numbers)
# answer_list.sort()
# for i in range(len(answer_list)):
#     for j in range(len(answer_list[i])):
#         print(answer_list[i][j], end="")
#     print()