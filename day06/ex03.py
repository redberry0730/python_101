'''
아래의 code 를 실행했을 때
출력되는 결과는?
'''
def add_5(number):
  return number + 5

num1 = add_5(20)
num2 = add_5(num1)
num3 = add_5(num2)
print(num3)

result = add_5(add_5(add_5(20)))
print(result)
print("--------------------------------------------")

def add_7(number):
  return number + 7
def double_number(number):
  return number * 2

result1 = add_7(12)
result2 = double_number(result1)

print(result2)
print("--------------------------")

def double_num(number):
  return number * 2
def func1(number):
  return double_num(number + 2)
def func2(number):
  number += 20
  return func1(number)

print(func2(22))



