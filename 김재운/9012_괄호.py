from sys import stdin

n = int(stdin.readline())
vps_list = [stdin.readline().strip() for _ in range(n)]


for i in vps_list:
    check = []
    for j in i:
        if j == "(":
            check.append(j)
        elif j == ")":
            if len(check) != 0 and check[-1] == "(":
                check.pop()
            else:
                check.append(")")
                break

    if len(check) == 0:
        print("YES")
    else:
        print("NO")
