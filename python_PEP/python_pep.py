data = [[1,2], [3,4]]

# 각각 list의 길이를 출력

# a, b = map(int, input().split(' '))

def solution(mylist):
    return list(map(len, mylist))

print(solution(data))

# 몫과 나머지
# 일반적
a = 7
b = 5
print(a//b, a%b)

# unpacking
print(*divmod(a, b))

# 10진법으로 변환
num = '3212'
base = 5
answer = int(num, base)

# 왼쪽, 오른쪽, 가운데 정렬
text = 'abc'
n = 10
print(text.ljust(n))
print(text.rjust(n))
print(text.center(n))

# 알파벳 출력
import string

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789

# zip

list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]

for number1, number2, number3 in zip(list1, list2, list3):
   print(number1 + number2 + number3)

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(*mylist)


# zip 함수에 서로 길이가 다른 리스트가 인자로 들어오는 경우에는 
# 길이가 짧은 쪽 까지만 이터레이션이 이루어집니다
def solution2(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer

mylist = [83, 48, 13, 4, 71, 11]    
print(solution2(mylist))

# 이어 붙히기
pp = ['123','4','56']

print(''.join(pp))

# 곱집합(조합)
import itertools

iter1 = 'ABCD'
iter2 = 'xy'
iter3 = '1234'
print(list(itertools.product(iter1, iter2, iter3)))