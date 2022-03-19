def make_table(S):
    length = len(S)
    table = [0] * length
    j = 0
    for i in range(1, length):
        while j > 0 and S[i] != S[j]:
            j = table[j - 1]

        if S[i] == S[j]:
            j += 1
            table[i] = j

    return table


def kmp(P, S):
    table = make_table(S)
    Plen = len(P)
    Slen = len(S)
    j = 0
    for i in range(Plen):
        while j > 0 and P[i] != S[j]:
            j = table[j - 1]
        if P[i] == S[j]:
            if j == Slen - 1:
                return 1
            else:
                j += 1

    return 0

P = input()
S = input()
print(kmp(P, S))