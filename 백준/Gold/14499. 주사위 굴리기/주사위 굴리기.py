def roll_dice(dice, direction):
    top, north, east, west, south, bottom = dice
    if direction == 1:  # 동쪽
        return [west, north, top, bottom, south, east]
    elif direction == 2:  # 서쪽
        return [east, north, bottom, top, south, west]
    elif direction == 3:  # 북쪽
        return [south, top, east, west, bottom, north]
    elif direction == 4:  # 남쪽
        return [north, bottom, east, west, top, south]

def simulate_dice_rolls(N, M, x, y, board, commands):
    # 주사위 초기 상태
    dice = [0, 0, 0, 0, 0, 0]
    # 방향에 따른 이동 변화 (동, 서, 북, 남)
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    for command in commands:
        # 이동할 방향
        dx, dy = directions[command - 1]
        nx, ny = x + dx, y + dy
        
        # 지도의 범위를 벗어나면 무시
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        
        # 주사위 굴리기
        dice = roll_dice(dice, command)
        
        # 이동한 칸의 값에 따른 주사위와 지도의 상호 작용
        if board[nx][ny] == 0:
            board[nx][ny] = dice[5]  # 주사위 바닥면의 값 복사
        else:
            dice[5] = board[nx][ny]  # 칸의 값을 주사위 바닥면에 복사
            board[nx][ny] = 0
        
        # 주사위 윗면의 값 출력
        print(dice[0])
        
        # 현재 좌표 갱신
        x, y = nx, ny

# 입력 처리
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
x = int(data[2])
y = int(data[3])
K = int(data[4])

board = []
index = 5
for i in range(N):
    board.append(list(map(int, data[index:index + M])))
    index += M

commands = list(map(int, data[index:]))

# 주사위 굴리기 시뮬레이션 실행
simulate_dice_rolls(N, M, x, y, board, commands)