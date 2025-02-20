from collections import deque
import sys
input = sys.stdin.readline
 
dx = [1,-1,0,0]
dy = [0,0,1,-1]
 
board = [list(input().rstrip()) for _ in range(12)]
combo = 0
 
# 상하좌우로 동일한 블록들을 탐색해 해당 좌표들을 가진 리스트를 반환
def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    visited[x][y] = True
 
    same_blocks = [(x, y)] # 동일한 블록의 좌표를 담을 리스트
 
    while q:
        x, y = q.popleft()
 
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
 
            if 0 <= nx < 12 and 0 <= ny < 6 and board[x][y] == board[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                same_blocks.append((nx, ny))
    return same_blocks
 
# 동일한 블록들을 제거
def delete(same_blocks):
    for x, y in same_blocks:
        board[x][y] = "."
 
# 역순으로 반복문을 돌며 위에서 아래로 블록을 내림
def down():
    for y in range(6):
        for x in range(10, -1, -1):
            for k in range(11, x, -1):
                if board[x][y] != "." and board[k][y] == ".":
                    board[k][y] = board[x][y]
                    board[x][y] = "."
 
while True:
    pang = False
    visited = [[False] * 6 for _ in range(12)]
 
    for x in range(12):
        for y in range(6):
            if board[x][y] != "." and not visited[x][y]:
                same_blocks = bfs(x, y)
 
                # 동일한 블록이 4개이상일 경우 블록을 터트린다.
                if len(same_blocks) >= 4:
                    pang = True
                    delete(same_blocks)
 
    # 터트릴 블록이 있다면, 블록을 터트리고 터트린 블록을 밑으로 내린다.
    if pang:
        down()
        combo += 1
    else:
        break
 
print(combo)