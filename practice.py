import sys
input = sys.stdin.readline

def find(x):
    for j in range(len(x)-1):
        if x[j] == x[j+1][:len(x[j])]:
            print('NO')
            return
    print('YES')
    return
            
T = int(input())
for TC in range(T):
    ans = 'YES'
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(input().rstrip())
    lst.sort()
    find(lst)