croatian_alphabet = ["c=","c-","dz=","d-","lj","nj","s=","z="]
temp = input()
cnt = len(temp)
for i in croatian_alphabet:
    temp = temp.replace(i,"A")

print(len(temp))