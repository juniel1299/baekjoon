import sys

input = sys.stdin.readline

# N: 세로선 개수, M: 기존 가로선 개수, H: 가로선을 놓을 수 있는 행 개수
N, M, H = map(int, input().split())

# 사다리 배열 초기화
ladder = [[0] * N for _ in range(H)]

# 기존 가로선 추가
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a - 1][b - 1] = 1  # b번 세로선과 b+1번 세로선을 잇는 가로선

# 현재 상태에서 i번 세로선이 i번으로 가는지 확인하는 함수
def check():
    for start in range(N):
        k = start
        for j in range(H):
            if ladder[j][k] == 1:
                k += 1  # 오른쪽 이동
            elif k > 0 and ladder[j][k - 1] == 1:
                k -= 1  # 왼쪽 이동
        if k != start:
            return False
    return True

# 백트래킹 (DFS) 방식으로 가로선을 추가하며 최소 개수를 찾음
def dfs(count, x, y):
    global min_steps

    # 현재 최소 개수보다 많아지면 종료
    if count >= min_steps:
        return

    # 모든 세로선이 자기 자신으로 가는지 확인
    if check():
        min_steps = count
        return

    # 가로선은 최대 3개까지만 추가 가능
    if count == 3:
        return

    # 가능한 위치에 가로선을 추가
    for i in range(x, H):
        start_y = y if i == x else 0
        for j in range(start_y, N - 1):
            # 가로선이 존재하지 않는 경우만 추가
            if ladder[i][j] == 0 and ladder[i][j + 1] == 0:
                # 가로선 추가
                ladder[i][j] = 1
                dfs(count + 1, i, j + 2)  # 연속 가로선 방지를 위해 j+2부터 탐색
                # 원래 상태로 복구
                ladder[i][j] = 0

# 정답 초기화 (최대 3개 추가 가능)
min_steps = 4

# DFS 탐색 시작
dfs(0, 0, 0)

# 정답 출력
print(min_steps if min_steps < 4 else -1)