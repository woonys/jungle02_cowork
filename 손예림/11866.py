import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
nums = deque(range(1, n+1)) # 1~n까지 만듦
result = []

while len(nums) > 0:
    for i in range(k):
        if i == k-1:
            result.append(nums.popleft())
        else:
            nums.append(nums.popleft())
    
# while len(nums) > 0:
#     nums.append(nums.popleft())
#     nums.append(nums.popleft())
#     result.append(nums[0])
#     nums.popleft()
    
    
# a = "".join(str(y))    
# a = result[1:-1]
# print('<'+a+'>')
print('<%s>'%(str(result)[1:-1]))
