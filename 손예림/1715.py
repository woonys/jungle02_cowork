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

A, B, C = map(int, sys.stdin.readline().split())

def multi(a, b):
    # b가 1인 경우에는 곱할 필요가 없기에 그냥 나머지 리턴.
    if b == 1:
        return a % C

    # multi함수를 통해 a를 (b // 2)번 곱한 나머지를 구함.
    tmp = multi(a, b // 2) # 재귀
    
    # b가 짝수인 경우 (a가 n의 제곱 이상으로 가는 경우)
    if b % 2 == 0:
    # tmp를 제곱 후 C로 나눈 나머지를 리턴.
        return tmp * tmp % C
    # b가 홀수인 경우
    else:
    # tmp 제곱 후 a를 한번 더 곱한 후 C를 나눠야 a를 b번 곱한 후 C로 나눈 나머지가 구해짐.
        return tmp * tmp * a % C
        

print(multi(A, B))


# import sys
# a,b,c = map(int,sys.stdin.readline().split())

# def multi (a,n):
#     if n == 1:
#         return a%c
#     else:
#         tmp = multi(a,n//2)
#         if n %2 ==0:
#             return (tmp * tmp) % c
#         else:
#             return (tmp  * tmp *a) %c

# print(multi(a,b))
