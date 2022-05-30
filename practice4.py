import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

minV = 2000000001
left, right = 0, N-1

while left < right:
    tmp = liquid[left]+liquid[right]
    if abs(tmp) < minV:
        a = liquid[left]
        b = liquid[right]
        minV = abs(tmp)
        if minV == 0:
            break
    if tmp > 0:
        right -= 1
    else:
        left += 1
print(a, b)