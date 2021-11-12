import sys
input=sys.stdin.readline

n, min_bring = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

start = 0
end = max(trees)

while start <= end :
    mid = (start+end) // 2
    
    T_cut_sum = 0
    for tree in trees:
        if tree >= mid:
            T_cut_sum += tree-mid
    
    if T_cut_sum >= min_bring:
        start = mid + 1
    else:
        end = mid - 1
    
print(end)


# ---

# import sys
# input=sys.stdin.readline

# n, min_bring = map(int, input().split())
# trees = list(map(int, input().split()))
# trees.sort()

# start = 0
# end = max(trees)
# check = 0

# def sumcut(mid):
#     T_cut_sum = 0
#     for tree in trees:
#         if tree >= mid:
#             T_cut_sum += tree-mid
#     return T_cut_sum
            
# while start <= end :
#     mid = (start+end) // 2
#     T_cut_sum = sumcut(mid)
#     if T_cut_sum >= min_bring:
#         start = mid + 1
#         check = mid
#     else:
#         end = mid - 1
    
# print(end)
