# import sys
# n = int(sys.stdin.readline())
# lst = list(map(int,sys.stdin.readlind().split()))
# lst.sort()

from sys import stdin

n = int(stdin.readline())
solution_list = list(map(int, stdin.readline().split()))

solution_list.sort()


def two_pointer(array, n):
    left = 0
    right = n - 1
    ans = [float('inf'), 0, 0]
    while True:
        if left > right:
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