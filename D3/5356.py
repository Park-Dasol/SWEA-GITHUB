T = int(input())
for tc in range(1, T + 1):
    words = [list(input()) for _ in range(5)]
    maxlen = 0
    for i in range(5):
        if len(words[i]) > maxlen:
            maxlen = len(words[i])
    print('#{}'.format(tc), end=' ')
    for j in range(maxlen):
        for l in range(5):
            if len(words[l]) > j:
                print(words[l][j], end='')
            else:
                continue

            #try, except 구문을 이용해도 같은 결과를 얻을 수 있다.
    print()

'''

2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx


'''
