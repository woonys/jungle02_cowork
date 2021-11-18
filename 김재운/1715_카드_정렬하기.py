# from sys import stdin
# import heapq
#
# n = int(stdin.readline())
# cards = list()
# for i in range(n):
#     card = int(stdin.readline())
#     heapq.heappush(cards, card)
#
# sum = heapq.heappop(cards) # a1 값 미리 뺴옴
# print(sum)
# for i in range(n-1):
#     k = (heapq.heappop(cards))
#     print(k)
#     sum += (n-1-i)*k
#
# print(sum)

from sys import stdin
import heapq

n = int(stdin.readline())
cards = list()
for i in range(n):
    card = int(stdin.readline())
    heapq.heappush(cards, card)

total = 0
while len(cards) > 0:
    if len(cards) == 1:
        break
    a = heapq.heappop(cards) # 첫번째로 작은
    b = heapq.heappop(cards) # 두번째로 작은
    sum = a+b
    total += sum
    heapq.heappush(cards, sum)
print(total)
