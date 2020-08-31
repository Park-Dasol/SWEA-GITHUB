def check(m, total):
    x = med -m
    y = med
    for dir in range(4):
               
        for i in range(m):
            x += dx[dir]
            y += dy[dir] 
            total += mat[x][y]
            # print(total)
            #print(x, y,dir)
    return total

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input()))for _ in range(N)]
    #print(mat)
    med = N // 2
    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, +1]
    total = mat[med][med]

    for m in range(1, med+1):
        total = check(m, total)

    print('#{} {}' .format(tc, total))