T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, T+1):
    
    count = [0]*8
    N = int(input())
    m = 0
    while N != 0:
        for i in range(m, 8):
            if N >= money[i]:
                N -= money[i]
                count[i] += 1
                if N >= money[i]:
                    break
                else:
                    m = i+1

    print(f'#{tc}', end=" ")
    for j in range(8):
        print(count[j], end=" ")
    print()









 
        # for i in range(8):
        #     if N >= money[i]:
        #         count[i] += 1
        #         N -= money[i]
        #         if N >= money[i]:
        #             break
        #         else:
        #             continue