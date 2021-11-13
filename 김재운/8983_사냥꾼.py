# 풀이 1: 이중 for문 돌리기 => 60점

from sys import stdin

m, n, l = map(int, stdin.readline().split())
gun = list(map(int, stdin.readline().split()))
animal = [list(map(int, stdin.readline().split())) for _ in range(n)]

def distance(gun, animal):
    return (abs(gun-animal[0]) + animal[1])

count = 0
for i in gun:
    for j in animal[:]:
        if distance(i, j) <= l:
            count += 1
            print(j)
            animal.remove(j)


print(count)

# 풀이 2: 이분탐색으로 x, y 기준으로 싹 정렬하고 제거

from sys import stdin
from bisect import bisect_left

m, n, l = map(int, stdin.readline().split())
gun = list(map(int, stdin.readline().split()))
animal = [list(map(int, stdin.readline().split())) for _ in range(n)]

gun.sort()  # 사대 정렬하고
# 무조건 l-animal[i][1]만큼 까야겠네. 그게 사대 거리 (x 값끼리만 비교 가능)


count = 0
for i in animal[:]:
    start = 0  # 사대의 가장 왼쪽 위치
    end = m - 1
    while (start < end):
        mid = (start + end) // 2
        if gun[mid] < i[0]:
            start = mid + 1
        else:
            end = mid
    if (abs(i[0] - gun[end - 1])+i[1]) > l  and (abs(gun[end] - i[0])+i[1]) <= l:
        count += 1

print(count)