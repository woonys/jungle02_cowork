from sys import stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
find_num = list(map(int, stdin.readline().split()))

A.sort()

def binary_search(array, target, start, end): # start, end: 인덱스!
    if start > end:
        return 0
    mid = (start + end) // 2
    if target == array[mid]:
        return 1
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

for tar in find_num:
    print(binary_search(A, tar, 0, N-1))
