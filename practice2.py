import sys
input = sys.stdin.readline

n = int(input())
count = 0
stack = []
result = ''
Flag = 1

for i in range(n):
    x = int(input())

    while count < x:
      count += 1
      stack.append(count)
      result += '+'

    if stack[-1]==x:
        stack.pop()
        result += "-"
    else:
        Flag = 0

if Flag:
    for j in result:
        print(j)
else:
    print("NO")