bucket,gong = map(int,input().split()) # 문제 기준 N과 M 

basket = [0 for _ in range(bucket)]

for _ in range(gong):
    i,j,k = map(int,input().split()) 
    for n in range(i,j+1):
        basket[n-1] = k         #  문제는 1번부터인데 list 의 index는 0부터 시작하기 때문에 -1 

for n in range(bucket):
    print(basket[n], end=' ') # 띄어쓰기를 위해 end 사용 > 숫자 사이사이 스페이스바 