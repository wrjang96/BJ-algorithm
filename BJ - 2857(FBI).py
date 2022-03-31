li = []
for i in range(1, 6):
    w = input()
    if "FBI" in w:
        li.append(i)
if li:
    print(*li) 
else:
    print("HE GOT AWAY!")