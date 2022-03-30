N, K = map(int, input().split())
tem_list = list(map(int, input().split()))

part_sum = sum(tem_list[:K])
answer = [part_sum]

for i in range(0, len(tem_list)-K):
    part_sum = part_sum - tem_list[i] + tem_list[i+K]
    answer.append(part_sum)

print(max(answer))