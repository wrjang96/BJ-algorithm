input_num, output_num = map(int, input().split())
memo = {}
for i in range(input_num):
    input_site, input_password = map(str, input().split())
    memo[input_site] = input_password
for i in range(output_num):
    print(memo[input().rstrip()])