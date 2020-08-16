T = int(input())

for tc in range(1, T+1):
    N = input()
    lst = [0]*10
    K = 0
    result = 0
    while result == 0:
        K += 1
        M = int(N) * K
        M = str(M)
        for i in range(len(M)):
            j = int(M[i])
            lst[j] += 1
        for c in range(len(lst)):
            if lst[c] == 0:
                result = 0
                break
            else:
                result = 1
    print(f'#{tc} {M}')


