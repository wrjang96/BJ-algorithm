N = int(input())
cnt2 =0
cnt5 =0
mini =0
       
for i in range(1,N+1,1):
    while(i%2==0 or i%5==0):
        #print(i)
        if(i%2==0):
            i =i//2
            cnt2+=1
        if(i%5==0):
            i =i//5
            cnt5+=1
#print(cnt2,cnt5)
mini = min(cnt2,cnt5)
print(mini)
    
