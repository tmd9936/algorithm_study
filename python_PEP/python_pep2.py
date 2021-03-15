# 데이터 이어 붙히기
my_list = [['A', 'B'], ['X', 'Y'], ['1']]

answer = sum(my_list, [])

import itertools

list(itertools.chain.from_iterable(my_list))

list(itertools.chain(*my_list))

pp = [element for array in my_list for element in array]
print(pp)

from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

import operator
list(reduce(operator.add, my_list))


