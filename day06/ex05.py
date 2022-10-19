num=10
'''
divmod(분자, 분모) : divmod(10, 8) --> 몫, 나머지
'''
print(divmod(10, 8))  # (1, 2)

'''
enumerate() : 열거함수
 ㄴ sequential type 을 입력 받아서
      ㄴ list, tuple, str
    index 값과 data 를 반환함
'''
list_fruits = ['strawberry','peach','banana','mango']

for fruit in list_fruits:
  print(fruit)
print("--------------------------------")

for idx, fruit in enumerate(list_fruits):
  print(idx, fruit)
print("--------------------------------")

'''
eval('표현식') : '표현식'의 결과를 반환함
'''
print(eval('1 + 2'))  # 3
print(divmod(10, 8))
print('divmod(10, 8)')
print(eval('divmod(10, 8)'))
print("--------------------------------")

'''
hex() : 정수를 입력받아서 16진수로 반환함
'''
print(hex(32)) # 0x20
print("--------------------------------")

'''
id() : 객체의 주소를 반환함
'''
a = 10
print(a)
print(id(a))
print("--------------------------------")

# immutable :  원본이 변형되지 않음
str1 = "hello"
print('str1 에 + " everybody" 하기 전')
print('str1 :',str1)
print('str1 :',id(str1))
str2 = str1 + " everybody"
print('str1 에 + " everybody" 한 후')
print('str1 :',str1)
print('str2 :',str2)
print('str2 :',id(str2))
print("--------------------------------")


# mutable :  원본이 변형됨
list_numbers = [1, 2, 3]
print('list_numbers :',list_numbers)
print('list_numbers :',id(list_numbers))

list_numbers.append(4)
print('list_numbers :',list_numbers)
print('list_numbers :',id(list_numbers))