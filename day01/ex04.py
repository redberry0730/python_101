'''
 나머지 연산자 : % <-- 배수 판별
 몫            : //

 2의 배수 - 어떤 수를 2로 나눈 나머지가 0
 3의 배수 - 어떤 수를 3로 나눈 나머지가 0
 7의 배수 - 어떤 수를 7로 나눈 나머지가 0
'''

number = 168
rs_2 = number % 2
rs_3 = number % 3
rs_7 = number % 7

print('rs_2 :', rs_2)
print('rs_3 :', rs_3)
print('rs_7 :', rs_7)

'''
rs_2 : 0
rs_3 : 0
rs_7 : 0
 ㄴ 168은 2의 배수(짝수)도 되고
 ㄴ 168은 3의 배수도 되고
 ㄴ 168은 7의 배수도 됨
'''

number1 = 10
number2 = 6

result = number1 ** 2
print('result :', result)

print('number1 == number2 :',number1 == number2)
# number1 == number2 : False
print('number1 != number2 :',number1 != number2)
# number1 != number2 : True

result = number1 >= 10 and number2 <= 50
print('result :',result)

result = 10 <= number1 <= 50
print('result :',result)

print(number1 >= 50)
print(not(number1 >= 50))

print(number1 == 10)
print(number1 != 10)














