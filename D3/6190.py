T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    num = []
    for i in range(0, N-1):
        for j in range(i+1, N):
            if A[i]*A[j] >= 10:
                num.append(str(A[i]*A[j]))
    res = []
    for i in range(len(num)):
        flag = 0
        for j in range(len(num[i])-1):
            if num[i][j] <= num[i][j+1]:
                flag += 1
        if flag == len(num[i])-1:
            res.append(int(num[i]))
    # print(res)
    ans = -1
    for r in range(len(res)):
        if res[r] > ans:
            ans = res[r]



    print('#{} {}' .format(tc,ans))



'''

1
4
2 4 7 10

'''