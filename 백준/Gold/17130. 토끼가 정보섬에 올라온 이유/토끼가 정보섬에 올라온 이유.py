import sys

input = sys.stdin.readline
MIISS = lambda: map(int, input().strip().split())
directions = [(0, -1), (1, -1), (-1, -1)]

N, M = MIISS()
arr = list(input().strip() for _ in range(N))
dp = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]


# 토끼가 들어온 위치 찾는 로직 (부르트포스 이용 (난 더 못 줄인다 음음 .. ))
def rabbit_start():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'R':
                return (i, j)


ri, rj = rabbit_start()
side_door = []
visited[ri][rj] = True

for j in range(rj + 1, M): # 토끼는 왼쪽으로 안 움직이니까 왼쪽으로 나가는 경우의 수는 없다 . 
    for i in range(N):
        if arr[i][j] == '#':
            continue  # 벽이면 반복 종료 

        # 도착점에 도착할 때 당근을 제일 많이 얻을 수 있는 경우에 대한 당근 값 
        most_carrot = 0
        flag = False # 당근을 다 챙겨 나올 수 있는지 확인

        for ki, kj in directions:
            ni, nj = i + ki, j + kj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj]:  # 도착점 도착이 가능한지에 대한 3가지 - 방문했는지에 대해 다 체크해야함 모두 벽이면 그냥 종료 
                most_carrot = max(most_carrot, dp[ni][nj])
                flag = True

        if flag == False: # 모두 벽인 경우
            continue

        visited[i][j] = True # 도착점에 갈 수 있는 경우

        if arr[i][j] == 'C':
            dp[i][j] = most_carrot + 1

        elif arr[i][j] == '.':
            dp[i][j] = most_carrot

        elif arr[i][j] == 'O':
            if most_carrot == -1:  # 도착 실패 시에 
                continue
            dp[i][j] = most_carrot
            side_door.append(most_carrot)

# 쪽문 탈출 성공
if side_door:
    print(max(side_door))
else:  # 쪽문 탈출 실패
    print(-1)