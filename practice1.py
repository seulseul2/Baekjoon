from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dY = [-1, 1, 0, 0]
dX = [0, 0, -1, 1]

# 익은 토마토 리스트
start_lst = []
empty_box = 0
for y in range(n):
    for x in range(m):
        if box[y][x] == 1:
            start_lst.append([y, x])
        elif box[y][x] == -1:
            empty_box += 1
# print(start_lst)

# 익은 토마토가 없는 경우
if len(start_lst) == 0:
    print(-1)
# 모든 토마토가 익은 경우
elif len(start_lst) + empty_box == m*n:
    print(0)
else:
    cnt = len(start_lst) # 전체 갯수를 세 줄 녀석
    visited = [[0] * m for _ in range(n)]
    queue = deque()
    for y, x in start_lst:
        visited[y][x] = 1
        queue.append([y, x])
    while queue:
        curY, curX = queue.popleft()
        for i in range(4):
            newY = curY + dY[i]
            newX = curX + dX[i]
            if 0<=newY<n and 0<=newX<m and not visited[newY][newX] and box[newY][newX] == 0:
                cnt += 1
                queue.append([newY, newX])
                visited[newY][newX] = visited[curY][curX] + 1
                result = visited[newY][newX] - 1
    if cnt + empty_box == m*n:
        print(result)
    else:
        print(-1)