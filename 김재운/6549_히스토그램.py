# from sys import stdin
#
# list_ = list(map(int, stdin.readline().split()))
# n = list_[0]
# h_list = list_[1:]
# ans_list = []
# for k in range(n):
#     temp_ans = []
#     for j in range(k + 1):
#         if k - 1 - j == -1:
#             ans = min(h_list[j: k - 1 - j]) * (k + 1)
#         ans = min(h_list[j: k - 1 - j]) * (k + 1)
#         temp_ans.append(ans)
#     a = min(temp_ans)
#     ans_list.append(a)
#
# print(max(ans_list))

from sys import stdin


def his_sqr(a):
    if len(a) == 1:
        return a[0]

    if len(a) % 2 == 1:
        a = [0] + a
    d = len(a) // 2
    x = a[:d]
    y = a[d:]
    cnt = 2
    tmpmax = min(a[d - 1], a[d])
    tmparea = tmpmax * cnt
    i = 0
    j = 0

    for _ in range(0, len(a) - 2):
        if d - 1 - i == 0:
            j += 1
        elif d + j == len(a) - 1:
            i += 1
        else:
            if a[d - 2 - i] >= a[d + 1 + j]:
                i += 1
            else:
                j += 1
        tmpmax = min(tmpmax, a[d - 1 - i], a[d + j])
        cnt += 1
        tmparea = max(tmparea, tmpmax * cnt)
    z = tmparea
    return max(his_sqr(x), his_sqr(y), z)

while True:
    n, *histogram = list(map(int, stdin.readline().split()))
    if n == 0:
        break
    maxarea = his_sqr(histogram)
    print(maxarea)