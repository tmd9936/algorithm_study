import math

# f(x) = 0.5x + 0.1
def getF(x: float) -> float:
    a = 0.5
    b = 0.1
    return a*x + b

print(getF(1.3))


# x가 1만큼 변하면 f가 얼마나 변하는가
# 한점에서의 변화량을 구하기 lim(△x ->0) △f/△x  = df/dx(x)

# x가 부분에서의 증가량
# df/dx(x) = (f(x + △x) - f(x)) / △x

# 프로그램안에서의 미분 
# Analytical differentiation = 미분표에 나와있는데로 함수 작성

# 자주 사용되는 미분표
# https://en.wikipedia.org/wiki/Activation_function

# f(x) = x /  f'(x) = 1
def getIdentity(x: float) -> float:
    return x

def getGradIndentity(x: float) -> float:
    return 1


# 시그모이드, 로지스틱
def getSigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))

def getGradSigmoid(x: float) -> float:
    f = getSigmoid(x)
    return f * (1.0 - f)

# ReLU
def getReLU(x: float) -> float:
    return x if x >= 0.0 else 0.0

def getGradReLU(x: float) -> float:
    return 0 if x < 0 else 1