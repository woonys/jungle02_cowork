from sys import stdin

n = int(stdin.readline())

top_stack = list(map(int, stdin.readline().split()))
k = top_stack.pop()
i = -1
ans = list()
while len(top_stack) > 0:
    if top_stack[i] > k:
        ans.append(len(top_stack)+1+i)
        k = top_stack.pop()
        i = -1
    else:
        if top_stack[i] == top_stack[0]:
            ans.append(0)
            i = 0
        i-=1

