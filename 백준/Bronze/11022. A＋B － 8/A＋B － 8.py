num = int(input()) # 숫자

for i in range(1, num+1):
    a, b = map(int,input().split()) # 더하기 숫자
    print(f"Case #{i}: {a} + {b} = {a+b}")

