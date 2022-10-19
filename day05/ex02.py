
num1 = 11
num2 = 22
number1 = 33
number2 = 44

'''
1) 매개변수 없는 함수
  1_1) return 값도 없는 함수
  1_2) return 값이 있는 함수
2) 매개변수 있는 함수
  1_1) return 값이 없는 함수
  1_2) return 값도 있는 함수

'''

def add(num1, num2):
  print('num1 :',num1,'-- num2 :',num2)
  return num1 + num2

print('add(number1, number2) :',add(number1, number2))
print('add(number2, number1) :',add(number2, number1))

result = add(num1, num2)
print('result :',result)

result = add(add(num1, num2), number1);
print('result :',result)

def multiply(n1, n2):
  return n1 * n2

result = multiply(num1, 2)
print('result :',result)

result = multiply(add(num1, num2), 2)
print('result :',result)

result = add(multiply(num1, num2), 2)
print('result :',result)


def add(num1, num2):
  print('num1 :',num1,'-- num2 :',num2)
  return num1 + num2


add(11, 22)
add(101, 202)
add(115, 225)

add(num2=123, num1=456)

