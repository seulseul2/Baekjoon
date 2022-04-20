import sys
input = sys.stdin.readline

N = int(input())
budget = list(map(int, input().split()))
total = int(input())

end = max(budget)
start = 1

while start <= end:
    tmp = 0
    middle = (start+end)//2
    for i in budget:
        if i >= middle:
            tmp += middle
        else:
            tmp += i
        if tmp > total:
            end = middle - 1
            break
    else:
        start = middle + 1
print(end)