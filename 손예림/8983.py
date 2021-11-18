import sys

m, n, l = map(int, sys.stdin.readline().split())
gun = list(map(int, sys.stdin.readline().split()))
animal = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
gun.sort()

count = 0
for i in animal[:]:
    start = 0
    end = m - 1
    while (start < end):
        mid = (start + end) // 2
        if gun[mid] < i[0]:
            start = mid + 1
        else:
            end = mid
    #사정거리 안에 들어오는지
    if (abs(i[0] - gun[end - 1])+i[1]) > 1 and (abs(gun[end] - i[0])+i[1]) <= l:
        count += 1
        
print(count)
#잡을 수 있는 동물의 수 출력