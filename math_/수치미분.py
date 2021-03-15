# 직접 미분값 추측하기
# Numerical differentiation
# df/dx(x) -> (f(x + △x) - f(x)) / △x
# = (a(x + △x)^n - an^x)) / △x

# △x를 무한대로 작게는 불가능하니까 적당히 작은 비슷한 값을 넣음

# df/dx(x) -> (f(x + △x) - f(x)) / △x를 이용

import math

# f(x) = 0.5x + 0.1
def getF(x: float) -> float:
    a = 0.5
    b = 0.1
    return a*x + b

# 함수를 모르더라도 미분값을 얻기 가능
x = 1.0
dx = 0.1
df = getF(x + dx) - getF(x)
dfdx = df / dx

# 1. Extrapolation
# 미분과 그 함수의 값을 안다면 x가 다른경우 추측이 가능함(정확한 값은 구하기 어렵지만 추축은 가능함)
# f(x + △x) = f(x) + df/dx*△x
delX = 0.2

# f(x + 0.2)의 값 구하기
ret = getF(x) + dfdx*0.2

# 2. Approximation
# f(x)가 0.7이 되는 값을 알고 싶다면 어느 한 점의 값을 구하고 
# 그점에서 얼마를 증가시키면 원하는 값을 내줄꺼냐
# dx가 작을수록 정확도가 높아짐
# △x = (f(x + △x) - f(x)) / (df/dx(x))

f_target = 0.7
dx_target = (f_target - getF(x)) / dfdx