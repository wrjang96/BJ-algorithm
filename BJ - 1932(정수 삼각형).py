N = int(input())
triangle = [list(map(int,input().split())) for i in range(N)]
result = [[-1] *N for i in range(N)] #입력값 없으면 -1

for i in range(0,N,1):
    for j in range(0,i+1,1):
        result[i][j] = triangle[i][j]  
        

for i in range(0,N-1,1):
    for j in range(0,i+1,1):
        temp1 = result[i][j]+triangle[i+1][j]
        temp2 = result[i][j]+triangle[i+1][j+1]
        if(temp1 != -1):
            result[i+1][j] = max(result[i+1][j],temp1)
        if(temp2 != -1):
            result[i+1][j+1] = max(result[i+1][j+1],temp2)
        
print(max(result[N-1])) # 최종 행렬의 max 값 출력

#for i in range(0,N,1):
#    for j in range(0,i+1,1):
#        print(i,j)
#        print(triangle[i][j])
        #print(triangle[i][j] +triangle[i-1][j], triangle[i+1][j] +triangle[i-1][j])
    
