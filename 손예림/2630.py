import sys
n = int(sys.stdin.readline())
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

#처음에 모두 같은 색인지 check
#아니면 재귀 1
#파티션 4개 다 같은색인지아닌지 판별하는 과정 함수 만들기

white = 0
blue = 0
def colors(size):
    for i in range(size): #numbers 
        for j in i:
            if range(size)[0][0] == j:
                continue
            else:
                return False, j #j 의미없음
    return True, j

#재귀
def partitions(n, x, y): #위치는?
    global white, blue
    #colors에서 색검사하고 다 같은 색이면(colors == 리턴값 Ture) 종결
    if colors(n) == (True, 1):
        blue += 1
    elif colors(n) == (True, 0):
        white += 1
    else:
        partitions(n//2, 0, 0) #이걸 네번 부르고 위치를 계싼해
        partitions(n//2, x, y)
        
        
        
    
    


#재귀 돌릴 영역


