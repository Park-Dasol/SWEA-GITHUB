import sys
sys.stdin = open('input1873.txt', 'r')

def game(key):
    global r, c, curD
    curR = r
    curC = c
    if key == 'S':
        shot = True
        while shot:
            e, f = zip((curR, curC), dirs[curD])
            tarY = sum(e)
            tarX = sum(f)
            if tarX >= 0 and tarX < W and tarY>=0 and tarY < H and matrix[tarY][tarX] == '*':
                matrix[tarY][tarX] = '.'
                matrix[r][c] = keys[curD]
                shot = False
            elif tarX >= 0 and tarX < W and tarY>=0 and tarY < H and matrix[tarY][tarX] == '#':
                matrix[r][c] = keys[curD]
                shot = False
            elif tarX >= 0 and tarX < W and tarY>=0 and tarY < H:
                curR = tarY
                curC = tarX
            else:
                shot = False
    else:
        curD = key
        a, b = zip((r,c), dirs[key])
        newy = sum(a)
        newx = sum(b)
        if newx >= 0 and newx < W and newy>=0 and newy < H and matrix[newy][newx] == '.':
            matrix[newy][newx] = keys[key]
            matrix[r][c] = '.'
            r = newy
            c = newx
        else:
            matrix[r][c] = keys[key]





T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    matrix = [list(map(str, input())) for _ in range(H)]
    N = int(input())
    userinput = list(map(str, input()))

    keys = {'U': '^', 'D': 'v', 'L': '<', 'R': '>', 'S': '.'}
    dirs = {'U': (-1, 0), 'D': (+1, 0), 'L': (0, -1), 'R': (0, 1), 'S': (0, 0)}

    for i in range(H):
        for j in range(W):
            if matrix[i][j] in ('<', '>', '^', 'v'):
                r = i
                c = j
                for k in keys:
                    if keys[k] == matrix[i][j]:
                        curD = k

    for l in userinput:
        game(l)

    print('#{}' .format(tc), end=" ")
    for i in range(H):
        print(''.join(matrix[i]))
