T = int(input())

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, T+1):
    result = 0
    m1, d1, m2, d2 = map(int, input().split())
    if m1 == m2 :
        result = d2 - d1 + 1
    else:
        for i in range(m1, m2):
            result += month[i]
        result += d2 - d1 + 1
    print(f'#{tc} {result}')
    


