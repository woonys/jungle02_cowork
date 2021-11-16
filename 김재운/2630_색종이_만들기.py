from sys import stdin

n = int(stdin.readline())
paper = [list(map(int, stdin.readline().split())) for _ in range(n)]
result = []
def divide(x, y, n):
    # 종료 조건
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                divide(x, y, n//2)
                divide(x, y + n // 2, n // 2)
                divide(x+ n // 2, y, n // 2)
                divide(x + n // 2, y + n // 2, n // 2)
                return # 끝내야 아래 코드가 실행되지 X => 아래 코드는 color가 동일한 케이스에서만 실행되어야 하니!
    if color == 0:
        result.append(0)
    else:
        result.append(1)

divide(0, 0, n)
print(result.count(0))
print(result.count(1))