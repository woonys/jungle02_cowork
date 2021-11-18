import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    lst = sys.stdin.readline().split()
    if len(lst) == 2: #push 2 이면 2를 lst에 삽입함
        queue.append(int(lst[1])) 
    else: # push 외 명령어
        if lst[0] == 'pop':
            if len(queue) == 0:
                print(-1)
            else:
                a = queue.popleft()
                print(a)
        elif lst[0] == 'size':
            print(len(queue))
        elif lst[0] == 'empty':
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif lst[0] =='front':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        else: 
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])
                