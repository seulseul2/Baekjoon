import sys
input = sys.stdin.readline

C = int(input())
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)

B = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

time = 0

if cranes[0] < boxes[0]:
    print(-1)
else:
    while boxes:
        if not boxes:
            break
        for crane in cranes:
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        time += 1
    print(time)