import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 방향 설정: 북(0), 동(1), 남(2), 서(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방문 여부를 확인하기 위한 배열
visited = [[False] * M for _ in range(N)]
visited[r][c] = True  # 현재 위치 청소
cleaned_count = 1  # 청소한 칸의 수

while True:
    cleaned = False
    for _ in range(4):
        # 왼쪽 방향으로 회전
        d = (d + 3) % 4
        nx = r + dx[d]
        ny = c + dy[d]
        # 청소되지 않은 빈 칸이 존재한다면
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and room[nx][ny] == 0:
            visited[nx][ny] = True
            cleaned_count += 1
            r, c = nx, ny
            cleaned = True
            break
    if not cleaned:
        # 후진할 위치
        nx = r - dx[d]
        ny = c - dy[d]
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            r, c = nx, ny
        else:
            break

print(cleaned_count)