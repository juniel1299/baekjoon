from collections import deque

# 방향 벡터 (상, 하, 좌, 우)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def rotate_and_melt(board, L, N):
    size = 2 ** L
    new_board = [[0] * N for _ in range(N)]
    
    # 부분 격자 회전
    for y in range(0, N, size):
        for x in range(0, N, size):
            for i in range(size):
                for j in range(size):
                    new_board[y + j][x + size - 1 - i] = board[y + i][x + j]
    
    # 얼음 감소 처리
    melt_list = []
    for y in range(N):
        for x in range(N):
            if new_board[y][x] == 0:
                continue
            ice_count = 0
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < N and 0 <= nx < N and new_board[ny][nx] > 0:
                    ice_count += 1
            if ice_count < 3:
                melt_list.append((y, x))
    
    for y, x in melt_list:
        new_board[y][x] -= 1
    
    return new_board

def bfs(board, y, x, N, visited):
    queue = deque([(y, x)])
    visited[y][x] = True
    count = 1
    
    while queue:
        cy, cx = queue.popleft()
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and board[ny][nx] > 0:
                visited[ny][nx] = True
                queue.append((ny, nx))
                count += 1
    
    return count

def main():
    import sys
    input = sys.stdin.readline
    
    N, Q = map(int, input().split())
    size = 2 ** N
    board = [list(map(int, input().split())) for _ in range(size)]
    L_list = list(map(int, input().split()))
    
    for L in L_list:
        board = rotate_and_melt(board, L, size)
    
    # 남아있는 얼음의 총 합
    total_ice = sum(sum(row) for row in board)
    
    # 가장 큰 얼음 덩어리 찾기
    visited = [[False] * size for _ in range(size)]
    max_chunk = 0
    for y in range(size):
        for x in range(size):
            if board[y][x] > 0 and not visited[y][x]:
                max_chunk = max(max_chunk, bfs(board, y, x, size, visited))
    
    print(total_ice)
    print(max_chunk)

if __name__ == "__main__":
    main()