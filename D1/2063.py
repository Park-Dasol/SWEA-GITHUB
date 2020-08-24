N = int(input())
lst = list(map(int, input().split()))
for i in range(N-1, 0, -1):
    for j in range(0, i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
med = N // 2

print(lst[med])