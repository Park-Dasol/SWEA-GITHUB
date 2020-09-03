import sys
sys.stdin = open('input1959.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Num= list(map(int, input().split()))# 짧은애
    Mum= list(map(int, input().split())) #긴애

    if N > M :
        Num, Mum = Mum, Num
        M, N = N, M
    # print(Num, Mum)
    result = 0
    for i in range(M-N +1): #긴애의 인덱스 M
        total = 0
        for j in range(N): # 짧은애의 인덱스
            total += Num[j] * Mum[j+i]
        if total >= result:
            result = total
    print('#{} {}'.format(tc, result))