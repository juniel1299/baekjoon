N,M = map(int,input().split()) # 문제 기준 N과 M 

basket = [i for i in range (1,N+1)]

temp = 0

for _ in range (M):
    i,j = map(int,input().split())
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp


for i in range (N):
    print(basket[i], end = ' ')