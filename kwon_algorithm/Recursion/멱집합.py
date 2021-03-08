# 임의의 집함 data의 모든 부분집합을 멱집합
# data = {a, b, c}
# {공, a, b, c, ab, ac, bc, abc}, 2^3 = 8개

# S의 멱집합을 구한 후 각각에 집합 P를 합집합하여 출력하라
# def powerSet(P, S):
#     if S is an empty set:
#         print P
#     else:
#         let t be the first element of S
#         powerSet(P, S-{t}) # t를 뺀 집합의 멱집합을 구함
#         powerSet(PU{t}, S-{t}) #t를 포함한 집합의 멱집합을 구함

# 상태공간트리
# 해를 찾기위해 탐색할 필요가 있는 모든 후보들을 포함하는 트리
# 트리의 모든 노드들을 방문하면 해를 찾을 수 있다.
# 루트에서 출발하여 체계적으로 모든 노드를 방문하는 절차를 기술한다.

data = ['a','b','c','d','e','f']
n = len(data)
include = [False] * n
sets = list()

# k는 트리상에서 현재나의 깊이를 표현한다.
def powerSet(k):
    # 만약 내 위치가 리프노드라면
    if k == n:
        tmp = list()
        for i in range(n):
            # if (include[i]): print("{}".format(data[i]), end=" ")
            if (include[i]): tmp.append(data[i])
        #print()
        sets.append(tmp) 
        return
    # 먼저 외쪽으로 내려갔다가
    include[k] = False
    powerSet(k+1)
    # 오른쪽으로 내려간다.
    include[k] = True
    powerSet(k+1)

powerSet(0)
print(sorted(sets))

# 시간 복잡도
# T(n) = 2T(n-1)
# T(n) = 2^nT(1)
# O(2^n)

## 홀로 체크 해보기
data = ['a','b','c','d','e']
n = len(data)
# 포함된 상태인지 아닌지 체크
include = [False]*n

def pSet(k):
    # 마지막 노드에 도착했을때 
    if k == n:
        for i in range(n):
            if include[i]: print("{} ".format(data[i]), end="")
        print()
        return
    else:
        # 현재 인수를 포함하고 다음 인수로 넘어감
        include[k] = True
        pSet(k+1)
        # 현재 인수를 포함하지 않고 다음 인수로 넘어감
        include[k] = False
        pSet(k+1)
