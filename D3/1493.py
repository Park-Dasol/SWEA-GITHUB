
def getP(n):
    idx = 1
    cnt = 0
    global info
    info = [[0] * 2]
    while idx <= n :
        cnt += 1
        for j in range(1, cnt+1):
            info.append([cnt - j + 1,j])
            if idx == n:
                return cnt-j +1, j
            idx += 1


def getQ(x, y):
    idx = 1
    cnt = 0
    global info
    info = [[0] * 2]
    while(10000):
        cnt += 1
        for j in range(1, cnt + 1):
            info.append([cnt - j + 1, j])
            if x == cnt-j +1 and y == j:
                return idx
            idx += 1


T = int(input())
for tc in range(1, T+1):
    x, y = map(int, input().split())

    i, j = getP(x)
    l, m = getP(y)

    v = i + l
    w = j + m

    res = getQ(v, w)
    print('#{} {}' .format(tc, res))