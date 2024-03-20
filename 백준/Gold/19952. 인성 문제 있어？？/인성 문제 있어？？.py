from collections import deque

class Car:
    def __init__(self, x, y, energy):
        self.x = x
        self.y = y
        self.energy = energy

def bfs():
    global result
    visit = [[False] * (w+1) for _ in range(h+1)]
    q = deque()
    q.append(Car(xs, ys, f))
    visit[xs][ys] = True
    
    while q:
        next_car = q.popleft()
        if next_car.x == xf and next_car.y == yf:
            result = 1
            return
        
        for dx, dy in dir:
            x1 = next_car.x + dx
            y1 = next_car.y + dy
            if x1 <= 0 or x1 > h or y1 <= 0 or y1 > w or visit[x1][y1] or \
               elevation_map[x1][y1] - elevation_map[next_car.x][next_car.y] > next_car.energy or next_car.energy == 0:
                continue
            
            visit[x1][y1] = True
            q.append(Car(x1, y1, next_car.energy - 1))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        result = 0
        h, w, o, f, xs, ys, xf, yf = map(int, input().split())
        elevation_map = [[0] * (w+1) for _ in range(h+1)]
        
        for _ in range(o):
            x, y, height = map(int, input().split())
            elevation_map[x][y] = height
        
        dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        bfs()
        
        if result == 0:
            print("인성 문제있어??")
        else:
            print("잘했어!!")
