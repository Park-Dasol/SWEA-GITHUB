month= [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())
for tc in range(1, T+1):
    date = str(input())
    y = date[0:4]
    m = date[4:6]
    d = date[6:]
    M = int(m)
    D = int(d)
    
    if M < 1 or M > 12:
        result = -1 
    elif month[M] < D :
        result = -1
    else:
        result = y + '/' + m +'/'+d
    print(f'#{tc} {result}')


