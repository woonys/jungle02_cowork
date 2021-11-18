import sys

n, c = map(int, sys.stdin.readline().split())
home_list = [int(sys.stdin.readline()) for _ in range(n)]
home_list.sort()

start, end = 1, home_list[-1] - home_list[0]
result = 0 # 공유기 사이 거리의 최대값

while start <= end:
    mid = (start + end) // 2
    count = 1
    current = home_list[0]
    for i in range(1,n):
        if home_list[i] >= current + mid:
            count += 1
            current = home_list[i]
    if count >= c: 
        start = mid + 1
        result = mid
    else:
        end = mid - 1
        
print(result)
