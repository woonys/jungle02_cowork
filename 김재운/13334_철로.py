from sys import stdin
import heapq

n = int(stdin.readline())
com = [list(map(int, stdin.readline().split())) for _ in range(n)]
d = int(stdin.readline()) # d는 선분 길이

li = []

for i in com:
    i[0], i[1] = min(i[0], i[1]), max(i[0], i[1])
    if i[1] - i[0] > d:
        continue
    else:
        li.append(i)

li.sort(key= lambda x: x[1])

heap = []
max_count = 0
for i in li:
    if len(heap) == 0:
        heapq.heappush(heap, i)
    else:
        while len(heap) != 0 and heap[0][0] < i[1] - d:
            heapq.heappop(heap)
        heapq.heappush(heap, i)
    max_count = max(max_count, len(heap))

print(max_count)


