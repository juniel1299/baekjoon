import sys

input = sys.stdin.readline

# 입력 처리
N, M = map(int, input().split())  # 앱 개수, 확보해야 할 메모리
memory = list(map(int, input().split()))  # 각 앱이 사용하는 메모리
cost = list(map(int, input().split()))  # 각 앱을 비활성화하는 비용

# 최대 비용 계산 (비용의 합)
max_cost = sum(cost)

# DP 배열 (0으로 초기화)
dp = [0] * (max_cost + 1)

# 배낭 문제 접근 (0/1 Knapsack)
for i in range(N):
    app_memory = memory[i]
    app_cost = cost[i]

    # **역순으로 업데이트해야 함** (0/1 Knapsack 패턴)
    for j in range(max_cost, app_cost - 1, -1):
        dp[j] = max(dp[j], dp[j - app_cost] + app_memory)

# 최소 비용 찾기 (dp[j]가 M 이상이 되는 가장 작은 j 찾기)
for j in range(max_cost + 1):
    if dp[j] >= M:
        print(j)
        break