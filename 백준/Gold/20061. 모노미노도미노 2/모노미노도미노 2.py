import sys

input = sys.stdin.readline

# 보드 생성
green = [[0]*4 for _ in range(6)]
blue = [[0]*6 for _ in range(4)]

score = 0

# 초록 보드에 블록 추가
def drop_on_green(t, x, y):
    if t == 1:
        r = 0
        while r+1 < 6 and green[r+1][y] == 0:
            r += 1
        green[r][y] = 1
    elif t == 2:
        r = 0
        while r+1 < 6 and green[r+1][y] == 0 and green[r+1][y+1] == 0:
            r += 1
        green[r][y], green[r][y+1] = 1, 1
    elif t == 3:
        r = 0
        while r+2 < 6 and green[r+2][y] == 0:
            r += 1
        green[r][y], green[r+1][y] = 1, 1


# 파란 보드에 블록 추가
def drop_on_blue(t, x, y):
    if t == 1:
        c = 0
        while c+1 < 6 and blue[x][c+1] == 0:
            c += 1
        blue[x][c] = 1
    elif t == 2:
        c = 0
        while c+2 < 6 and blue[x][c+1] == 0 and blue[x][c+2] == 0:
            c += 1
        blue[x][c], blue[x][c+1] = 1, 1
    elif t == 3:
        c = 0
        while c+1 < 6 and blue[x][c+1] == 0 and blue[x+1][c+1] == 0:
            c += 1
        blue[x][c], blue[x+1][c] = 1, 1


# 초록 보드 줄 제거
def clear_green():
    global score
    # 가득 찬 행 제거
    to_clear = []
    for i in range(6):
        if sum(green[i]) == 4:
            to_clear.append(i)
    # 점수 계산 및 줄 제거
    for i in to_clear:
        score += 1
        green.pop(i)
        green.insert(0, [0, 0, 0, 0])

    # 연한 구역 확인
    shift = sum(1 for i in [0, 1] if sum(green[i]) > 0)
    for _ in range(shift):
        green.pop()
        green.insert(0, [0, 0, 0, 0])


# 파란 보드 줄 제거
def clear_blue():
    global score
    # 가득 찬 열 제거
    to_clear = []
    for j in range(6):
        if sum(blue[i][j] for i in range(4)) == 4:
            to_clear.append(j)

    # 점수 계산 및 열 제거
    for j in to_clear:
        score += 1
        for i in range(4):
            for k in range(j, 0, -1):
                blue[i][k] = blue[i][k-1]
            blue[i][0] = 0

    # 연한 구역 확인
    shift = sum(1 for j in [0, 1] if sum(blue[i][j] for i in range(4)) > 0)
    for _ in range(shift):
        for i in range(4):
            for k in range(5, 0, -1):
                blue[i][k] = blue[i][k-1]
            blue[i][0] = 0


def count_blocks():
    return sum(sum(row) for row in green) + sum(sum(row) for row in blue)


n = int(input())
for _ in range(n):
    t, x, y = map(int, input().split())

    # 블록 추가
    drop_on_green(t, x, y)
    drop_on_blue(t, x, y)

    # 점수 계산
    clear_green()
    clear_blue()

# 결과 출력
print(score)
print(count_blocks())