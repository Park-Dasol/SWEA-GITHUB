T = int(input())
for tc in range(1,T+1):
    a, b = map(int, input().split())
    m = a // b
    n = a % b
    print('#{} {} {}' .format(tc, m, n))