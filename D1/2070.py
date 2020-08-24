T = int(input())
for tc in range(1, T+1):    
    N, M = map(int, input().split())
    if N > M :
        res = '>'
    elif N < M :
        res = '<'
    else: 
        res = '='
    print(f'#{tc} {res}')