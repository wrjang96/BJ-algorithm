# 스프러그- 그런디 정리
# : 게임판의 상태를 각각 하나의 자연수로 치환할 수 있다는 것이다.
# 1. 아무것도 할수 없는 그런디 수의 초기화는 0이다
# 2. 그런디 수가 같은 두 게임판의 상태는 같은 상태이다.
# 따라서 그런디 수가 0인 상태는 무조건 패배하는 상태이며 0보다 큰 상태에서는 한 번의 행동으로 무조건 그런디 수가 0인 상태로
# 만들 수 있으니 승리할 수 있는 상태입니다.
#
# n개의 게이밍 있고 각 게임판의 그런디 수가 g1 g2 g3일 경우
# 그런디 수 = g1 xor(^) g2 xor(^) g3
# 그런디 수가 0 이면, 먼저 게임을 진행한 사람이 패배

N = int(input())
arr = list(map(int, input().split()))

grundy_num = 0
for temp in arr:
    grundy_num ^= temp

if grundy_num == 0:
    print("cubelover")
else:
    print("koosaga")

















#
#
#
#
#
#
#
#
#
#
#
#
# grundy_num = 0;
# for i in range(N):
#     grundy_num ^= arr[i]
#
# if grundy_num:
#     print("koosaga")
# else:
#     print("cubelover")
#
