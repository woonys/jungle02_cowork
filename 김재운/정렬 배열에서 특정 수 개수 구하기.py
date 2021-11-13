# from sys import stdin
# from bisect import bisect_left, bisect_right
# N, target = map(int, stdin.readline().split())
# num_arr = list(map(int, stdin.readline().split()))
#
# #bisect_left(a, x): 배열 a에서 x가 들어갈 인덱스 반환
#
# def count_num():
#     left_idx = bisect_left(num_arr, target)
#     right_idx = bisect_right(num_arr, target)
#     count = right_idx - left_idx
#     if count == 0:
#         return -1
#     return count
#
# print(count_num())

#직접 이진탐색 짜보기

from sys import stdin
N, target = map(int, stdin.readline().split())
num_arr = list(map(int, stdin.readline().split()))

def binary_search_idx_left(num_arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2 # 인덱스 값
    if num_arr[mid] > target:
        end = mid -1
        binary_search_idx_left(num_arr, target, start, end)
