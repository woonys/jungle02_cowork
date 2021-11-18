import sys

n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

count = 0
val = 0

for i in range(n):
    if count == 0:
        count += 1
        val = a.pop()
    else:
        if a[-1] <= val:
            a.pop()
        else:
            a[-1] > val
            count += 1
            val = a.pop()

print(count)