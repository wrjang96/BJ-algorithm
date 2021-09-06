N,K = map(int,input().split())
cnt = 0

for t in range(N + 1):
    for m in range(60):
        for s in range(60):
            if str(K) in f'{str(t):0>2}{str(m):0>2}{str(s):0>2}':
                cnt += 1
print(cnt)

# for k in range(N + 1):
#     for i in range(60):
#         for j in range(60):
#             if k >=0 and k <=9:
#                 hour = str(0) + str(k)
#             else:
#                 hour = str(k)
#             if i >= 0 and i <= 9:
#                 minute = str(0) + str(i)
#             else:
#                 minute = str(i)
#             if j >= 0 and j <= 9:
#                 second = str(0) + str(j)
#             else:
#                 second = str(j)
#             answer_num = hour + minute + second
#             flag = False
#             for a in range(len(answer_num)):
#                 if answer_num[a] == str(K):
#                     # print(answer_num[a], str(K))
#                     flag = True
#             if flag == True:
#                 cnt +=1
#             # print(answer_num)
# print(cnt)