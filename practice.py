import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dp = [0] * 501
for i in range(N):
    lst = list(map(int, input().split()))
    tmp = dp[:]
    dp[0] += lst[0]
    for j in range(1, len(lst)):
        dp[j] = lst[j] + max(tmp[j-1], tmp[j])
print(max(dp))