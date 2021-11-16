from sys import stdin
from collections import deque

n = int(stdin.readline())
queue = deque()

for i in range(n):
    li = stdin.readline().split()
    if len(li) == 2:
        queue.append(int(li[1]))
    else:
        if li[0] == 'pop':
            if len(queue) == 0:
                print(-1)
            else:
                a = queue.popleft()
                print(a)
        elif li[0] == "size":
            print(len(queue))
        elif li[0] == "empty":
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif li[0] == 'front':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        else:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])