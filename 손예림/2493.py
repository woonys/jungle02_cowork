import sys

n = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
stack = []
a = []

for i in range(0,n):
    while 1:
        if not stack:
            stack.append((i,top[i]))
            a.append(0)
            break
        if stack[-1][1]>=top[i]:
            a.append(stack[-1][0]+1)
            stack.append((i,top[i]))
            break
        else:
            stack.pop()
print(*a)






# for i in range(n):
#     if len(stack) == 0: #시작할때마다 저장해야하니까 if == 0이면 안됨;
#         a = top[-1] 
#         if top[-2] > a:
#             stack.append(top.pop())
#         elif top[-2] <= a:
#             continue
#         else:
#             stack.append(0)
#     else:
#         a = top[-1] 
#         if top[-2] > a:
#             stack.append(top.pop())
#         elif top[-2] <= a:
#             continue
#         else:
#             stack.append(0)
    

# print(stack[::-1])
        
        