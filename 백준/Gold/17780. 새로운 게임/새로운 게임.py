import sys

def newDirection(direction):
    if direction == 0:
        return 1
    elif direction == 1:
        return 0
    elif direction == 2:
        return 3
    else:
        return 2 

def check(x,y):
    if len(current[x][y]) >= 4:
        return True
    return False

N, K = map(int, sys.stdin.readline().split(" "))
maps = []
current = [[[] for _ in range(N)] for _ in range(N)]
pieces = []
for _ in range(N):
    maps.append(list(map(int,sys.stdin.readline().split())))
for i in range(K):
    position = tuple(map(int,sys.stdin.readline().split()))
    pieces.append([position[0]-1,position[1]-1,position[2]-1])
    current[position[0]-1][position[1]-1] = [i]

ret = 0
dirX = [0,0,-1,1]
dirY = [1,-1,0,0]



while ret <= 1000:
    flag = False

    for i,piece in enumerate(pieces):
        curX, curY, direction = piece
        if current[curX][curY][0] == i:
            nextX, nextY = curX + dirX[direction], curY + dirY[direction]
            if 0 <= nextX < N and 0 <= nextY < N:
                if maps[nextX][nextY] == 0:
                    # 흰색
                    current[nextX][nextY].extend(current[curX][curY])
                    for p in current[curX][curY]:
                        pieces[p] = [nextX,nextY,pieces[p][2]]
                    current[curX][curY] = []

                    if check(nextX,nextY):
                        flag = True
                        break

                elif maps[nextX][nextY] == 1:
                    # 빨간색
                    current[nextX][nextY].extend(current[curX][curY][::-1])
                    for p in current[curX][curY]:
                        pieces[p] = [nextX, nextY, pieces[p][2]]
                    current[curX][curY] = []

                    if check(nextX, nextY):
                        flag = True
                        break

                elif maps[nextX][nextY] == 2:
                    # 파란색
                    direction = newDirection(direction)
                    pieces[i][2] = direction

                    newNextX,newNextY = curX + dirX[direction], curY + dirY[direction]
                    if not (0 <= newNextX < N and 0 <= newNextY < N):
                        continue
                    elif maps[newNextX][newNextY] == 2:
                        continue
                    elif maps[newNextX][newNextY] == 0:
                    	# 흰색
                        current[newNextX][newNextY].extend(current[curX][curY])
                        for p in current[curX][curY]:
                            pieces[p] = [newNextX, newNextY, pieces[p][2]]
                        current[curX][curY] = []

                        if check(newNextX,newNextY):
                            flag = True
                            break
                    elif maps[newNextX][newNextY] == 1:
                    	# 빨강색
                        current[newNextX][newNextY].extend(current[curX][curY][::-1])
                        for p in current[curX][curY]:
                            pieces[p] = [newNextX, newNextY, pieces[p][2]]
                        current[curX][curY] = []

                        if check(newNextX, newNextY):
                            flag = True
                            break
            else:
                # 파란색 처리
                direction = newDirection(direction)
                pieces[i][2] = direction
                newNextX, newNextY = curX + dirX[direction], curY + dirY[direction]
                if not (0 <= newNextX < N and 0 <= newNextY < N):
                    continue
                elif maps[newNextX][newNextY] == 2:
                     continue
                elif maps[newNextX][newNextY] == 0:
                    current[newNextX][newNextY].extend(current[curX][curY])
                    for p in current[curX][curY]:
                        pieces[p] = [newNextX, newNextY, pieces[p][2]]
                    current[curX][curY] = []

                    if check(newNextX, newNextY):
                        flag = True
                        break
                elif maps[newNextX][newNextY] == 1:
                    current[newNextX][newNextY].extend(current[curX][curY][::-1])
                    for p in current[curX][curY]:
                        pieces[p] = [newNextX, newNextY, pieces[p][2]]
                    current[curX][curY] = []

                    if check(newNextX, newNextY):
                        flag = True
                        break

    ret += 1
    if flag:
        break

if ret <= 1000:
    print(ret)
else:
    print(-1)