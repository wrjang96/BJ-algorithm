temp = input()
alphabet = [0 for i in range(26)]

for i in range(len(temp)):
    if 65<=ord(temp[i])<=90:
        alphabet[ord(temp[i])-65]+=1
    elif 97<=ord(temp[i])<=122:
        alphabet[ord(temp[i])-97]+=1
#print(max(alphabet))
cnt =0
index=0
for i in range(26):
    if(max(alphabet)==alphabet[i]):
        cnt+=1
        index =i
        
if(cnt>=2):
    print('?')
else:
    print(chr(index+65))

