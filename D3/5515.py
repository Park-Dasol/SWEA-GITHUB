T= int(input())
months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, T+1):
    start = 3
    days = 3
    m, d = map(int, input().split())
    for i in range(m):
        days += months[i]
    days += d
    print('#{} {}' .format(tc, days%7))