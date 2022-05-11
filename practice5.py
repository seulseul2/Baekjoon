import sys
input = sys.stdin.readline

N, C = map(int, input().split())
lst = []
for i in range(N):
    lst.append(int(input()))
lst.sort()

start = 1
end = lst[N-1] - lst[0]

while start <= end:
    middle = (start+end) // 2
    now = lst[0]
    cnt = 1

    for i in range(1, N):
        if lst[i] >= now + middle:
            cnt += 1
            now = lst[i]
    
    if cnt >= C:
        start = middle + 1
        ans = middle
    else:
        end = middle -1

print(ans)        