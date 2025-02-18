def rotate_face_clockwise(face):
    return [list(row) for row in zip(*face[::-1])]

def rotate_face_counterclockwise(face):
    return [list(row) for row in zip(*face)][::-1]

def rotate(cube, face, direction):
    if direction == '+':
        cube[face] = rotate_face_clockwise(cube[face])
    else:
        cube[face] = rotate_face_counterclockwise(cube[face])

    # 측면 회전 처리
    if face == 'U':
        if direction == '+':
            temp = cube['B'][0][:]
            cube['B'][0] = cube['L'][0]
            cube['L'][0] = cube['F'][0]
            cube['F'][0] = cube['R'][0]
            cube['R'][0] = temp
        else:
            temp = cube['B'][0][:]
            cube['B'][0] = cube['R'][0]
            cube['R'][0] = cube['F'][0]
            cube['F'][0] = cube['L'][0]
            cube['L'][0] = temp

    elif face == 'D':
        if direction == '+':
            temp = cube['F'][2][:]
            cube['F'][2] = cube['L'][2]
            cube['L'][2] = cube['B'][2]
            cube['B'][2] = cube['R'][2]
            cube['R'][2] = temp
        else:
            temp = cube['F'][2][:]
            cube['F'][2] = cube['R'][2]
            cube['R'][2] = cube['B'][2]
            cube['B'][2] = cube['L'][2]
            cube['L'][2] = temp

    elif face == 'F':
        if direction == '+':
            temp = [cube['U'][2][i] for i in range(3)]
            for i in range(3):
                cube['U'][2][i] = cube['L'][2 - i][2]
                cube['L'][2 - i][2] = cube['D'][0][2 - i]
                cube['D'][0][2 - i] = cube['R'][i][0]
                cube['R'][i][0] = temp[i]
        else:
            temp = [cube['U'][2][i] for i in range(3)]
            for i in range(3):
                cube['U'][2][i] = cube['R'][i][0]
                cube['R'][i][0] = cube['D'][0][2 - i]
                cube['D'][0][2 - i] = cube['L'][2 - i][2]
                cube['L'][2 - i][2] = temp[i]

    elif face == 'B':
        if direction == '+':
            temp = [cube['U'][0][i] for i in range(3)]
            for i in range(3):
                cube['U'][0][i] = cube['R'][i][2]
                cube['R'][i][2] = cube['D'][2][2 - i]
                cube['D'][2][2 - i] = cube['L'][2 - i][0]
                cube['L'][2 - i][0] = temp[i]
        else:
            temp = [cube['U'][0][i] for i in range(3)]
            for i in range(3):
                cube['U'][0][i] = cube['L'][2 - i][0]
                cube['L'][2 - i][0] = cube['D'][2][2 - i]
                cube['D'][2][2 - i] = cube['R'][i][2]
                cube['R'][i][2] = temp[i]

    elif face == 'L':
        if direction == '+':
            temp = [cube['U'][i][0] for i in range(3)]
            for i in range(3):
                cube['U'][i][0] = cube['B'][2 - i][2]
                cube['B'][2 - i][2] = cube['D'][i][0]
                cube['D'][i][0] = cube['F'][i][0]
                cube['F'][i][0] = temp[i]
        else:
            temp = [cube['U'][i][0] for i in range(3)]
            for i in range(3):
                cube['U'][i][0] = cube['F'][i][0]
                cube['F'][i][0] = cube['D'][i][0]
                cube['D'][i][0] = cube['B'][2 - i][2]
                cube['B'][2 - i][2] = temp[i]

    elif face == 'R':
        if direction == '+':
            temp = [cube['U'][i][2] for i in range(3)]
            for i in range(3):
                cube['U'][i][2] = cube['F'][i][2]
                cube['F'][i][2] = cube['D'][i][2]
                cube['D'][i][2] = cube['B'][2 - i][0]
                cube['B'][2 - i][0] = temp[i]
        else:
            temp = [cube['U'][i][2] for i in range(3)]
            for i in range(3):
                cube['U'][i][2] = cube['B'][2 - i][0]
                cube['B'][2 - i][0] = cube['D'][i][2]
                cube['D'][i][2] = cube['F'][i][2]
                cube['F'][i][2] = temp[i]


def print_upper_face(cube):
    """윗면 출력"""
    for row in cube['U']:
        print(''.join(row))


def solve_rubiks_cube():
    """메인 함수"""
    t = int(input())
    for _ in range(t):
        # 매 테스트 케이스마다 큐브 새로 생성
        cube = {
            'U': [['w'] * 3 for _ in range(3)],
            'D': [['y'] * 3 for _ in range(3)],
            'F': [['r'] * 3 for _ in range(3)],
            'B': [['o'] * 3 for _ in range(3)],
            'L': [['g'] * 3 for _ in range(3)],
            'R': [['b'] * 3 for _ in range(3)]
        }

        # 명령 입력받아 처리
        n = int(input())
        moves = input().split()

        for move in moves:
            rotate(cube, move[0], move[1])

        print_upper_face(cube)


# 프로그램 실행
solve_rubiks_cube()