import sys
input = sys.stdin.readline
from itertools import combinations

N,K =map(int,input().split()) # 마라탕 재료 수, 고를 재료 수

req=[]
result=[]

for i in range(0,N) :
    req.append(list(map(int,input().split())))
    
for c in combinations([i for i in range(N)], K):
    sum = 0
    
    for c2 in combinations(c,2):
        sum+=req[c2[0]][c2[1]] # 궁합에 대한걸 계속 더해야 함
        
    result.append(sum)
    
    
print(max(result))