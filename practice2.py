import heapq
import sys
input = sys.stdin.readline

N = int(input())
ptree = []
mtree = []
for i in range(N):
    x = int(input())
    if x < 0:
        heapq.heappush(mtree, abs(x))
    elif x > 0:
        heapq.heappush(ptree, x)
    else:
        if not mtree and not ptree:
            print(0)
            continue
        if mtree and not ptree:
            print(-1 * heapq.heappop(mtree))
            continue
        if ptree and not mtree:
            print(heapq.heappop(ptree))
            continue
        if mtree[0] <= ptree[0]:
            print(-1 * heapq.heappop(mtree))
        else:
            print(heapq.heappop(ptree))