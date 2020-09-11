T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    guests = list(map(int, input().split()))
    guests = sorted(guests)
    sold = 0
    flag = 'Impossible'
    for g in range(len(guests)):
        mok = guests[g] // M
        cur = mok * K - sold
        if cur >= 1:
            flag = 'Possible'
            sold += 1
        else:
            flag = 'Impossible'
            break
    print('#{} {}' .format(tc, flag))