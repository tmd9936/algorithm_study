# 제일 큰 값을 찾아서 끝자리에 놓기
# 시간복잡도 T(n) = (n-1) + (n-2) + ... +2+1 = O(n^2)
data = [29, 10, 14, 37, 13]

for i in range(len(data)):
    mx = 0
    index = 0
    for j in range(len(data) - i):
        if data[j] > mx:
            mx = data[j]
            index = j
    tmp = data[len(data) - i - 1]
    data[len(data) - i - 1] = mx
    data[index] = tmp

print(data)
