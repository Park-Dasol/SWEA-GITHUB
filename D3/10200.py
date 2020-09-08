T = int(input())
for tc in range(1, T+1):
    N, A, B = map(int, input().split())
    if A >= B:
        maxc = B
    elif A < B:
        maxc = A
    if (A+B) - N > 0:
        minc = (A+B)- N
    else:
        minc = 0
    print('#{} {} {}' .format(tc, maxc, minc))