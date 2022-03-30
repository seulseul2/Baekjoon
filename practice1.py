import sys
input = sys.stdin.readline

dY = [0, 0, -1, 1]
dX = [-1, 1, 0, 0]

def dfs(y, x):
    global visited
    stack = [[y, x]]
    visited[y][x] = True
    while stack:
        curY, curX = stack.pop()
        for j in range(4):
            newY = curY + dY[j]
            newX = curX + dX[j]
            if 0<=newX<n and 0<=newY<n and not visited[newY][newX] and area[newY][newX] > k:
                stack.append([newY, newX])
                visited[newY][newX] = True


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

# 높이최댓값 구하기
maxV = 0
for i in range(n):
    x = max(area[i])
    if x > maxV:
        maxV = x

max_area = 0
for k in range(maxV):
    cnt = 0
    visited = [[False]*n for _ in range(n)]
    for q in range(n):
        for p in range(n):
            if area[q][p] > k and not visited[q][p]:
                dfs(q, p)
                cnt += 1
    if cnt > max_area:
        max_area = cnt
print(max_area)
