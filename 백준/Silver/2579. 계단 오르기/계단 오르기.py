# 다이나믹 프로그래밍 문제 
# 백준 2579번 , https://www.acmicpc.net/problem/2579
N = int(input())
# dp에 사용할 배열과 각 계단에 저장할 값을 선언
dp = [0] * (N+1)
point = [0] * (N+1)
for i in range(1, N+1):
    point[i] = int(input())
if N==1:
    print(point[1])
    exit()
elif N==2:
    print(sum(point[:3]))
    exit()
dp[1] = point[1]
dp[2] = point[1]+point[2]
for i in range(3, N+1):
    dp[i] = max(dp[i-2]+point[i], dp[i-3]+point[i-1]+point[i])

print(dp[-1])