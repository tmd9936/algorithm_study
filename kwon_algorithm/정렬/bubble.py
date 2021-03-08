# 두 값을 계속비교 하면서 자리바꾸면서 마지막 값까지 가기
# 시간복잡도 T(n) = (n-1) + (n-2) + ... + 2 + 1 = O(n^2)
data = [29, 10, 14, 37, 13]

for i in range(len(data)):
    for j in range(len(data) - i - 1):
        if data[j] > data[j+1]:
            tmp = data[j]
            data[j] = data[j+1]
            data[j+1] = tmp

print(data)