num=10
'''
현재 가격을 입력받아서 <-- 매개변수
30% 인상된 가격을 출력하는
함수를 작성하고 실행하세요
'''

def print_price_30(price):
  return price * 1.3

price = int(input("현재 가격을 입력하세요 : "))
print(print_price_30(price),'원')
print("------------------------------------------")

'''
두 개의 정수를 입력 받아서
덧셈, 뺄셈, 곱셈, 나눗셈 의 
결과를 출력하는 함수를 작성하세요

결과를 반환하는 함수를 작성하세요
 ㄴ 반환된 값을 출력하세요
'''

def print_calc(num1, num2):
  print(num1 + num2)
  print(num1 - num2)
  print(num1 * num2)
  print(num1 / num2)

print_calc(10, 8)
print("------------------------------------------")

def print_calc2(num1, num2):
  return (num1 + num2), (num1 - num2), (num1 * num2), (num1 / num2)

result = print_calc2(10, 8)
add, subtract, multiplication, division = result
print(add)
print(subtract)
print(multiplication)
print(division)
