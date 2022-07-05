import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    else:
        root_x = find(parent[x])
        parent[x] = root_x
        return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x
        number[root_x] += number[root_y]

T = int(input())
for TC in range(T):
    parent = dict()
    number = dict()

    F = int(input())
    for _ in range(F):
        A, B = input().rstrip().split()
        
        if A not in parent:
            parent[A] = A
            number[A] = 1
        if B not in parent:
            parent[B] = B
            number[B] = 1
        
        union(A, B)
        print(number[find(A)])