T= int(input())

for tc in range(1, T+1):
    lst = list(map(int,input().split()))
    total = 0
    n = len(lst)
    for l in lst:
        total += l

    result = round(total/n)


    print(f'#{tc} {int(result)}')


    # round 없이 반올림하려면
    # 7.8 * 10 을 하면 78이 된다.
    # 78 % 10 을 하면 1의 자리 숫자가 나온다.
    # 그 나머지가 5 이상이라면 반올림을 한다.
    # 5 미만이라면 버림을 한다.
    # 10을 더한상태에서 // 10을 하던지
    # //을 하고 1을 더하던지 하면 된다.
