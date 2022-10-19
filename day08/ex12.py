num=10
'''
예외처리

 예외 : 
 프로그램 오류 중에서 code를 수정함으로 해서
 고칠 수 있는 비교적 가벼운 오류
 
 에러 : 
 프로그램 오류 중에서 code를 수정함으로 해서
 고칠 수 없는 오류
 
'''

def divide(number):
  return 100 // number

print(divide(2))
print(divide(5))
# ZeroDivisionError: integer division or modulo by zero
# print(divide(0))

'''
예외처리 : Exception Handling
  ㄴ 프로그램의 비정상적인 종료를 막아주고
     정상적으로 종료하도록 하는 것

try - except 구문

try: 
  예외가 발생할 가능성이 있는 code
except:
  예외가 발생하면 처리해 주는 code  

'''
try:
  number_division = int(input('숫자를 입력하세요 : '))
  result = 100 / number_division
  print(result)
except:
  print("예외가 발생했습니다")



print("프로그램 종료")






