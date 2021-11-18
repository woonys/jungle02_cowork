from sys import stdin
from collections import deque



# 알고리즘 수행 과정
# 1. 2차원 배열(N x N)을 만든다. (0으로 초기화)
#
# 2. 사과의 위치에 1을 저장한다.
#
# 3. (0, 0)에서 뱀은 시작하며 뱀이 지나갔던 곳은 2로 저장한다.
#
# - 방향의 변화가 생겼는지 확인한다.
#
# - 뱀의 머리가 사과가 없는 위치로 가면 꼬리의 값을 0으로 수정한다. (2 -> 0)
#
# - 뱀의 머리가 사과가 있는 위치로 가면 꼬리의 값을 수정하지 않는다.
#
# 4. 3번의 과정을 벽에 부딪히거나, 자기 자신의 몸에 부딪힐 때까지 진행한다.

def change(d, c): # d는 회전 방향 # c는 왼/오 구분
    # 상:0, 우:1, 하: 2, 좌:3
    # 시계 방향 회전: 상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0): +1 방향
    # 반시계 방향 회전: 상(0) -> 좌(3) -> 하(2) -> 우(1) -> 상(0): -1 방향

    if c == "L":
        d = (d-1) % 4
    else:
        d = (d+1) % 4
    return d
# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def start():
    # arr에는 사과를 저장 or 뱀 지나갔던 위치 체크
    direction = 1 # 초기방향
    time = 1 # 시간
    y, x = 0, 0 # 초기 뱀 위치 => x가 행이고 y는 열인데 이차원 배열에서는 y부터 결정됨!
    visited = deque([[y, x]]) # 방문 위치
    arr[y][x] = 2 # 뱀이 지나간 곳은 2로 저장
    while True:
        y, x = y + dy[direction], x + dx[direction] # y, x 둘 중 하나 값으로 direction 방향으로 이동
        if 0 <= y < n and 0 <= x < n and arr[y][x] !=2: #arr 체크: 아직 지나가지 않은 곳일때
            if not arr[y][x] == 1: # 사과가 없는 경우
                temp_y, temp_x = visited.popleft() #방문했던 곳에서 자리 빼와
                arr[temp_y][temp_x] = 0 # 꼬리 제거
            arr[y][x] = 2
            visited.append([y, x])
            if time in times.keys(): # time은 시간 저장해놓은 딕셔너리
                direction = change(direction, times[time])
            time +=1
        else:
            return time

if __name__ == "__main__":
    # input값
    n = int(stdin.readline())
    k = int(stdin.readline())
    arr = [[0] * n for _ in range(n)]
    for i in range(k):
        a, b = map(int, stdin.readline().split())
        arr[a - 1][b - 1] = 1  # 사과 저장
    L = int(stdin.readline())
    times = {}
    for i in range(L):
        X, C = stdin.readline().split()
        times[int(X)] = C
    print(start())
