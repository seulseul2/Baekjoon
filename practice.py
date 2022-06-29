import sys
input = sys.stdin.readline

cRoom = [list(input().rstrip()) for _ in range(5)]
dY = [0, 0, -1, 1]
dX = [-1, 1, 0, 0]
ans = set()

def btrk(Y):
    if Y >= 4:
        return
    if len(lst) == 7:
        tmp = sorted(lst)
        ans.add(tuple(tmp))
        return
    for each in lst:
        for i in range(4):
            nY = each[0] + dY[i]
            nX = each[1] + dX[i]
            if 0<=nY<5 and 0<=nX<5 and (nY, nX) not in lst:
                lst.append((nY, nX))
                if cRoom[nY][nX] == 'Y':
                    btrk(Y+1)
                else:
                    btrk(Y)
                lst.pop()

for y in range(5):
    for x in range(5):
        if cRoom[y][x] == 'S':
            lst = [(y, x)]
            btrk(0)

print(len(ans))