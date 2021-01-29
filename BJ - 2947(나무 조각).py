from sys import stdin
data = list(map(int,stdin.readline().split()))
answer = [1,2,3,4,5]
while (1):
    for i in range (0,4,1):
        if data[i] > data[i+1]:
            temp = data[i]
            data[i] = data[i+1]
            data[i+1] = temp
            for i in range(0, 5, 1):
                print(data[i],end =' ')
            print()
    if answer == data:
        break
