num = 10

'''
  str(문자열), list, tuple, range
  
  data 가 연속적으로 저장되어있음
           ㄴ index 번호가 자동 부여됨
           
  시퀀스 자료형 (Sequence data type)
     str(문자열), list, tuple, range

'''

list_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('5 in list_nums :',5 in list_nums)
print('15 in list_nums :',15 in list_nums)
print('15 not in list_nums :',15 not in list_nums)

print(4 in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(33 in (11, 22, 33, 44, 55))
print(4 in range(10))
print('o' in 'python')

list_add = [1, 2, 3, 4] + [5, 6, 7, 8]
print(list_add)
tuple_add = (1, 2, 3, 4) + (5, 6, 7, 8)
print(tuple_add)
str_add = 'hello' + ' python'
str_add2 = 'hello' + str(12)
str_add3 = 'hello' + str(12.56)
print(str_add)
print(str_add2)
print(str_add3)
'''
unsupported operand type(s) for +: 'range' and 'range'
range_add = range(1,6) + range(6,11)
print(range_add)
'''
list_range_add = list(range(1, 6)) + list(range(6, 11))
print(list_range_add)
tuple_range_add = tuple(range(1, 6)) + tuple(range(6, 11))
print(tuple_range_add)

str1 = 'hello'
print(str1 * 3)
list1 = [1,2,3]
print(list1 * 3)
tuple1 = (1, 2, 3)
print(tuple1 * 3)

'''
unsupported operand type(s) for *: 'range' and 'int'
range1 = range(1, 4)
print(range1 * 3)
'''
range1 = range(1, 4)
print(list(range1) * 3)
print(tuple(range1) * 3)


print(len(list_add))
print(len(tuple_add))
print(len(str_add))

greeting_kor =  "안녕하세요"
print(len(greeting_kor))
print(len(greeting_kor.encode('utf-8')))

greeting_eng = "hello"
print(len(greeting_eng))
print(len(greeting_eng.encode('utf-8')))

