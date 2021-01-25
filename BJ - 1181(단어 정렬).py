N = int(input())
words =[]
while N:
    tmp = input()
    words.append(tmp.strip())
    N-=1
words = set(words)
words = list(words)
words2 =[]
for i in range (len(words)):
    words2.append([len(words[i]),words[i]])
words2.sort()
for i in range (len(words2)):
    print(words2[i][1])
    
