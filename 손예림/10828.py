import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    lst = sys.stdin.readline().split()
    if len(lst) == 2:
        stack.append(lst[1]) #스택리스트에 lst입력 받은 값 중 2단어짜리의 2번째값을 채워준다
    else:
        if lst[0] == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        elif lst[0] == 'size':
            print(len(stack))
        elif lst[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif lst[0] == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])