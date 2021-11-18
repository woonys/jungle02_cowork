from sys import stdin

n = int(stdin.readline())

stack = [int(stdin.readline()) for _ in range(n)]

count = 1
k = stack.pop()
while len(stack) > 0:
    if stack[-1] <= k:
        stack.pop()
    else:
        count += 1
        k = stack.pop()

print(count)