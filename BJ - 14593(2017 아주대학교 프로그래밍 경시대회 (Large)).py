N = int(input())
arr = []
for i in range(N):
    S,C,L = map(int,input().split())
    C *= -1
    L *= -1
    arr.append([S,C,L, i+1])
arr.sort(reverse = True)
#print(arr)
print(arr[0][3])
