import sys

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N = int(input())

student_len = N*N
board = [[0 for _ in range(N)] for _ in range(N)]

# [학생 번호, 좋아하는 친구들] 입력
students = []
for _ in range(student_len):
    students.append(list(map(int, sys.stdin.readline().split())))

# 학생을 차례로 꺼내면서 자리 지정
for student in students:
    number = student[0] # 현재 학생 번호
    able_position = [] # 현재 학생이 앉을 수 있는 자리를 넣을 리스트
    # 교실 모든 자리를 탐색
    for i in range(N):
        for j in range(N):
            # 현재 자리가 비어있다면
            if board[i][j] == 0:
                like = 0 # 현재 자리의 선호 점수
                blank = 0 # 현재 자리 주위에 있는 빈 자리 개수
                # 4방향 탐색
                for t in range(4):
                    nx = i + dx[t]
                    ny = j + dy[t]
                    # 범위 체크
                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue
                    # 탐색한 위치에 현재 학생이 선호하는 친구가 있다면
                    if board[nx][ny] in student[1:]:
                        # 선호 점수 += 1
                        like += 1
                    # 탐색한 위치가 빈 자리라면
                    if board[nx][ny] == 0:
                        # 빈 자리 개수 += 1
                        blank += 1
                # 현재 학생이 앉을 수 있는 자리 리스트에 저장
                able_position.append([like, blank, i, j])
    # 현재 학생이 앉을 수 있는 자리를 (like, blank)는 내림차순으로, (좌표)는 오름차순으로 정렬
    able_position.sort(key=lambda x:(-x[0], -x[1], x[2], [3]))
    # 조건의 우선 순위가 가장 높은 위치에 해당 학생을 앉힘
    board[able_position[0][2]][able_position[0][3]] = number

# 학생들의 행복도 조사
happy = 0 # 출력할 행복도
students.sort() # 학생들의 번호에 맞춰서 탐색하기 위해 학생 번호를 기준으로 정렬

# 모든 자리를 탐색하며 해당 자리에 앚아있는 학생을 기준으로 행복도 조사
for i in range(N):
    for j in range(N):
        like_cnt = 0 # 현재 자리에 앉아 있는 학생의 행복도
        num = board[i][j] # 현재 자리에 앉아 있는 학생의 번호
        # 현재 자리에서 4방향 탐색
        for t in range(4):
            nx = i + dx[t]
            ny = j + dy[t]
            # 범위 체크
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            # 탐색한 자리에 앉아 있는 학생이 현재 자리에 앉아 있는 학생이 선호하는 학생이라면
            if board[nx][ny] in students[num-1][1:]:
                like_cnt += 1 # 현재 자리에 앉아 있는 학생의 행복도 += 1
        # 행복도가 0이 아니라면
        if like_cnt != 0:
            # 10의 지수로 계산
            happy += (10 ** (like_cnt - 1))

print(happy)