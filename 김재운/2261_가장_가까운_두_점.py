# from sys import stdin
#
# n = int(stdin.readline())
#
# pl = [list(map(int, stdin.readline().split())) for _ in range(n)]
#
# # x축 기준 정렬
# pl.sort()
#
# minDist = min(dac(start, mid), dac(mid, end))
#
# # x축 기준으로 후보 점 찾기
# target_pl = []
# for i in range(start, end + 1):
#     if (pl[mid][0] - pl[i][0]) ** 2 < minDist:
#         target_pl.append(pl[i])
#         # 여기서 x축 기준으로 거리가
# # y축 기준 정렬
# target_pl.sort(key=lambda x: x[1])
#
# # y축 기준으로 후보 점들 사이의 거리 비교
# t = len(target_pl)
# for i in range(t - 1):
#     for j in range(i + 1, t):
#         if (target_pl[i][1] - target_pl[j][1]) ** 2 < minDist:
#             minDist = min(minDist, getDist(target_pl[i], target_pl[j]))
#         else:
#             break
#             # 현재 후보 점이 다음 점과 최소 거리보다 먹
# # 두 점 사이 거리 계산 함수
# def getDist(p1, p2):
#     return (p1[0] - p2[0])**2 + (p1[1]-p2[1])**2
#
# def dac(start, end):
#     # 종료 조건
#     # 1. 점 하나의 거리는 없으니 최대값을 리턴
#     if end == start:
#         return float('inf')
#
#     # 2. 점 두 개 남으면 사이의 거리 리턴
#     if end - start == 1:
#         return getDist(pl[start], pl[end])
#
#
#     # 분할정복 실행
#     mid = (start + end) // 2먹
#
#
#


from sys import stdin
n = int(stdin.readline())
point_list = [list(map(int, stdin.readline().split())) for _ in range(n)]

point_list.sort(key=lambda x: (x[0], x[1]))


def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2


def divideandconquer(start, end):  # start, end는 point_list의 점 순서 인덱스! 사이 거리는 계산하면 되니까
    # 종료 조건
    if end == start + 1:
        return dist(point_list[start], point_list[end])
    mid = (start + end) // 2

    # 각 두 점 사이 거리 재는 걸로 싹다 쪼개기 by 재귀!
    min_val = min(divideandconquer(start, mid), divideandconquer(mid, end))

    temp = []
    for i in range(start, end+1):
        if (point_list[mid][0] - point_list[i][0])**2 < min_val:
            temp.append(point_list[i])
    temp.sort(key=lambda x: x[1])

    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            if (temp[i][1] - temp[j][1])**2 < min_val:
                min_val = min(min_val, dist(temp[i], temp[j]))
            else:
                break
    return min_val


print(divideandconquer(0, n-1))