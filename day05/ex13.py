num=10
'''
 reduce() 함수
 
               list, tuple, range
 reduce(함수, iterable 객체, 초기값)
   ㄴ functools 모듈 속에 있음
'''
from functools import reduce

result = reduce(lambda n1, n2 : n1 + n2, [1, 2, 3, 4, 5])
print('result :',result) # result : 15

result = reduce(lambda n1, n2 : n1 + n2, [1, 2, 3, 4, 5], 10)
print('result :',result) # result : 25


list_numbers = [32, 54, 67, 12, 456, 43, 51]

result \
  = reduce(lambda n1, n2 : n1 if n1 >= n2 else n2, list_numbers)
print('result :',result) # result : 456 (max)

result \
  = reduce(lambda n1, n2 : n1 if n1 <= n2 else n2, list_numbers)
print('result :',result) # result : 12 (min)

# 5! <-- 5 * 4 * 3 * 2 * 1
                                          # 1, 2, 3, 4, 5
result = reduce(lambda n1, n2 : n1 * n2, range(1, 6))
print('result :',result) # result : 120

def factorial_number(num):
  return reduce(lambda n1, n2 : n1 * n2, range(1, num+1))

print(factorial_number(5)) # 120










