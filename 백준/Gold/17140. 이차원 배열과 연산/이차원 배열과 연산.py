from collections import Counter

def operate(matrix):
    max_len = 0
    new_matrix = []
    for row in matrix:
        count = Counter(row)
        if count.get(0):
            del count[0]
        sorted_items = sorted(count.items(), key=lambda x: (x[1], x[0]))
        new_row = []
        for num, freq in sorted_items:
            new_row.extend([num, freq])
        max_len = max(max_len, len(new_row))
        new_matrix.append(new_row)
    for row in new_matrix:
        row.extend([0] * (max_len - len(row)))
    return new_matrix

def transpose(matrix):
    return list(map(list, zip(*matrix)))

def solution():
    r, c, k = map(int, input().split())
    r -= 1
    c -= 1
    A = [list(map(int, input().split())) for _ in range(3)]
    
    time = 0
    while time <= 100:
        if r < len(A) and c < len(A[0]) and A[r][c] == k:
            print(time)
            return
        if len(A) >= len(A[0]):
            A = operate(A)
        else:
            A = transpose(A)
            A = operate(A)
            A = transpose(A)
        time += 1
    print(-1)

solution()