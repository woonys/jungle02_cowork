from sys import stdin
a, b, c = map(int, stdin.readline().split())

def mod(n, k):
    if k == 1:
        return n % c
    else:
        tmp = mod(n, k//2)
        if k % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * n) % c

print(mod(a, b))
