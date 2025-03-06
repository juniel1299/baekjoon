from collections import deque

# 방향 전환 함수
def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

# 보드 크기
n = int(input())
board = [[0] * n for _ in range(n)]

# 사과 위치
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1  # 사과 위치를 1로 표시

# 방향 전환 정보
l = int(input())
info = {}
for _ in range(l):
    x, c = input().split()
    info[int(x)] = c

# 초기 설정
dx = [0, 1, 0, -1]  # 동, 남, 서, 북
dy = [1, 0, -1, 0]
direction = 0  # 초기 방향: 동쪽
time = 0
x, y = 0, 0  # 초기 위치
snake = deque([(x, y)])
board[x][y] = 2  # 뱀이 있는 위치를 2로 표시

# 게임 시작
while True:
    time += 1
    x += dx[direction]
    y += dy[direction]
    
    # 벽에 부딪히거나 자기 몸에 부딪히면 게임 종료
    if x < 0 or x >= n or y < 0 or y >= n or board[x][y] == 2:
        break
    
    # 사과가 있다면
    if board[x][y] == 1:
        board[x][y] = 2
        snake.append((x, y))
    else:
        # 사과가 없다면
        board[x][y] = 2
        snake.append((x, y))
        tail_x, tail_y = snake.popleft()
        board[tail_x][tail_y] = 0
    
    # 방향 전환 시간이 되면
    if time in info:
        direction = turn(direction, info[time])

print(time)