def powerset(k, cnt):
    if cnt ==3:
        setsum(empty)
        return
    if k == 7:
        return

    empty[k] = 1
    powerset(k+1, cnt+1)
    empty[k] = 0
    powerset(k+1, cnt)


def setsum(empty):
    total = 0
    for i in range(len(empty)):
        if empty[i] == 1:
            total += nums[i]
    result.append(total)

def get5th(result):
    for i in range(0, 5):
        for j in range(i+1, len(result)):
            if result[i] < result[j]:
                result[i], result[j] = result[j], result[i]
    return result[4]


T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    empty = [0]*7
    cnt = 0
    result = []
    powerset(0, cnt)
    my_set = set(result)
    my_list = list(my_set)
    ans = get5th(my_list)
    print('#{} {}' .format(tc, ans))