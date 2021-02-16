import sys
input = sys.stdin.readline
N = int(input())
crane = list(map(int,input().split()))
crane.sort(reverse = True)
M = int(input())
cargo = list(map(int, input().split()))
cargo.sort(reverse = True)
if cargo[0] > crane[0]:
    print(-1)
else:
    time =0
    while(len(cargo)):
        time +=1
        for i in range(len(crane)):
            for j in range (len(cargo)):
                if cargo[j] <= crane[i]:
                    cargo.pop(0+j)
                    break

    print(time)
#3
#6 8 9
#9
#1 2 3 4 5 6 7 8 9