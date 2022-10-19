num1 = 11
num2 = 22
result = num1 + num2
print('result :',result)
print('result : ' + str(result))

# 주석(메모) : python interpreter 가 읽지 않는 부분
# 한 줄 주석
'''
 여러 줄
 주석
 입니다
'''
'''
변수 : 1) data 를 저장한 공간에 붙이는 이름표
       2) data 를 저장한 공간
       
       number1 = 111
       1) 변수 <--  number1
       2) 변수 <--  number1이라는 이름표가 붙은 공간
       
변수를 사용하는 이유
 data 가 RAM 에 저장될 때
 RAM 에 이미 정해진 어떤 주소지에 저장이 되는데
 computer 는 이 주소지로 data 의 위치를 파악함
 이 data 를 활용하려면 이 주소를 computer 에게
 알려줘야 하는데... 이 주소를 사용하는 것이 어려워서
 대신 '변수' 라는 이름표를 사용함 
 (cf. 도메인주소)
       
 data type 
 자료  형(태) : 자료형
 
 type : 형
 
'''

number = 11
print('number :', number)
print('type(number) :', type(number))
# type(number) : <class 'int'>
# int : 숫자 - 정수형

number2 = 3.1415
print('number2 :',number2)
print('type(number2) :',type(number2))
# type(number2) : <class 'float'>
# float : 숫자 - 실수형

num3 = 5.12E10
num4 = 5.12e-10
# E(e) : exponent - 지수

'''
 8 진수 :  숫자0++알파벳O(o) - 0o214
 octal
'''
num_8 = 0o214
print('num_8 :',num_8)
# num_8 : 140

'''
 16 진수 : 숫자0++알파벳X(x) - 0x214
 Hexadecimal
'''
num_16 = 0x214
print('num_16 :',num_16)
# num_16 : 532

'''
 숫자형 ( int, float ) 에서 사용하는 연산자
 + - * / (//) % 
'''
a = 10
b = 8
rs1 = a + b
rs2 = a - b
rs3 = a * b
rs4 = a / b
rs5 = a // b
rs6 = a % b
print('rs1 (+)  :', rs1)
print('rs2 (-)  :', rs2)
print('rs3 (*)  :', rs3)
print('rs4 (/)  :', rs4)
print('rs5 (//) :', rs5)
print('rs6 (%)  :', rs6)
'''
rs1 (+)  : 18
rs2 (-)  : 2
rs3 (*)  : 80
rs4 (/)  : 1.25  - 실수 반환(return)
rs5 (//) : 1     - 정수(몫) 반환(return) - 반올림 X
rs6 (%)  : 2     - 정수(나머지) 반환(return) 
'''

c = 2
d = 5
rs7 = c ** d
print('rs7 :',rs7)
# rs7 : 32


