num = 10
'''
isinstance(변수, 클래스이름) : True, False

 클래스 : data 를 메모리에 loading 시킬 때
          어떤 구성(모양)으로 loading 할지를
          설명해 놓은 소스 - 설계도
 객체(Object, instance)
        : 클래스에 설명해 놓은대로 
          메모리에 loading 되어서 
          활성화된 상태의 data - 실체
'''
class Person:
  # code....
  pass

class Student:
  pass

p1 = Person()
s1 = Student()
p2 = Person()
s2 = Student()
p3 = Person()
s3 = Student()
p4 = Person()
s4 = Student()

'''
isinstance(변수, 클래스이름) : True, False
'''
print(isinstance(s3, Student))
print(isinstance(p1, Student))
print("----------------------------")

'''
max(), min()
'''
list_number2 = [1, 2, 3, 4, 5]
print(max(list_number2))
print(min(list_number2))
print("----------------------------")

'''
oct(십진수 정수) -- > 8진수
'''
print(oct(34)) # 0o42
print("----------------------------")

'''
open, map, filter
'''

'''
pow(밑, 지수)
'''
print(pow(2, 3)) # 8
print("----------------------------")

'''
round(숫자)  :  반올림 함수
'''
print(round(5.3))
print(round(5.7))

print(round(3.14159, 4))
print(round(3.14159, 3))
print(round(3.14159)) # 3
print(round(3.141592)) # 3
print(round(3.641592)) # 4
print("----------------------------")

'''
sorted(정렬할 data) - 내장 함수 :  
                      정렬 후 새로운 객체 생성
                        ㄴ 원데이터를 변형하지 않음          
[list.]sort() - 리스트 클래스의 메소드
                   ㄴ 원데이터를 변형함 
                   
reverse() : 역정렬
                   
'''
list_nums = [11, 8, 2, 3]
print('list_nums ;',list_nums)

print('sorted(list_nums) :',sorted(list_nums))
print('list_nums ;',list_nums)

print('list_nums :',list_nums)
print('list_nums :',id(list_nums))
 # [11, 8, 2, 3] --> [2, 3, 8, 11]
list_nums.sort() # 원본이 변형됨 : 원본이 정렬됨
print('list_nums :',list_nums)
print('list_nums :',id(list_nums))

num = 11
print(type(num)) # <class 'int'>

print(list_nums) # [2, 3, 8, 11]
list_nums = [11, 8, 2, 3]
print(list_nums) #  [11, 8, 2, 3]
list_nums.reverse()
print(list_nums) #  [3, 2, 8, 11]


'''
sum(), srt(), int(), float(), list(), tuple()
'''

'''
zip(list1, list2)
'''
list1 = [1, 2, 3]
list2 = ['1', '2', '3']

print(list(zip(list1, list2)))
# [(1, '1'), (2, '2'), (3, '3')]
