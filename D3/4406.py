T = int(input())

for tc in range(1, T+1):
    word = input()
    result = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for l in word:
        if not l in vowels:
            result += l
    print(f'#{tc} {result}')