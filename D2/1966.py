T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(N-1):
        res = i
        for j in range(i+1, N):
            if lst[res] > lst[j]:
                res = j
        lst[i], lst[res] = lst[res], lst[i]
    print(f'#{tc}', end=" ")
    for n in range(N):
        print(f'{lst[n]}', end=" ")
    print()