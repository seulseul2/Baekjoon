from re import A


n = int(input())
a = 300
b = 60
c = 10

A = n // a
B = (n-A*a) // b
C = (n-(A*a)-(B*b)) // c

if A*a + B*b + C*c == n:
    print(A, B, C)
else:
    print(-1)