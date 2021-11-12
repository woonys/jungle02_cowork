import sys
input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split(' ')))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split(' ')))


left = 0
right = len(n_list) - 1
def find_number (n_list, num, left, right): # n_list의 가장 오른쪽 값 = 리스트길이 - 1 해준다. (인덱스가 1 작으니까)
    if left > right: #재귀 종결 조건
        return 0
    
    mid = (left + right) // 2
    if num == n_list[mid]: #n리스트의 mid숫자가 몇번째에 있는 지의 인덱스값과 num비교
        return 1
    elif num > n_list[mid]:
        left = mid + 1
        return find_number (n_list, num, left, right)
    elif num < n_list[mid]: 
        right = mid - 1
        return find_number (n_list, num, left, right)
    
for i in m_list:
    print(find_number(n_list, i, left, right)) #시작값. m_list의 값들을 i로 받아옴
                                #윗부분에 left, right 안쓰고 0, n-1 로 시작했어도 됨.




    
    # for num in m_list:
    #     while left<=right:
    #         mid = (left + right) // 2 #구한 중간 값을 인덱스로 하여 첫번째 리스트에서 가져온 값이 두번째 각 값과 같으면 1출력
    #         if num == n_list[mid]: #n리스트의 mid숫자가 몇번째에 있는 지의 인덱스값과 num비교
    #             return 1
    #         elif num > n_list[mid]:
    #             left = mid + 1
    #         elif num < n_list[mid]: 
    #             right = mid - 1
            
    #     if left > right:
    #         return 0
        
# for i in range(len(m_list)):
#     print(find_number(n_list, left, right)) #시작값

#출력 오류(None), def 옆에 (), print(0) 안뜸 <-return


#리스트 값을 절반씩 버리면서 해당 숫자를 찾는 이분탐색문제
#첫번째 리스트의 중간값 mid = left+right길이 // 2 로 구하고 왼쪽부터 있는지 비교




#n번째 숫자가 첫번째 리스트 안에 존재하면 1 출력

# while lt<=rt: #반 나눠서 점점 범위 좁혀오다가 lt가 남은rt 거리보다 커져버리면 함수 종결
#     mid=(lt+rt)//2
#     if a[mid]==m:      #a의 미드에 있는 값이 m이니?
#         print(mid+1)  #맞으면 mid출력~ 인덱스 값이니 +1 해줌
#         break
#     elif a[mid]>m:
#         rt=mid-1  #큰쪽(오른쪽) 날림
#     else:
#         lt=mid+1  #왼쪽을 오른쪽으로 가서 범위 좁힘