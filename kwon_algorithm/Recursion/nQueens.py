# N개의 말을 놓아야 하는데 어떤 말도 같은 행, 열, 대각선에 있으면 안됨
# 백트래킹과 상태공간 트리를 이용
# 백트래킹 : 상태공간 트리를 깊이 우선 방식으로 탐색하여 해를 찾는 알고리즘을 말한다.
# 상태공간트리 : 찾는 해를 포함하는 트리
#               즉 해가 존재한다면 그것은 반드시 이 트리의 어떤 한 노드에 해당함
#               따라서 이트리를 체계적으로 탐색하면 해를 구할 수 있음

# 상태공간 트리의 모든 노드를 탐색해야 하는 것은 아님
# 예를들어 이미 충돌된 경우 즉 다음 노드가 오류인 경우에는 오류 다음을 탐색 할 필요가 없음 

# 수도 코드
# 노드에 도착한 순간 실행되는 코드라고 생각하면 됨
# def queens ( arguments ):
#     # 이미 오류인 곳이라서 내려갈 필요가 있는 노드인가 확인
#     if non-promising:
#         report failure
#     # 내가 찾고있는 노드인가
#     elif success:
#         report answer and return
#     # 그렇지 않다면 자식 노드들을 탐색
#     else:
#         visit children recursively

# N = 4
# # 1번말이 놓은 열 번호
# cols = [0] * (N+1)
# # level = 트리의 깊이
# def queens(level):
#     if promising(level) is False:
#         return False
#     elif (level == N):
#         for i in range(1, N+1):
#             print(str(i) + "," + str(cols[i]))
#         return True
#     else:
#         for i in range(1, N+1):
#             cols[level+1] = i
#             if (queens(level+1)):
#                 return True
#         return False

# # 전의 말들 간에는 충돌이 없음(즉 이미 충돌 검사가 끝난 상태)
# # 따라서 마지막에 놓인 말이 이전에 놓은 다른 말들과 충돌하는지 검사하는 것으로도 충분함
# def promising(level):
#     for i in range(1, level):
#         # 같은 세로라인에 있는지 검사
#         if cols[i] == cols[level]:
#             return False
#         # 같은 대각선에 위치하는지 검사
#         elif (level - i) == abs(cols[level] - cols[i]):
#             return False
#     return True

# queens(0)



N = 8
# 가로
cols = [0] * (N+1)

# level = 세로
def queens2(level):
    # 같은 위치가 있는지 확인
    if promising(level) is False:
        return False
    # 목표한 개수에 도달하면 끝
    elif level == N:
        for i in range(1, N+1):
            print("{0}, {1}".format(i, cols[i]))
        return True
    else:
        # 깊이 탐색
        for i in range(1, N+1):
            cols[level + 1] = i
            if queens2(level+1):
                return True
        return False
    

def promising(level):
    # 해당 레벨과 전의 값들을 비교
    for i in range(1, level):
        # 같은 세로선상이면 지우기
        if cols[level] == cols[i]:
            return False
        elif (level - i) == abs(cols[level] - cols[i]):
            return False
    return True

queens2(0)
