from sys import stdin

n = int(stdin.readline())

def push(command, list):
    num= int(command[1])
    list.append(num)


ans_list = [] #리스트로 스택 구현 - 리스트에서 스택 구현은 append(push에 해당)와 pop()로 한다.
for i in range(n):
    com = stdin.readline().split()
    if len(com) == 2: # push x에 해당
        push(com, ans_list)
    else:
        command = com[0]
        if command == 'pop':
            if len(ans_list) == 0:
                print(-1)
            else:
                print(ans_list.pop())
        elif command == 'size':
            print(len(ans_list))
        elif command == 'empty':
            if len(ans_list) ==0:
                print(1)
            else:
                print(0)
        else:
            if len(ans_list) == 0:
                print(-1)
            else:
                print(ans_list[-1])
