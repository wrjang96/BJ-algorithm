N = int(input())
arr = list(map(int, input().split()))
cal = list(map(int, input().split()))
tmp = []

min = 10 ** 22
max = 10 ** 22 * -1


def solve(idx, val, pl,mi,mu,di):
    global min
    global max
    global N
    if idx >= N:
        if val < min:
            min = val
        if val > max:
            max = val
    if pl > 0:
        solve(idx + 1, val + arr[idx], pl-1, mi,mu,di)
    if mi > 0:
        solve(idx + 1, val - arr[idx], pl, mi - 1, mu, di)
    if mu > 0:
        solve(idx + 1, val * arr[idx], pl, mi, mu - 1, di)
    if di > 0:
        solve(idx + 1, int(val / arr[idx]), pl, mi, mu, di - 1)


solve(1, arr[0], cal[0], cal[1], cal[2], cal[3])

print(max)
print(min)