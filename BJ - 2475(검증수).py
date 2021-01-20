import math

result =0
#for i in range(5):
data =list(map(int,input().split()))
for i in data:
           result += i**2
#print(result)
print(result%10)
