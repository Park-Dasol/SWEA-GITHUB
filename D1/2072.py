T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    total = 0
    for l in lst:
        if l % 2 :
            total += l
        else : 
            continue

    print(f'#{tc} {total}')