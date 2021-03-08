from typing import List, TypeVar

# T라는 타입은 int, str, List[int]값을 갖는다 
T = TypeVar('T', int, str, List[int])

# a는 T타입 b는 T타입이고 T를 반환한다.
def add(a: T, b: T) -> T:
    return a + b



print(add(1, 3)) # [int, int] -> int
print(add('item', '4')) # [str, str] -> str
print(add([1, 2], [3, 4])) # [List[int], List[int]] -> List[int]
# print(add('item', 5)) # Error!