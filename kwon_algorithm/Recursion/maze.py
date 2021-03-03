# https://youtu.be/m6lXDsx7oCk
# 권오흠교수님 미로찾기

# 미로의 기본 알고리즘
# 현재 위치가 출구이거나
# 혹은 이웃한 셀들 중 하나에서 현재 위치를 지나지 않고 출구까지 가는 경로가 있거나

# Decision problem 
# 어떤 위치의 x,y를 좌표로 표현

# def findpath(x,y):
# if wall or visited cell:
#   return false
# 도착지면 빠져나감
# if x == 2 and y == 2:
#     return true
# else:
    # 인접한 셀들을 확인
    # mark (x,y) as a visited cell
    # for eah neighbouring cell (x', y') of (x,y) do
    #   if (x', y') is path and x' != x and y' != y':
    #       if findPath(x', y'):
    #           return true
# 모든길이 막혔다면
# return false


N=8
maze = [
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 0]
]

PATHWAY = 0
WALL = 1
# 이미 길이 아닌게 검증됨
BLOCKED = 2
# 막혔는지 아직 검증이 안됨
PATH = 3

endX = N-1
endY = N-1

def findMaze(x, y):
    if x < 0 or y < 0 or x >= N or y >= N:
        return False
    elif maze[x][y] != PATHWAY:
        return False
    elif x == endX and y == endY:
        maze[x][y] = PATH
        return True
    else:
        maze[x][y] = PATH
        if findMaze(x-1, y) or findMaze(x, y-1) or findMaze(x+1, y) or findMaze(x, y+1):
            return True
        else:
            maze[x][y] = BLOCKED
            return False

findMaze(0, 0)
for i in range(N):
    for j in range(N):
        print(maze[i][j], end=" ")
    print()
    
        
