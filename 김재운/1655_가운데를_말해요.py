# 1. sort 이용 => 시간 초과.. 알면서도 그냥 해봄..
from sys import stdin

n = int(stdin.readline())
ans = []
for i in range(n):
    num = int(stdin.readline())
    ans.append(num)
    ans.sort()
    if i % 2 == 0:
        print(ans[i//2])
    else:
        if ans[i // 2] < ans[i //2 +1]:
            print(ans[i//2])
        else:
            print(ans[i // 2+1])
#
# 2. 얘를 더 빠르게 정렬? => 우선순위 큐!

힙 정렬하면? => 얘도 시간초과.. for문 두 번 돌아서 의미가 없는듯
from sys import stdin
import heapq

n = int(stdin.readline())

ans = []
for i in range(n):
    num = int(stdin.readline())
    heapq.heappush(ans, num)
    temp = ans[:]
    for _ in range(i // 2):
        heapq.heappop(temp)
    if i % 2 == 0:
        pass
    else:
        a = heapq.heappop(temp)
        b = heapq.heappop(temp)
        if a < b:
            print(a)
        else:
            print(b)
        continue
    mid = heapq.heappop(temp)
    print(mid)

from sys import stdin
import heapq

n = int(stdin.readline())

leftheap = []
rightheap = []
answer = []

for i in range(n):
    input_num = int(stdin.readline())

    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, (-input_num, input_num)) # 양쪽에 같은 개수가 들어가면 (==
    else:
        heapq.heappush(rightheap, (input_num, input_num))

    if rightheap and leftheap[0][1] > rightheap[0][0]: # rightheap이 있고 & leftheap[0][1]
        min = heapq.heappop(rightheap)[0]
        max = heapq.heappop(leftheap)[1]
        heapq.heappush(leftheap, (-min, min))
        heapq.heappush(rightheap, (max, max))

    answer.append(leftheap[0][1])
for j in answer:
    print(j)