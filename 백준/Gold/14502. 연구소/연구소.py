import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs():

    for i in combinations(blank, 3):
        queue = deque()
        trial = copy.deepcopy(grid)

        for y, x in i:
            trial[y][x] = 1

        for i in range(len(virus)):
            queue.append(virus[i])

        while queue:
            y, x = queue.popleft()

            for i in range(4):
                ny = dy[i] + y
                nx = dx[i] + x

                if ny <= -1 or ny >= n or nx <= -1 or nx >= m:
                    continue
                if trial[ny][nx] == 0:
                    trial[ny][nx] = 2
                    queue.append([ny, nx])

        global safe
        safe_current = 0

        for i in range(n):
            safe_current += trial[i].count(0)

        safe = max(safe, safe_current)


n, m = map(int, input().split())
grid = []
virus = []
blank = []
safe = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    grid.append(list(map(int, input().split())))

for y in range(n):
    for x in range(m):
        if grid[y][x] == 2:
            virus.append([y, x])
        if grid[y][x] == 0:
            blank.append([y, x])

bfs()
print(safe)