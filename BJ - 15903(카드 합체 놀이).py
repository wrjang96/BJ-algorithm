N, M = map(int,input().split())
number = list(map(int,input().split()))
number.sort()
while M:
    twosum = number[0] + number[1]
    number[0] = twosum
    number[1] = twosum
    number.sort()
    M -= 1
print(sum(number))