import sys

input = sys.stdin.readline

# 테트로미노의 19가지 모양 (회전 + 대칭 포함)
tetrominoes = [
    # ㅡ 자형
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],

    # ㅁ 자형
    [(0, 0), (0, 1), (1, 0), (1, 1)],

    # L 자형
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 1), (1, 1), (2, 1), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (0, 1)],
    [(0, 2), (1, 0), (1, 1), (1, 2)],

    # Z 자형
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (0, 1), (0, 2)],
    [(0, 1), (1, 0), (1, 1), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],

    # ㅗ 자형
    [(0, 1), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 1), (1, 0), (1, 1), (2, 1)]
]

def is_valid(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

def find_max_tetromino_sum(board, N, M):
    max_sum = 0

    # 모든 좌표에서 테트로미노 배치 시도
    for i in range(N):
        for j in range(M):
            for shape in tetrominoes:
                total = 0
                valid = True
                for dx, dy in shape:
                    nx, ny = i + dx, j + dy
                    if is_valid(nx, ny, N, M):
                        total += board[nx][ny]
                    else:
                        valid = False
                        break
                if valid:
                    max_sum = max(max_sum, total)

    return max_sum

# 입력 처리
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 결과 계산
result = find_max_tetromino_sum(board, N, M)
print(result)