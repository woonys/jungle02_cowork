# 풀이 1: My solution
# from sys import stdin
#
#
# def binary_search_idx(array, start, end, count, c_list):
#     # start, end에는 각각 인덱스 값이 들어가야. count는 공유기 수 (c)
#     mid = (start + end) // 2
#     print("mid is: ",mid)
#     print("c_list is: ", c_list)
#     if count == 0:
#         c_list.sort()
#         print("종료", c_list)
#         return c_list
#
#     if array[mid] - array[start] < array[end] - array[mid]:
#         print("go right")
#         start = mid + 1
#         print("start is ", start)
#         count -=1
#         c_list.append(start)
#         binary_search_idx(array, mid+1, end, count, c_list)
#
#     elif array[mid] - array[start] > array[end] - array[mid]:
#         end = mid-1
#         print("end is: ", end)
#         count -= 1
#         c_list.append(start)
#         binary_search_idx(array, start, mid-1, count, c_list)
#
# n, c = map(int, stdin.readline().split())
#
# homes = [int(stdin.readline()) for _ in range(n)] # 리스트에는 최대 20만개 & 각 밸류는 최대 10억
# homes.sort() # 집 좌표 정렬
#
# c_list = [0, n-1]
#
# binary_search_idx(homes, 0, n-1, c-2, c_list) # start, end에는 인덱스 값이 들어가야 하니 end에 n-1







# 풀이 2: mid 간격만큼 공유기 배치 후 내가 배치한 공유기 수(count)보다 c 값이 크냐 작냐로 이진 탐색 실시

# from sys import stdin
#
# n, c = map(int, stdin.readline().split())
#
# homes = [int(stdin.readline()) for _ in range(n)] # 리스트에는 최대 20만개 & 각 밸류는 최대 10억
# homes.sort() # 집 좌표 정렬

#start, end, mid: 각각 집과 집 사이 거리의 최소/최대/중간값
# start = 1
# end = homes[-1] - homes[0]
# result = 0
# while (start <= end):
#     mid = (start + end) // 2
#     current = homes[0]
#     count = 1
#     for i in range(1, n):
#         if homes[i] >= current + mid: #homes[i]와 homes[i-1] 사이 간격이 mid보다 크면!
#             count +=1
#             current = homes[i] #homes[i], homes[i+1] 사이 간격 비교
#
#     if count >= c:
#         start = mid +1
#         result = mid
#     else:
#         end = mid - 1
# print(result)


#풀이 2 again

from sys import stdin

n, c = map(int, stdin.readline().split())
homes = [int(stdin.readline()) for _ in range(n)]
homes.sort()

start = 1
end = homes[-1] - homes[0]
result = 0 # 공유기 사이 거리의 최대값
while (start <= end):
    mid = (start + end)//2
    count = 1
    current = homes[0]
    for i in range(1, n):
        if homes[i] >= current + mid:
            count +=1
            current = homes[i]

    if count >= c: # mid 간격보다 큰 애들이 설치해야 할 공유기 대수 이상이라는 뜻이니 mid 간격을 늘려야. 그러려면 start를 mid+1만큼 올려야 start+end의 평균이 그만큼 올라감.
        start = mid + 1
        result = mid
    else:
        end = mid -1

print(result)