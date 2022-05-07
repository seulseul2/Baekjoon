import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(s):
    global cnt
    queue = []
    heapq.heappush(queue, [0, s])
    seconds[s] = 0
    while queue:
        sec, now = heapq.heappop(queue)
        if seconds[now] < sec:
            continue
        for i in graph[now]:
            Nsec = sec + i[1]
            if Nsec < seconds[i[0]]:
                if seconds[i[0]] == INF:
                    cnt += 1
                seconds[i[0]] = Nsec
                heapq.heappush(queue, [Nsec, i[0]])

T = int(input())
for TC in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    seconds = [INF] * (n+1)
    for i in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])
    cnt = 1
    dijkstra(c)
    maxV = 0
    for j in seconds:
        if j == INF:
            continue
        maxV = max(maxV, j)
    print(cnt, maxV)