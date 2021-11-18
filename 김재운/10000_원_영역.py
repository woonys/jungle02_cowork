# 1. 재귀 풀이

# from sys import stdin, setrecursionlimit
# from bisect import bisect_left
#
# n = int(stdin.readline())
# setrecursionlimit(10**6)
#
# li = []
# for i in range(n):
#     x, r = map(int, stdin.readline().split())
#     li.append([x-r, x+r])
#
# li.sort(key=lambda x: (x[0], -x[1]))
#
# count = 0
#
# def check(big, small):
#     global count
#     if big[1] == small[1]: # 둘의 오른쪽 끝점이 같다면
#         count +=1
#         return
#     nextidx = bisect_left(li, [small[1], -100000000000])
#     if nextidx == len(li):
#         return
#     if small[1] -- li[nextidx][0]:
#         check(big, li[nextidx])
#
# for i in range(n-1):
#     if li[i][0] == li[i+1][0]:
#         check(li[i], li[i+1])
# print(1+n+count)


# 2. 스택 풀이: 핵심! start, end 점에 라벨링 & 한 원에 묶는 개념이 아니라 점만 따로 생각! 스택에서 원이 닫히는 식으로다가.

"""백준 10000번 원 영역"""
from sys import stdin
n = int(stdin.readline())


def check_connection(coordinates): # coordinates는 좌표값
    stack = []
    count = 1  # 원이 없어도 공간 하나는 있음
    for circle_type, coordinate in coordinates: # circle_type은 start/end/circle, coordinate는 왼/오 값
        # print(f'현재 좌표 : {coordinate}')
        # 원의 시작점이면 무조건 삽입
        if circle_type == 'start': # 시작점 => 삽입
            stack.append([circle_type, coordinate]) # 스택에다가 (start, 시작점 좌표) 삽입
        else: # 들어오는 점의 상태는 무조건 end겠지. 단, 가장 아래에 보면 type을 circle이라고도 만든다.
            inner_circle = 0 # 내부 원의 지름 = inner_circle이라고 하자. 일단 0으로 설정하고
            while stack and stack[-1][0] == 'circle': # 스택에 맨 위에 쌓인 놈이 circle, 즉 완성된 원이 맨 윗 스택에 놓여 있다면?
                inner_circle += stack.pop()[1] # inner_circle: 위의 완성된 원의 지름을 가져와서 더한다.
            new_circle = coordinate - stack.pop()[1] # 만약 스택 맨 위에 원이 없다면? => 원이 만들어지고 그 원의 지름이 new_circle:
            if new_circle == inner_circle: # new_circle의 지름 길이가 inner circle과 같다면? 즉 내부에 원이 닫힌다면?
                count += 2 # 두 개를 센다.
            else:
                count += 1 # 그렇지 않으면 하나를 세고.
            stack.append(['circle', new_circle]) # 그다음에 circle을 넣어준다. 위에서 end는 이미 pop을 한 상황.
    return count


coordinates = []
for _ in range(n):
    x, r = map(int, sys.stdin.readline().split())
    coordinates.append(['start', x - r])
    coordinates.append(['end', x + r])

coordinates.sort(key=lambda x: x[0])
coordinates.sort(key=lambda x: x[1])
answer = check_connection(coordinates)
print(answer)
