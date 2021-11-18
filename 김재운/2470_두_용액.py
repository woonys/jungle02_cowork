# from sys import stdin
#
# n = int(stdin.readline())
# solution_list = [int(stdin.readline()) for _ in range(n)]
#
# solution_list.sort()

# start = 0
# end = max(abs(solution_list[-1] + solution_list[-2]), abs(solution_list[0] + solution_list[1]))
# def find(array, start, end)
#
#     mid = (start + end) // 2
#     current = array[0]
#     if start > end:
#         print(mid)
#         return
#
#     for i in range(n):
#         if abs(current + solution_list[i]) <= mid:


# 말 그대로 투포인터 알고리즘. 이진 탐색이 아닌 것 같은데...?

from sys import stdin

n = int(stdin.readline())
solution_list = list(map(int, stdin.readline().split()))

solution_list.sort()

#
def two_pointer(array, n):
    left = 0
    right = n - 1
    ans = [float('inf'), 0, 0]
    while True:
        if left >= right: # left와 right가 같으면 안됨! 여기서 용액 값은 모두 특성값이니..
            return ans

        tmp = (array[left] + array[right])
        if abs(tmp) < ans[0]:  # 값을 저장하는 식으로
            ans = [abs(tmp), array[left], array[right]]

        if tmp > 0:
            right -= 1
        elif tmp < 0:
            left += 1
        else:  # abs(tmp) == 0 => 정답!
            ans = [abs(tmp), array[left], array[right]]
            return ans


answer = two_pointer(solution_list, n)

print(f'{answer[1]} {answer[2]}')


