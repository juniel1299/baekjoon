import sys
input = sys.stdin.readline

N = int(input())
list = []
for i in range(N):
    list.append(float(input()))
    if len(list) > 7:
        list.remove(max(list))

for i in sorted(list):
    print(f'{i:.3f}')