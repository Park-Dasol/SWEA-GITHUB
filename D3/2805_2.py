T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input()))for _ in range(N)]
    #print(mat)
    med = N // 2
    i = 0
    total = 0

    for n in range(N):
        if n > med:
            i = n - med
        else:
            i = med - n
        for j in range(i, N - i):
            total += mat[n][j]

    print('#{} {}' .format(tc,total))
