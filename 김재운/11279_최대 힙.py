from sys import stdin
import heapq

n = int(stdin.readline())

ans_list = []

for i in range(n):
    a = int(stdin.readline())
    if a == 0:
        if len(ans_list) == 0:
            print(0)
        else:
            print(heapq.heappop(ans_list)[1])
    else:
        heapq.heappush(ans_list, (-a, a))
