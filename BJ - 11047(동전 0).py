N, K = map(int,input().split())
coins = []

for i in range(N):
    coins.append(int(input()))
coins.reverse()
cnt =0

while(K>0):
    for i in range(0,N,1):
        if(K>=coins[i]):
            K -= coins[i]
            cnt+=1
            break
        
print(cnt)
    
