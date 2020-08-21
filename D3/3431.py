T = int(input())

for tc in range(1, T+1):
    l, u, x = map(int, input().split())

    if x > u:
        res = -1
    elif l <= x <= u:
        res = 0
    else:
        res = l - x
    print(f'#{tc} {res}')
        