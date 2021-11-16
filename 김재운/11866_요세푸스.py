from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())

circle = deque(range(1, n+1))
y = list()
while len(circle) >0:
    for i in range(k):
        if i == k-1:
            y.append(circle.popleft())
        else:
            circle.append(circle.popleft())

a = "".join(str(y))
a = a[1:-1]

print("<"+a+">")

