

T = int(input())
for tc in range(1, T+1):
    bits =input()
    # print(bits)
    j = '0'
    cnt = 0
    for i in bits:
        if j != i:
            cnt += 1
            j = i
    print('#{} {}' .format(tc, cnt))