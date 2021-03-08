# 배열에 정수들이 저장되어 있다. 연속적인 구간들 중 그 합이 가장 큰 구간을 찾는 알고리즘을 작성하라.
# 단, 구간의 크기는 1 이상이 허용된다.

MIN = -2 ** 31 - 1
arr = [1,2,3,0,-1,-2,-1,0,1,4,3,2,1,0,-1,-2,-3,-4,2]

# 시간 복잡도 O(n^2)
def partial_sum(arr):
    arr = [0]+arr
    N = len(arr)
    p_sum = [0] * N
    ans = MIN

    # 구간별 합을 구함
    for i in range(1, N):
        p_sum[i] = p_sum[i-1] + arr[i]

    # hi가 5면 p_sum[5]에서 p_sum[1] ~ p_sum[4]까지 다 빼보고 큰거를 ans에 넣음
    for hi in range(1, N):
        for lo in range(1, hi+1):
            ans = max(ans, p_sum[hi] - p_sum[lo-1])
    
    return ans


# 
def divide_conquer(arr):
    n = len(arr)

    def find(lo, hi):
        if lo == hi:
            return arr[lo]
        
        mid  = (lo + hi) // 2


# 시간복잡도 O(n)
def dynamic_programming(arr):

    cache = [None] * len(arr)
    cache[0] = arr[0]

    for i in range(1, len(arr)):
        cache[i] = max(0, cache[i-1]) + arr[i]

    print(max(cache))





    
