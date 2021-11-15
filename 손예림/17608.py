import sys

n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
_a = a[::-1]

# print(_a)
high = []
# count = 0
for i in range(n):
    if i >= :
        high.append(i)
    elif i >= high[i-1]:
        high.append(i)
        # count += 1
    # else :
        # i < high
        # high.pop()
        
print(len(high))

