# 분할정복법
# 배열을 다음과 같은 조건이 만족되도록 두 부분으로 나눈다.
# elements in lower parts <= elements in upper parts
# 정복 : 각 부분을 순환적으로 정렬한다.
# 합병 : nothing to do

# 피봇 : 피봇보다 작은것 큰것으로 나눔
# 맨 마지막 수를 기준(pivot)으로 삼는다

# 기준보다 작은 수는 기준의 뇌쪽에 나머지는 기준의 오른쪽에 오도록 재배치(분할) 한다
# 기준의 왼쪽과 오른쪽을 각각 순환적으로 정렬한다

# A[p...r] 까지 정렬
# def quickSort(A[], p, r):
#     if (p < r) then:
#         q = partition(A, p, r) # pivot의 위치 분할의 기준
#         quickSort(A, p, q-1) # 왼쪽 부분배열 정렬
#         quickSort(A, q+1, r) # 오른쪽 부분배열 정렬

# def partition(A[], p, r):
    # 배열 A[p... r]의 원소들을 A[r]을 기준으로 양쪽으로 재배치하고
    # A[r]이 자리한 위치를 return 한다.

    # i는 피봇보다 작은 값들 중 마지막 값
    # j는 지금 검사하려는 값
    # if A[j] >= x:
    #     j <- j+1
    # 피봇보다 작다면 피봇보다 작은 값들 중 마지막값의 다음 값과 바꿈
    # else:
    #     i <- i+1
    #     exchange A[i] and A[j]
    #     j <- j+1

# partition의 시간 복잡도
# O(n) 모든 데이터와 한 번씩 비교

# quichSort의 시간복잡도
# 최악의 경우
# T(n) = T(0) + T(n-1) + 0(n)
#      = T(n - 1) + 0(n)
#      = T(n - 2) + T(n - 1) + 0(n-1) + 0(n)
#      ...
#      = 0(1) + 0(2) + ... + 0(n-1) + 0(n)
#      = 0(n^2)
# 최악은 이미 정렬 되어있을때가 가장 느림 O(n^2) 

# 최선의 경우
# 항상 절반으로 분할되는 경우
# T(n) = 2T(n/2) + 0(n)
#      = O(nlogn)

# 첫번째 값이나 마지막 값을 피봇으로 선택
# - 이미 정렬도니 데이터 혹은 거꾸로 정렬된 데이터가 최악의 경우
# - 현실의 데이터는 랜덤하지 않으므로 (거꾸로) 정렬된 데이터가 입력으로 들어올 가능성은 매우 높음
# - 따라서 좋은 방법이 아니다
# Median of Three
# - 첫번째 값과 마지막 값, 그리고 가운데 값 중에서 중간값(median)을 피봇으로 선택
# - 최악의 경우 시간복잡도가 달라지지는 않음
# Randomized QuickSort
# - 피봇을 랜덤하게 선택
# - no worst case instance, but worst case execution
# 평균 시간복잡도 O(NlogN)

# 징점 : 공간이용이 적다.


def quickSort(data, p, r):
    if p < r:
        q = partition(data, p, r)
        quickSort(data, p, q-1)
        quickSort(data, q+1, r)

    

def partition(data, p, r):
    pivot = data[r]
    i = p-1
    for j in range(p, r):
        if data[j] <= pivot:
            i = i + 1
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
    temp = data[i+1]
    data[i+1] = data[r]
    data[r] = temp
    return i+1


data = [10, 22, 4, 20 , 5, 3, 9, 12, 18, 2, 1]
quickSort(data, 0, len(data)-1)
print(data)

