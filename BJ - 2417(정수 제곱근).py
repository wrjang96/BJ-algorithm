N = int(input())
start =0
end = int((2**63)**0.5)+1
cnt = 0
q = 0

while(start<=end):
    mid = (start + end)//2
    if mid*mid >= N:
        q = mid
        end = mid - 1
    else:
        start = mid + 1
print(q)