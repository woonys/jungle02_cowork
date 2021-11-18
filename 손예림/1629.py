import sys

A, B, C = map(int, sys.stdin.readline().split())

def multi(a, b):
    # b가 1인 경우에는 곱할 필요가 없기에 그냥 나머지 리턴.
    if b == 1:
        return a % C

    # multi함수를 통해 a를 (b // 2)번 곱한 나머지를 구함.
    tmp = multi(a, b // 2) # 재귀
    
    # b가 짝수인 경우 (a가 n의 제곱 이상으로 가는 경우)
    if b % 2 == 0:
    # tmp를 제곱 후 C로 나눈 나머지를 리턴.
        return tmp * tmp % C
    # b가 홀수인 경우
    else:
    # tmp 제곱 후 a를 한번 더 곱한 후 C를 나눠야 a를 b번 곱한 후 C로 나눈 나머지가 구해짐.
        return tmp * tmp * a % C
        

print(multi(A, B))


# import sys
# a,b,c = map(int,sys.stdin.readline().split())

# def multi (a,n):
#     if n == 1:
#         return a%c
#     else:
#         tmp = multi(a,n//2)
#         if n %2 ==0:
#             return (tmp * tmp) % c
#         else:
#             return (tmp  * tmp *a) %c

# print(multi(a,b))