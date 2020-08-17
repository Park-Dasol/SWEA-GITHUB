T = int(input())

def iswall(x, y, N, res):
    if x < 0 or x >= N:
        return True
    if y < 0 or y >= N:
        return True
    if res[x][y] != 0:
        return True
   
    return False


for tc in range(1, T+1):
    N = int(input())

    res = [[0]*N for _ in range(N)]
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    xp = yp = 0
    dir = 0
    nx = ny = 0

    for i in range(1, N**2 + 1):
        res[xp][yp] = i
        nx = xp + dx[dir]
        ny = yp + dy[dir]

        if iswall(nx, ny, N, res):
            dir = dir + 1
            if dir == 4:
                dir = 0
        xp = xp + dx[dir]
        yp = yp + dy[dir]


    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(res[i][j], end=' ')
        print()


