# 시간 복잡도 T(n) = T(n-1) + T(n-2) + 1
# < 2T(n-1) + 1
# < O(2^n)

def fibo(num):
    if num <= 2:
        return num
    else:
        return fibo(num-1) + fibo(num-2)