T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    N = len(lst)
    for i in range(N-1):
        res = i
        for j in range(i, N):
            if lst[j] < lst[res]:
                res = j
        lst[i], lst[res] = lst[res], lst[i]
    total = 0
    for l in range(1, N-1):
        total += lst[l]
    result = round(total / (N-2), 0)
    print(f'#{tc} {int(result)}')
