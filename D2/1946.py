T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = []
    for n in range(N):
     
        D, L = input().split()
        unzip = D * int(L)
        lst.extend(unzip)
    
    count = len(lst) // 10
    print(f'#{tc}')
    for c in range(count):
        for l in range(10):
            res = lst[l]
            print(res, end='')
        if len(lst) > 20:
            lst = lst[10:]
        else:
            print()
            for l in range(10, len(lst)):
                res = lst[l]
                print(res, end='')
        print()

