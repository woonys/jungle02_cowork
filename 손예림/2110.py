import sys

n, c = map(int, sys.stdin.readline().split())
home_list = []

for i in range(n):
    home_list.append(int(input()))

home_list.sort()
start, end = min(home_list), max(home_list)

while start <= end:
    mid = (start + end) // 2
    distance = 0
    # count=0
    #if count == c:
        # break
    
    for i in home_list:
        if i >= mid:
            distance += i - mid #나오는 값을 최대 거리 값으로 저장해줌
            # count += 1
    if c >= (distance // c): #체크해보기
        start = mid + 1
    else:
        end = mid - 1
        
print(end)

