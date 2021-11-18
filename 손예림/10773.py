import sys

k = int(sys.stdin.readline())
stack = []

for i in range(k):
    lst = int(sys.stdin.readline())
    if lst == 0: #'0'하면 문자열이라 에러남
        stack.pop()
    else:
        stack.append(lst)

print(sum(stack))