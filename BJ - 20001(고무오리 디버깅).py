# import sys
# input = sys.stdin.readline
cnt = 0
while True:
    input_string = input()
    if input_string == "고무오리 디버깅 끝":
        break
    if input_string == "문제":
        cnt +=1
    if input_string == "고무오리":
        if cnt == 0:
            cnt +=2
        else:
            cnt -=1

if cnt == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')
