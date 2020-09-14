T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = [0] * (N)
    for q in range(1, Q+1):
        L, R = map(int, input().split())
        for i in range(N):
            if L -1 <= i <= R-1:
                boxes[i] = q
    print('#{}' .format(tc), end=' ')
    for i in range(N):
        print(boxes[i], end=' ')
    print()
