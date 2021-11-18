import sys
import heapq

input = sys.stdin.readline
testcase = int(input())

heap = []
for i in range(testcase):
    heapq.heappush(heap, int(input()))

result = 0 # 최종 결과값
tmp = 0 # 중간 결과값

while True: #heap이 비어있는 경우는 더 돌 필요가 없으니 True일때로.
    # 2뭉탱이 빼내기
    if len(heap) >= 2: #1개 남아있을 때도 또 돌아서 더함
        tmp = heapq.heappop(heap) + heapq.heappop(heap)
        heapq.heappush(heap, tmp)
        result += tmp
        if len(heap) == 1:
            heapq.heappop(heap)
            break
    
    if len(heap) == 1:
        result = 0
        break
        
    # if not heap: #heap 안에 아무것도 없으면
        # break

print(result)
