import sys
sys.stdin = open('input1204.txt', 'r')

T= int(input())
for tc in range(1, T+1):
    int(input())
    students = list(map(int, input().split()))
    score = [0] * 101
    for st in range(1000):
        score[students[st]] += 1
    fre = 0
    for sc in range(101):
        if score[sc] >= score[fre]:
            fre = sc
    print('#{} {}' .format(tc, fre))
