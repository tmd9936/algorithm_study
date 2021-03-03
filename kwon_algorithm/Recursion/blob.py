# binary 이미지
# 서로 연결된 image를 blob이라고 함

# 현재 픽셀이 속한 blob의 크기를 카운트 하려면
# 현재 픽셍이 image color가 아니면
#   0을 반환한다
# 현재 픽셀 == image color
#   현재 픽셀을 카운트 한다
#   중복 카운트 방지를 위해 다른 색으로 칠한다
#   현재 픽셀에 이웃한 모든 픽셀들에 대해서
#       그 픽셀이 속한 blob의 크기를 카운트하여 카운터에 더해준다.
#   카운트를 반환한다.

pixels = [[1, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 0, 1, 1, 1]]

N = 8

NO_COLOR = 0
IMAGE_COLOR = 1
COUNT_COLOR = 2

def blob(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0
    elif pixels[x][y] != IMAGE_COLOR:
        return 0
    else:
        pixels[x][y] = COUNT_COLOR
        return 1 + blob(x-1, y+1) + blob(x, y+1) + blob(x+1, y+1)+ blob(x-1, y) + blob(x+1, y) + blob(x-1, y-1) + blob(x, y-1) + blob(x+1, y-1) 


result = blob(3, 5)
print(result) 

# 시간복잡도?
# T(n) = 8T(n-1) + 1
#  < T(n) = 8^nT(1) + n
#  < O(8^n)