import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    queue.append(i+1)
    
while len(queue) > 1: #1장 남을 때 까지 ( [4, 2] 남을 때 까지)
    queue.popleft() # 맨 앞 버리기 [1, 2, 3, 4, 5] -> [2, 3, 4, 5]
    queue.append(queue.popleft()) # 맨 앞을 맨 뒤에 넣기 [3, 4, 5, 2]
    
print(queue.pop())