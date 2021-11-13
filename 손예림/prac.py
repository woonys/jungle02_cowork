import sys

def Count(len):
    cnt=0
    for x in l_list:
        cnt += (x//len)
    return cnt



n, m = map(int, input().split())
l_list = []
result = 0
largest = 0

for i in range(n):
    tmp = int(input())
    l_list.append(tmp)
    largest = max(largest, tmp)
    
lt = 1
rt = largest
    
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid)>=n:
        result=mid
        lt = mid+1
    else:
        rt = mid-1

print(result)
