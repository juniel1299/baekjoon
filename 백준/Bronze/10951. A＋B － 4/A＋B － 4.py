while True:
    try:
        a, b = map(int,input().split()) # 더하기 숫자
    except:
        break
    print(f"{a+b}")
