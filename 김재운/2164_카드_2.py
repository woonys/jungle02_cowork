from sys import stdin
from collections import deque

n = int(stdin.readline())
cards = deque()

for i in range(1, n+1):
    cards.append(i)

while len(cards) != 1:
    cards.popleft()
    a = cards.popleft()
    cards.append(a)

print(cards[0])