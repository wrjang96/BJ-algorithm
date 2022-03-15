import sys
input = sys.stdin.readline
N,M = map(int, input().split())
one_arr =[]
six_arr = []
for i in range(M):
    sixtmp, onetmp = map(int, input().split())
    six_arr.append(sixtmp)
    six_arr.append(onetmp*6)
    one_arr.append(onetmp)

one_arr.sort()
six_arr.sort()

print(min((N//6 + 1) * six_arr[0],(N//6 * six_arr[0]) + ((N%6) * one_arr[0])))