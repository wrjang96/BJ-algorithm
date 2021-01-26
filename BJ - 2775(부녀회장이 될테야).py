from sys import stdin
testcase = int(stdin.readline())

while testcase:
    K = int(stdin.readline())
    N = int(stdin.readline())
    apartment = [[0] * N for i in range(K+1)]
    for i in range(0,1,1):
        for j in range(0,N,1):
            apartment[i][j] = j+1
    for i in range(0,K+1,1):
        for j in range(0,1,1):
            apartment[i][j] = 1

    for i in range(1,K+1,1):
        for j in range(1,N,1):
            apartment[i][j] = apartment[i-1][j] +apartment[i][j-1] 
    print(apartment[K][N-1])
    testcase -=1
