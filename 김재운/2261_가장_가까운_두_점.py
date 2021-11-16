from sys import stdin

n = int(stdin.readline())

pl = [list(map(int, stdin.readline().split())) for _ in range(n)]

# x축 기준 정렬
pl.sort()

minDist = min(dac(start, mid), dac(mid, end))

# x축 기준으로 후보 점 찾기
target_pl = []
for i in range(start, end + 1):
    if (pl[mid][0] - pl[i][0]) ** 2 < minDist:
        target_pl.append(pl[i])
        # 여기서 x축 기준으로 거리가
# y축 기준 정렬
target_pl.sort(key=lambda x: x[1])

# y축 기준으로 후보 점들 사이의 거리 비교
t = len(target_pl)
for i in range(t - 1):
    for j in range(i + 1, t):
        if (target_pl[i][1] - target_pl[j][1]) ** 2 < minDist:
            minDist = min(minDist, getDist(target_pl[i], target_pl[j]))
        else:
            break
            # 현재 후보 점이 다음 점과 최소 거리보다 먹
# 두 점 사이 거리 계산 함수
def getDist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1]-p2[1])**2

def dac(start, end):
    # 종료 조건
    # 1. 점 하나의 거리는 없으니 최대값을 리턴
    if end == start:
        return float('inf')

    # 2. 점 두 개 남으면 사이의 거리 리턴
    if end - start == 1:
        return getDist(pl[start], pl[end])


    # 분할정복 실행
    mid = (start + end) // 2먹


