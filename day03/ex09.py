num = 10

'''
 bool data type :  True(참), False(거짓)
  ㄴ boolean
'''
b1 = True
b2 = False

print(type(b1)) # <class 'bool'>
print(type(b2)) # <class 'bool'>

b3 = 1 == 1
print(b3) # True

'''

"python"	  참
""	        거짓
[1, 2, 3]	  참
[]	        거짓
()	        거짓
{}	        거짓
1	          참
0	          거짓
None	      거짓
'''

number = 111
print(type(number)) # <class 'int'>
number2 = 12.34
print(type(number2)) # <class 'float'>

result = bool(number)
print(result)  # True
number = 0
result = bool(number)
print(result)  # False
print(bool([1, 2, 3]))
print(bool([])) # False
print(bool(-654)) # True

print(int(True))  # 1
print(int(False)) # 0

print('python' == 'python')
print('python' == 'Python')
print('python' != 'Python')

print(1 == 1.0)

list_num1 = [1, 2, 3]
list_num2 = list_num1
list_num3 = [1, 2, 3]

print(list_num1 is list_num2)  # True
print(list_num1 is list_num3)  # False

print(list_num1 == list_num2)  # True
print(list_num1 == list_num3)  # True

print(list_num1 != list_num2)  # False
print(list_num1 != list_num3)  # False

print(list_num1 is not list_num2)  # False
print(list_num1 is not list_num3)  # True