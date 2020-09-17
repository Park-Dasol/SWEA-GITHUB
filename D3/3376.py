def pado(N):
    global k
    if k >= N:
        res = info[N-1]
        return res
    while k != N:
        k += 1
        first = info.pop(0)
        info.append(first + info[-1])
        res = info[-1]
    return res


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    info = [1, 1, 1, 2, 2]
    k = 5
    ans = pado(N)
    print('#{} {}' .format(tc, ans))
