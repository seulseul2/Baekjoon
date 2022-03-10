import sys
input = sys.stdin.readline

N, P = map(int, input().split())

stack = [[] for _ in range(6)]
cnt = 0
for i in range(N):
    s, f = map(int, input().split())
    if stack[s-1]:
        while stack[s-1] and stack[s-1][-1] > f:
            stack[s-1].pop()
            cnt += 1
        if stack[s-1]:
            if stack[s-1][-1] < f:
                stack[s-1].append(f)
                cnt += 1
        else:
            stack[s-1].append(f)
            cnt += 1
    else:
        stack[s-1].append(f)
        cnt += 1
print(cnt)