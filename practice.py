import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
Dp = lst[:]

for i in range(1,N):
    for j in range(i):
        if lst[j] < lst[i]:
            Dp[i] = max(Dp[i], Dp[j] + lst[i])
print(max(Dp))