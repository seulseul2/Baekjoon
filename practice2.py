import sys
input = sys.stdin.readline

N = int(input())
weight_lst = list(map(int, input().split()))
weight_lst.sort()

ans = 1

for weight in weight_lst:
    if ans < weight:
        break

    ans += weight

print(ans)