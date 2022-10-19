num = 10
'''
try:
  예외가 발생할만한 code
except:
  예외처리부분 - 예외발생시 실행하는 부분  
else:
  예외가 발생하지 않았을 때 실행하는 code
'''
try:
  number = int(input('숫자를 입력하세요 : '))
  result = 10 / number
except ZeroDivisionError as e:
  print(e)
else:
  print('예외가 발생하지 않은 경우에 실되는 code')
  print('result :',result)

print('프로그램 종료')




