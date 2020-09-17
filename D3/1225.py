import sys
sys.stdin = open('input1225.txt', 'r')


def get_password():
    k = 0
    while(k < 5):
        k += 1
        if password[0] - k > 0:
            first = password.pop(0)
            password.append(first- k)
        else:
            password.pop(0)
            password.append(0)
            return
        if k == 5:
            k = 0

T = 10
for tc in range(1, T+1):
    int(input())
    password = list(map(int,input().split()))
    get_password()
    print('#{}' .format(tc), end= ' ')
    for i in range(8):
        print(password[i], end=' ')
    print()