def getcombination(k, rate, cal):
    global maxrate
    if cal > maxcal:
        return
    if k == ingredients -1:
        if rate >= maxrate:
            maxrate = rate
            return
        else:
            return
    getcombination(k+1, rate + info[k+1][0], cal + info[k+1][1])
    getcombination(k + 1, rate, cal)

T = int(input())
for tc in range(1, T+1):
    ingredients, maxcal = map(int, input().split())
    info = []
    for i in range(ingredients):
        info.append(list(map(int, input().split())))
    rate = 0
    cal = 0
    maxrate = 0

    getcombination(-1, rate, cal)

    print('#{} {}' .format(tc, maxrate))