N = int(input())
test_plus = []
test_minus = []
for _ in range(N):
    a= int(input())
    if a>0:
        test_plus.append(a)
    else:
        test_minus.append(a)
test_minus.sort()
test_plus.sort(reverse = True)
#print(test_plus)
#print(len(test_plus))
#print(test_minus)

sum =0

for i in range(len(test_plus)):
    while(len(test_plus)>0):
        temp = test_plus[i]
        del test_plus[i]
        if len(test_plus) ==0:
            sum +=temp
            break
        #i+=1
        temp2 = test_plus[i]
        if(temp2 ==1):
            sum+=(temp+temp2)
        else:
            sum += (temp*temp2)
        del test_plus[i]

for i in range(len(test_minus)):
    while(len(test_minus)>0):
        temp = test_minus[i]
        del test_minus[i]
        if len(test_minus) ==0:
            sum +=temp
            break
        #i+=1
        temp2 = test_minus[i]
        sum += (temp*temp2)
        del test_minus[i]

print(sum)
    
