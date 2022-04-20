from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]
for i in range(M):
    p, q = map(int, input().split())
    lst[p].append(q)
    lst[q].append(p)

def bfs(n):
    visited = [0] * (N+1)
    visited[n] = 1
    queue = deque()
    queue.append(n)
    while queue:
        s = queue.popleft()
        if s == b:
            return visited[s]-1 
        for j in lst[s]:
            if not visited[j]:
                visited[j] = visited[s] + 1
                queue.append(j)
    return -1

print(bfs(a))