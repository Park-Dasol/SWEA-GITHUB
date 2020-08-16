T = int(input())
for tc in range(1, T+1):
    lst = list(input())
    L = []
    for l in range(len(lst)):
        if lst[l] == ' ':
            break
        else:
            L.append(lst[l])

    N = len(L)

    while N > 1:
        if L[0] == L[N-1]:
            L = L[1:N-1]
            N = len(L)
        else:
            result = 0
            break
        result = 1

    print(f'#{tc} {result}')