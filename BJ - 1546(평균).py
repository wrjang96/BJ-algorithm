N = int(input())
data = list(map(int,input().split()))
data.sort(reverse = True)
maxi = data[0]
total =0
for data in data:
    total+=(data/maxi)*100
sum = total/N
print(sum)
