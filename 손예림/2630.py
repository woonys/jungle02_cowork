import sys
n = int(sys.stdin.readline())
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

#처음에 모두 같은 색인지 check
#아니면 재귀 1
#파티션 4개 다 같은색인지아닌지 판별하는 과정 함수 만들기


#파티션 나눠보기 전 모두 같은 색인지 체크
def colors(size, x, y):
    start_point = numbers[x][y]
    for i in range(x, size+x): # x 초기위치 받은 곳 부터 끝까지 (가로)
        for j in range(y, size+y): # y 초기위치 받은 곳 부터 끝까지 (세로)
            if numbers[i][j] == start_point:
                continue
            else:
                return -1 # False
    if start_point == 0: #초기위치 값이 0이다
        return 0 #White
    else:
        return 1 #Blue

#재귀(파티션 나눠서 색 체크)
def partitions(size, x, y):
    global white, blue
    #colors에서 색검사하고 다 같은 색이면(colors == 리턴값 Ture) 종결
    if colors(size, x, y) == 1:
        blue += 1
    elif colors(size, x, y) == 0:
        white += 1
    else: # False인 경우 파티션 나눔
        partitions(size//2, x, y) # 0, 0
        partitions(size//2, x, y + size//2) # 0, 4
        partitions(size//2, x + size//2, y)
        partitions(size//2, x + size//2, y + size//2)
        
        
        
white = 0
blue = 0
partitions(n, 0, 0)
print(white)
print(blue)
    


