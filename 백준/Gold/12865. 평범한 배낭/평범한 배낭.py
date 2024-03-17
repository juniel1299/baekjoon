# 백준 baek12865 문제 , 평범한 베낭
# https://www.acmicpc.net/problem/12865 , 골드 5  
# 냅색 알고리즘  (베낭 문제)
n, k = map(int, input().split()) # 입력 (물건 수 n , 무게 k)

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)] 

for i in range(n): # 물건 수 만큼 반복해서 배열 늘림 . 
    thing.append(list(map(int, input().split()))) 

for i in range(1, n+1): 
    for j in range(1, k+1):
        w = thing[i][0] # 각 물건의 무게 
        v = thing[i][1] # 각 물건의 가치

        if j < w: # 각 물건의 무게가 더 클 경우  
            d[i][j] = d[i-1][j]
        else: # 전체 무게가 더 클 경우 
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k]) # 최종 결과 
