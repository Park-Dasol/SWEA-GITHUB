T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    i = 0
    for l in lst:
        if l > i :
            i = l
        else : 
            continue
    print(f'#{tc} {i}')