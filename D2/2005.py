T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = []
    for n in range(N):
        lst = [0] * (n+1)
        lst[0] = 1
        lst[n] = 1

        for m in range(1, n):
            lst[m] = result[n-1][m-1] + result[n-1][m]            
        result.append(lst)
    print(f'#{tc}')
    for s in result:
        for j in s:
            print(f'{j}', end=" ")
        print()