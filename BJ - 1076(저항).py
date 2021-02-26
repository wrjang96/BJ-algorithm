resistence = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
cnt = 3
result =""
while(cnt):
    N = input()
    if cnt >=2:
        result += str(resistence.index(N))
    else:
        result = int(result)
        result = result * 10**resistence.index(N)
    cnt -=1
print(result)
