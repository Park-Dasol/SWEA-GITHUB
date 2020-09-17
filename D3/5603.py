T = int(input())
for tc in range(1, T+1):
    N = int(input())
    info = [0] * N
    total = 0
    for n in range(N):
        info[n] = int(input())
        total += info[n]
    ave = total // N
    cha = 0
    for i in range(N):
        if info[i] - ave >= 0:
            cha += info[i] - ave
    print('#{} {}' .format(tc, cha))
