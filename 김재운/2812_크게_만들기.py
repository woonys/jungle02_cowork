# from sys import stdin
#
# n, k = map(int, stdin.readline().split())
# num = stdin.readline().strip() # 숫자를 str로 받기
# stack = []
# for i in range(len(num)):
#     t = int(num[i])
#
#     if len(stack) == 0:
#         stack.append(t)
#     else:
#         while stack[-1] < t:
#             stack.pop()
#             if len(stack) == 0:
#                 break
#         stack.append(t)
#
#
#     if len(stack) + (n-i-1) == n-k:
#         ans = "".join(map(str, stack)) + num[i+1:]
#         print(int(ans))




from sys import stdin

n, k = map(int, stdin.readline().split())
num = stdin.readline().strip() # 숫자를 str로 받기
stack = []
delNum = k
for i in range(n):
    while delNum > 0 and stack:
        if stack[-1] < num[i]:
            stack.pop()
            delNum -=1
        else:
            break
    stack.append(num[i])

a = ""
for i in range(n-k):
    a += str(stack[i])
print(int(a))





