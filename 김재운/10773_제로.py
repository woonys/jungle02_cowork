from sys import stdin

k = int(stdin.readline())
stack = list()
for i in range(k):
    a = int(stdin.readline())
    if a !=0:
        stack.append(a)
    else:
        stack.pop()
if len(stack) == 0:
    print(0)
else:
    print(sum(stack))