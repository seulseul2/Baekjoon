import sys
input = sys.stdin.readline

def func(depth, x):
    if depth == N:
        if eval(x.replace(' ',''))==0:
            print(x)
        return
    x = x + ' ' + str(lst[depth])
    func(depth+1, x)
    x = x[:-2]

    x = x + '+' + str(lst[depth])
    func(depth+1, x)
    x = x[:-2]

    x = x + '-' + str(lst[depth])
    func(depth+1, x)
    x = x[:-2]

T = int(input())
for TC in range(T):
    ans = []
    N = int(input())
    lst = [x for x in range(1, N+1)]
    EXP = '1'
    func(1, EXP)