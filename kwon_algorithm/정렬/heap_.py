# Heap
# complete binary tree 이면서
# heap property를 만족해야함
# complete binary tree : 마지막 레벨을 제외하면 완전히 꽉 차있고,
#                          마지막 레벨에는 가장 오른쪽 부터 연속된 몇 개의 노드가 비어있을 수 있음 
# max heap property : 부모는 자식보다 크거나 같다
# min heap property : 부모는 자식보다 작거나 같다

# 트리 높이 (logn)

# 힙은 일차원 배열로 표현가능: A[1...n]
# 루트 노드 A[1]
# A[i]의 부모 = A[i/2]
# A[i]의 왼쪽 자식 = A[2i]
# A[i]의 오른쪽 자식 = A[2i + 1]

# 각각의 노드의 왼쪽오른쪽 자식과 부모의 인덱스를 빠르게 찾기 가능해서 쓰는 자료구조

# max-heapify : 힙을 할때 정렬을 하기 위한 기본 연산
# 전제조건: complete ginary tree
# 왼쪽 부트리는 그 자체로 heap이고, 오른쪽 부트리도 그 자체로 heap 일 때
# max-heapify의 시간복잡도는 트리의 높이, 그리고 complete tree이기 때문에 
# O(logn)
import heapq

# Recursive 하게
# A: heap, i: 노드
# def max_hepify(A, i):
#     if A[i]가 자식이 있는지 확인 없으면:
#         return
#     k = A[i]보다 인덱스가 큰 자식
#     if A[i] >= A[k]: # A[i]가 자식보다 크다면
#         return 
#     A[i] 와 A[k] 바꿈
#     # 자식 노드에서 다시 변환
#     max_hepify(A, k)
# ----------------------------------------------

# iterative 하게
# def max_hepify(A, i):
#     while A[i]가 자식이 있다면:
#         k = i보다 인덱스가 큰 자식
#         if A[i] >= A[k]:
#             return
#         exchange A[i] and A[k]
#         i = k

# ----------------------------------------------

# 

