# 풀이 1: 그냥 재귀 => 이진 탐색을 사용하지 않으니 시간 초과.

# from sys import stdin
#
#
# def parametric_search(height, rice_cakes, cut):
#     # 재귀로 짜보기 => 그냥 재귀는 시간 초과..
#     # M: 요청한 떡의 길이
#     # rice_cakes: 내가 갖고 있는 각각 떡의 길이 & N: 떡 개수
#     # height = 설정한 절단기 길이
#
#     # 종료조건
#     if M <= sum(cut):
#         print(height+1)
#         return
#
#     cut = [0]*N #cut reset
#     for i in range(N):
#         if (rice_cakes[i]-height) > 0:
#             cut[i] = (rice_cakes[i]-height)
#         else:
#             cut[i] = 0
#     parametric_search(height-1, rice_cakes, cut)
#
#
# N, M = map(int, stdin.readline().split())
# rice_cakes = list(map(int, stdin.readline().split()))
# cut = [0, 0, 0, 0]
# parametric_search(max(rice_cakes), rice_cakes, cut)



# 풀이 2: 반복문 & 재귀 => Pypy3에서는 돌아가나 python3에서는 시간 초과
from sys import stdin

N, M = map(int, stdin.readline().split())
rice_cakes = list(map(int, stdin.readline().split()))

# 원래 이진탐색에서는 (array, target, start, end)가 필요한데 => 우리는 array 넣어주고 & target은 최댓값, start, end는
start = 0
end = max(rice_cakes)
# 재귀에 너무 목숨걸지 말자..!
ans = 0

def binary_search(array, start, end):
    while (start <= end):
        total_amount = 0
        mid = (start + end) // 2

        for i in rice_cakes:
            if i > mid:
                total_amount += i - mid

        if total_amount < M:
            end = mid-1
        else:
            ans = mid
            start = mid + 1

    print(ans)

binary_search(rice_cakes, start, end)

# 풀이 3: 이분 탐색 & 재귀 => Solved! Pypy3는 물론이고 Python3에서도 잘 돌아간다!

# M: 요청한 떡의 길이
# rice_cakes: 내가 갖고 있는 각각 떡의 길이 & N: 떡 개수
# height = 설정한 절단기 길이

from sys import stdin

def binary_search(rice_cakes, target, start, end):
    total_cakes = 0
    mid = (start + end) // 2
    # 종료 조건
    if start > end:
        print(mid)
        return

    for i in rice_cakes:
        if i > mid:
            total_cakes += i - mid

    if total_cakes >= target:
        binary_search(rice_cakes, target, mid + 1, end)
    elif total_cakes < target:
        binary_search(rice_cakes, target, start, mid - 1)

N, M = map(int, stdin.readline().split())
rice_cakes = list(map(int, stdin.readline().split()))

start = 0
end = max(rice_cakes)
while True:
    a = binary_search(rice_cakes, M, start, end)
    if a == None:
        break