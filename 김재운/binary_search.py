from stdin import stdin
# 반복문으로 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end)//2
        #찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1 # end를 반으로 줄인다.
        else:
            start = mid + 1 #start를 mid 뒤로 위치를 옮긴다

    return None

# 재귀로 구현

def binary_search(array, target, start, end):
    #종료 조건
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)