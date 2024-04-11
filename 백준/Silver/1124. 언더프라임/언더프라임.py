input = __import__('sys').stdin.readline
import math
 
def find(n):
    cnt=0
    for i in range(2, int(math.sqrt(n) + 1)):
        while n % i == 0:
            cnt+=1
            n //= i
    if n != 1:
        cnt+=1
    return cnt
 
 
a,b = map(int,input().split())
is_prime = [True for i in range(b + 1)]
 
is_prime[1] = False
for i in range(2, b + 1):
    if not is_prime[i]:
        continue
    
    for j in range(i * i, b + 1, i):
        is_prime[j] = False
cnt=0
for i in range(a,b+1):
    if is_prime[find(i)] == True:
        cnt+=1
print(cnt)