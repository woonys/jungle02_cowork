# from sys import stdin
#
# n = int(stdin.readline())
# paper = [list(map(int, stdin.readline().split())) for _ in range(n)]
# result = []
# def divide(x, y, n):
#     # 종료 조건
#     color = paper[x][y]
#     for i in range(x, x+n):
#         for j in range(y, y+n):
#             if color != paper[i][j]:
#                 divide(x, y, n//2)
#                 divide(x, y + n // 2, n // 2)
#                 divide(x+ n // 2, y, n // 2)
#                 divide(x + n // 2, y + n // 2, n // 2)
#                 return # 끝내야 아래 코드가 실행되지 X => 아래 코드는 color가 동일한 케이스에서만 실행되어야 하니!
#     if color == 0:
#         result.append(0)
#     else:
#         result.append(1)
#
# divide(0, 0, n)
# print(result.count(0))
# print(result.count(1))


# 다시!
# 핵심 1: 쪼개고 난 다음에 return 써서 재귀 종료시킬 것.
# 핵심 2: 재귀 쪼갤 때 범위 잘 설정하기 => 아래 i, j의 range에서 처음에는 N만 넣었는데 (range(N)) 이게 아니라 각 쪼갠 사각형에서 스캔 때려야 하니
# range(x, x+N), range(y y+N) 이렇게!

from sys import stdin

n = int(stdin.readline())
li = [list(map(int, stdin.readline().split())) for _ in range(n)]
w_count = 0
b_count = 0

def divide(x, y, N):

    color = li[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != li[i][j]:
                divide(x, y, N//2)
                divide(x+N//2, y, N//2)
                divide(x, y+N//2, N//2)
                divide(x+N//2, y+N//2, N//2)
                return # 이게 핵심! break가 아니라 return 해서 끝내기

    if color == 0:
        global w_count
        w_count +=1

    else:
        global b_count
        b_count += 1

divide(0, 0, n)
print(w_count)
print(b_count)