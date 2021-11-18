# 1. 넘파이 이용 풀이

# from sys import stdin
# import numpy as np
#
# n, b = map(int, stdin.readline().split())
#
# A = [list(map(int, stdin.readline().split())) for _ in range(n)]
#
# A = np.array(A)
#
# def sqr(a, n):
#     m = a
#     # a는 행렬, n은 제곱수
#     for _ in range(n-1):
#         m = np.dot(a, m)
#     return m
#
# print(sqr(A, b) % 1000)

# 2. 분할 정복

from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
n, b = map(int, stdin.readline().split()) # n: 행렬의 크기 b: 제곱수

A = [list(map(int, stdin.readline().split())) for _ in range(n)]


def matrix_mul(a, b):
    result = [([0] * n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k]*b[k][j] % 1000

    return result


def divide(mat, sqr): #A: 행렬, b: 제곱수
    if sqr == 1:
        return mat
    if sqr == 2:
        return matrix_mul(mat, mat)
    else:
        tmp = divide(mat, sqr//2)
        if sqr % 2 == 0:
            return matrix_mul(tmp, tmp)
        else:
            return matrix_mul(matrix_mul(tmp, tmp), mat)

ans = divide(A, b)
for i in range(n):
    li = []
    for j in range(n):
        print(ans[i][j] % 1000, end=" ")
    print()