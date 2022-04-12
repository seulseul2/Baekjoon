import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)
day = []
profit = []
for i in range(1, N+1):
    D, P = map(int, input().split())
    day.append(D)
    profit.append(P)

for j in range(N-1, -1, -1):
    if day[j] + j > N:
        dp[j] = dp[j+1]
    else:
        dp[j] = max(profit[j] + dp[j+day[j]], dp[j+1])
print(dp[0])