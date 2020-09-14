T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    #i A bread. j B bread
    if A < B :
        bread = C // A
    else:
        bread = C // B
    print('#{} {}' .format(tc, bread))

