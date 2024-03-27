import sys
input = sys.stdin.readline
DIVIDER = 1000000007

n = int(input())
inputString = input().rstrip()

dp = [0, 0, 0, 0]

for i in range(n-1, -1, -1):
    dp[3] = 2*dp[3]%DIVIDER
    
    if inputString[i] == "K": dp[0] = (dp[0]+1)%DIVIDER
    elif inputString[i] == "C": dp[1] = (dp[1]+dp[0])%DIVIDER
    elif inputString[i] == "O": dp[2] = (dp[2]+dp[1])%DIVIDER
    elif inputString[i] == "R": dp[3] = (dp[3]+dp[2])%DIVIDER
    
print(dp[3]%DIVIDER)