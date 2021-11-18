# from sys import stdin
#
# n = int(stdin.readline())
# a = list(map(int, stdin.readline().split()))
#
# left = 0
# right = n-1
# p = [a[0]]
# i = 0
# while left <= right:
#     if a[i] - a[left] > 0:
#         p.append(a[i])
#         left = i
#         i = left
#     i+= 1
#
#     if i > right:
#         break
# print(len(p))

# 11053번

# 풀이 1: dp
#
# 1. dp[i]를 1로 초기화
# 2. 현재 위치(i)보다 이전에 있는 원소(j)가 작은지 확인.
# 3. 작다면, 현재 위치의 이전 숫자 중, dp 최댓값을 구하고 거기에 1을 추가해준다. (A[i]를 해당 수열에다가 추가한다고 생각)
# n = int(stdin.readline())
# A = list(map(int, stdin.readline().split()))
#
# dp = [1 for i in range(n)] # dp[i]를 1로 초기화
#
# for i in range(n): # 여기서는 A의 각 원소를 뽑고
#     for j in range(i): # 여기서는 A의 각 원소 A[i]를 기준으로 그보다 작은 애들 (A[0], A[1], ..., A[i-1])
#         if A[i] > A[j]: #이 중 A[j]가 A[i]보다 작다면 -> 증가수열에 해당
#             dp[i] = max(dp[i], dp[j]+1) #원래 0부터 j까지 최대 증가수열에다가 i를 추가하니 +1하고 얘를 dp[i]와 비교해서 최댓값
#
# print(max(dp))
#
# 이 때 dp의 시간복잡도는 O(N^2) => 각 원소 i에 대해 그보다 작은 애들 0~i-1까지 다 살펴봐야 하니.








# 풀이 2: 이진 탐색

from sys import stdin
from bisect import bisect_left

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

dp = []

for i in a:
    k = bisect_left(dp, i) # dp 배열에서 i에 해당하는 인덱스를 이진 탐색으로 반환
    if len(dp) <= k: # i가 가장 큰 숫자라면
        dp.append(i)
    else:
        dp[k] = i # 자신보다 큰 수 중 최솟값과 대체

print(dp)

# 위의 방식은 정답 길이를 알아내는 것은 오케이인데 dp 순열이 실제 정답과 일치하지 않음.