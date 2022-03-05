N, K = map(int, input().split())

cost = 0
lst = list(map(int, input().split()))

idx = 0
if N % K:
    group = N//K + 1
    while idx + group < N:
        cost += lst[idx+group-1] - lst[idx]
        idx += group
    cost += lst[-1]-lst[idx]

else:
    group = N//K
    while idx + group <= N:
        cost += lst[idx+group-1] - lst[idx]
        idx += group
        
print(cost)