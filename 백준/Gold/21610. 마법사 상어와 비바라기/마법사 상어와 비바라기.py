import sys

input = sys.stdin.readline

# 방향 벡터 설정
dy8 = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dx8 = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 대각선 4방향 (↖, ↗, ↘, ↙)
dy4 = [-1, -1, 1, 1]
dx4 = [-1, 1, -1, 1]

def move_clouds(clouds, d, s, N):
    new_clouds = set()
    for y, x in clouds:
        ny = (y + dy8[d] * s) % N
        nx = (x + dx8[d] * s) % N
        new_clouds.add((ny, nx))
    return new_clouds

def water_copy_bug(board, clouds, N):
    for y, x in clouds:
        count = 0
        for d in range(4):
            ny = y + dy4[d]
            nx = x + dx4[d]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] > 0:
                count += 1
        board[y][x] += count

def create_new_clouds(board, prev_clouds, N):
    new_clouds = set()
    for y in range(N):
        for x in range(N):
            if (y, x) not in prev_clouds and board[y][x] >= 2:
                new_clouds.add((y, x))
                board[y][x] -= 2
    return new_clouds

def simulate_magic_shark(N, M, board, commands):
    # 초기 구름 위치 (set 사용)
    clouds = {(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)}

    for d, s in commands:
        # 1. 모든 구름이 d 방향으로 s칸 이동
        clouds = move_clouds(clouds, d, s, N)

        # 2. 각 구름이 있는 칸의 물의 양이 1 증가
        for y, x in clouds:
            board[y][x] += 1

        # 3. 물복사 버그 마법 시전
        water_copy_bug(board, clouds, N)

        # 4. 새로운 구름 생성 (이전 구름을 제외해야 하므로 set 사용)
        clouds = create_new_clouds(board, clouds, N)

    # 최종 물의 양 합계 계산
    total_water = sum(sum(row) for row in board)
    return total_water

# 입력 처리
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = [tuple(map(int, input().split())) for _ in range(M)]

# 시뮬레이션 실행
result = simulate_magic_shark(N, M, board, commands)
print(result)