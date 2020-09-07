import sys
sys.stdin = open('input1916.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    brd = [list(map(int, input().split())) for _ in range(N)]

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(brd[N-j-1][i], end='')
        print(' ', end='')
        for j in range(N):
            print(brd[N-i-1][N-j-1], end='')
        print(' ', end='')
        for j in range(N):
            print(brd[j][N-i-1], end='')
        print()

