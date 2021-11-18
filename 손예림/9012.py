import sys

input = sys.stdin.readline
n = int(input())

for i in range(n):
    input_data = input()
    sum = []

    for j in input_data:
        if j == "(":
            sum.append(j)
        elif j == ")":
            if len(sum) != 0 and sum[-1] == "(":
                sum.pop()
            else: 
                sum.append(")")
                break
            

    if len(sum) == 0:
        print("YES")
    else:
        print("NO")
        


# sum = 0
# for _ in range(k):
#     lst.append(map(str,input().split()))

#     for i in lst:
#         if i == '(':
#             sum += 1
#         else: 
#             i == ')'
#             sum -= 1
            

#     if sum == 0:
#         print("YES")
#     else:
#         print("NO")
