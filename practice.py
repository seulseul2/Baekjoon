from collections import deque
import sys
input = sys.stdin.readline

def bfs(n):
    visited = [0] * (N+1)
    queue = deque()
    queue.append(n)
    total = 0
    visited[n] = 1

    while queue:
        start = queue.popleft()
        for j in FRNS[start]:
            if not visited[j]:
                queue.append(j)
                visited[j] = visited[start] + 1
                total += visited[j] - 1
    return total


N, M = map(int, input().split())
FRNS = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    FRNS[a].append(b)
    FRNS[b].append(a)

print(FRNS)

result = 1e10
result_no = 1e10
for j in range(N, 0, -1):
    if bfs(j) <= result:
        result = bfs(j)
        result_no = j
print(result_no)