# 1.   '<' 있을 경우는 일렬로 저장하기 때문에 정답 문자열에 그대로 입력
# 1-1) '<' 받았을 경우 flag =1로 변경 후 그대로 정답에 저장
# 1-2) '>' 만났을 경우 flag =0으로 변경
# 2.   그외의 경우 공백 혹은 '<'를 만날 경우까지 저장 후 뒤집을 문자열이다
# 2-1) 그래서 그 전까지 ans 배열에 저장 후 [::-1] 활용하여 뒤집고 문자열에 넣음
# 2-2) 공백의 경우 누락돼서 뒤집고 문자열연산 후 넣음
# 2-3) 마지막 단어를 뒤집어야 할 경우 대비하여 끝에 ans배열에 저장 여부 확인

from sys import stdin

ans = []
string =''
index =0
S = stdin.readline().rstrip()

flag =0
for i in range(0,len(S),1):
    if(S[i] == '<'):
        if(len(ans) !=0):
            ans = ans[::-1]
            for j in range(len(ans)):
                string +=ans[j]
            ans.clear()
        flag = 1
        string +=S[i]
    elif flag ==1:
        string +=S[i]
        if S[i] == '>':
            flag =0
    elif(S[i] ==' '):
        ans = ans[::-1]
        for j in range(len(ans)):
            string +=ans[j]
        ans.clear()
        string +=S[i]
    else:
        ans.append(S[i])
        
if(len(ans) !=0):
            ans = ans[::-1]
            for j in range(len(ans)):
                string +=ans[j]
            ans.clear()
print(string)
