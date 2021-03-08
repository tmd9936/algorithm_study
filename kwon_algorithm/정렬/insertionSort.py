# 한 원소를 기준으로 그 자리에 끼워 넣기
# 시간복잡도 T(n) = (n-1) + (n-2) + ... + 2 + 1 = O(n^2)
data = [29, 10, 14, 37, 13]

for i in range(1, len(data)):
    item = data[i]
    for j in range(i-1, -1, -1):
        if item < data[j]:
            data[j+1] = data[j]
        else:
            data[j+1] = item
            break
    else:
        data[0] = item

print(data) 


i = 2
j = 1, 0