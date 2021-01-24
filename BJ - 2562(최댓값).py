maxi =0
index = 0
for i in range(0,9,1):
    temp = int(input())
    maxi = max(temp,maxi)
    if(maxi==temp):
        index = i+1

print(maxi)
print(index)
        
