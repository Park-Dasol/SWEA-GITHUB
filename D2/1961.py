T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [0]* N
    for n in range(N):
        lst[n] = list(map(int, input().split()))
    a = [[0 for _ in range(N)] for _ in range(N)]
    b = [[0 for _ in range(N)] for _ in range(N)]
    c = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            a[j][N-i-1] = lst[i][j]
            b[N-i-1][N-j-1] = lst[i][j]
            c[N-j-1][i] = lst[i][j]
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(a[i][j], end="")
        print(f' ', end="")
        for j in range(N):
            print(b[i][j], end="")
        print(f' ', end="")
        for j in range(N):
            print(c[i][j], end="")
        print()
    


