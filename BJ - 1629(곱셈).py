def pow(x, y, z):
    if y == 1:
        return x % z
    else:
        temp_num = pow(x, y // 2, z)
        if y % 2 == 0:
            return temp_num * temp_num % z
        else:
            return temp_num * temp_num * x % z


A,B,C = map(int, input().split())
print(pow(A,B,C))