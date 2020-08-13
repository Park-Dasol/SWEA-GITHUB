T = int(input())

for tc in range(1, T+1):

    N, K = map(int, input().split())

    lst = [0] * N
    for n in range(N):
        lst[n] = list(map(int, input().split()))

    cnt = 0
    for i in range(N):
        dist = 0
        for j in range(N):
            if lst[i][j] == 1:
                dist += 1
            elif lst[i][j] != 1 and dist == K:
                cnt += 1
                dist = 0
            else:
                dist = 0
        if dist == K:
            cnt += 1
    for j in range(N):
        dist = 0
        for i in range(N):
            if lst[i][j] == 1:
                dist += 1
            elif lst[i][j] != 1 and dist == K:
                cnt += 1
                dist = 0
            else:
                dist = 0
        if dist == K:
            cnt += 1

    print(f'#{tc} {cnt}')

            
        