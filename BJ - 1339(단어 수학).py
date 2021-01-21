N = int(input())
sumlist =[0 for _ in range(26)]
sum =0
for i in range(N):
    temp = input()
    for j in range(len(temp)):
        prev = int(sumlist[ord(temp[j])-65])
        del sumlist[ord(temp[j])-65]
        sumlist.insert(ord(temp[j])-65,prev+10**(len(temp)-j-1))
sumlist.sort(reverse = True)
index =0
answer =0
for i in range(9,0,-1):
    answer += sumlist[index] *i
    index+=1
    
#print(sumlist)
print(answer)

