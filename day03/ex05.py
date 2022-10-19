num = 10

'''
 dictionary data type

 data 를 key 와 value  한 쌍으로 저장함
 이런 형식으로 하나 이상의 data 쌍을 
 저장하는 data type
 
 index 는 없고 
 value(data) 는 key 에 의해서 구분됨
 
 ㄴ key 는 중복을 허용하지 X : immutable type
 ㄴ value 는 중복을 허용함   : mutable, immutable

'''
dict_empty = {}

dict_info = {'name':'이순신','phone':'01023659887', 'birth':'0428'}
print('이름 :',dict_info['name'])
print('전화 :',dict_info['phone'])
print('생일 :',dict_info['birth'])

dict_num = {1:'이순신', 2:'안중근', 3:'유관순'}

dict_market = {
               '0501': [10500, 10100, 10800, 10600],
               '0502': [10100, 10000, 10500, 10200],
               '0503': [10300, 10100, 10900, 10300]
              }

dict1 = {1 :'hello'}
dict2 = {2 : [1, 2, 3]}
print(dict2[2])

print(dict_market['0502'])

print(dict1)  # {1: 'hello'}

# dictionary 에 data 추가하기
dict1['name'] = '사임당'
print(dict1)  # {1: 'hello', 'name': '사임당'}

print(dict_market)
# 추가
dict_market['0504'] = [10100, 10000, 10500, 10200]
print(dict_market)
# 수정
dict_market['0503'] = [10100, 10000, 10500, 10200]
print(dict_market)

'''
dictionary 는 key 의 중복을 허용하지 않고
key 를 중복하고 value 를 다르게 지정하면
나중에 지장한 값만 저장됨 
'''
dict_fruits = {11:'strawberry', 11:'apple'}
print(dict_fruits)

greeting = "hello"
print(greeting)
print(greeting + ", everybody")

list_nums = [1, 2, 3]
list_nums.append(4)
print(list_nums)

dict_student = {
                 'name':['이순신','안중근','유관순'],
                 'addr':['마포구','강남구','강북구'],
                 'age':[48, 30, 19]
               }
dict_student['grade'] = [4, 3, 2]
print(dict_student)

print(dict_student.keys())

print(type(dict_student.keys()))
# <class 'dict_keys'>

list_keys = list(dict_student.keys())
print(list_keys)
print(type(list_keys))
# <class 'list'>

print(dict_student.values())
print(type(dict_student.values()))
# <class 'dict_values'>

list_values = list(dict_student.values())
print(list_values)
print(type(list_values))



print(dict_student.get('name'))
print(type(dict_student.get('name')))
# <class 'list'>

print(dict_student.get('grade'))
print(type(dict_student.get('grade')))
# <class 'list'>

print('grade' in dict_student)
print('name' in dict_student)
print('weight' in dict_student) #False

# dictionary 의 내용(data) 전체를 삭제함
dict_student.clear()
print(dict_student)

'''
pop(key) : 지정된(key) 키-값을 삭제함
'''
dict_student =  {1: 300, 2: 500, 3: 190, 4: 185, 5: 175, 6: 179, 7: 188}
print(dict_student.pop(2)) # 500
print(dict_student)
'''
pop(8, 10000) : 10000 <-- default (기본값)
dictionary에 없는 키를 지정해서 pop()을 실행하면
해당 key-value 가 없으므로 오류가 발생함
pop(8, 10000) 이런 형식으로 default(기본값) 10000을
설정하면 default(기본값) 을 return 함

'''
print(dict_student.pop(8, 10000))
print(dict_student)

del dict_student[7]
print(dict_student)

# {1: 300, 3: 190, 4: 185, 5: 175, 6: 179}
'''
popitem() : 맨 뒤에 있는 key-value 가 삭제됨
 cf) python v3.5 이하에서는 임의의 key-value 가 삭제됨
'''
dict_pop = dict_student.popitem()
print(dict_pop)
print(type(dict_pop))  # <class 'tuple'>
print(dict_student)

print(dict_student.keys())
print(dict_student.values())

'''
items() : 키와 값(value)이 tuple type으로 됨
                         <class 'tuple'>
'''
print(dict_student.items())
print(list(dict_student.items()))

print(list(dict_student.items())[0])

print(type(list(dict_student.items())[0]))
# <class 'tuple'>

'''
  list(tuple)를 dictionary 로 만들기
  
  dict.fromkeys(list(tuple))
  
'''
list_keys = ['a','b','c','d']

dict_list_keys = dict.fromkeys(list_keys)
print(dict_list_keys)

dict_list_keys2 = dict.fromkeys(list_keys, 333)
print(dict_list_keys2)
# {'a': 333, 'b': 333, 'c': 333, 'd': 333}

print(dict_list_keys2['c'])
# KeyError: 'f'
# print(dict_list_keys2['f'])

'''
 defaultdict() from collections

'''
from collections import defaultdict

dict_default = defaultdict(int)
print(dict_default)
print(dict_default['a'])  # 0

int('1234')  # <-- 1234
print(int())  # 0

print(dict_default[1])  # 0
print(dict_default)

dict_language = defaultdict(lambda : 'python')
print(dict_language['a'])
