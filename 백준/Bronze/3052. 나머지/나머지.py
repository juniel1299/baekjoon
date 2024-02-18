num = []

for _ in range (10):
    Su = int(input())
    mod = Su % 42
    num.append(mod)

same = set(num) # 중복 제거

print(len(same)) # 중복 제거한거 출력 
