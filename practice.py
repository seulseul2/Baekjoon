from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
INF = 100001

q = deque([N])
cnt = 0
visited = [-1] * INF
visited[N] = 0

while q:
    now = q.popleft()
    if now==K:
        cnt+=1
    for next in [now*2, now+1, now-1]:
        if 0<=next<INF:
            if visited[next]==-1 or visited[next]>=visited[now]+1: #시간: 방문한 적 없거나 현재시간 +1인경우
                visited[next]=visited[now]+1
                q.append(next)

print(visited[K])
print(cnt)