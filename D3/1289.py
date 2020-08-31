T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input()))
    # print(N)
    cnt = 0
    i = 0
    for j in range(len(N)):
        if N[j] != i :
            cnt += 1
            i = N[j]
    print('#{} {}' .format(tc,cnt))