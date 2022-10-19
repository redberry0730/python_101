num = 12
'''
숫자 하나를 입력받아서
그 수에 20을 더해서 출력하세요

숫자 하나를 입력받아서
그 수가 홀수인지 짝수인지 출력하세요
'''
num = int(input("숫자 하나를 입력하세요 : "))
print(num + 20)

num = int(input("숫자 하나를 입력하세요 : "))
if num % 2 == 0:
  print(num,'은 짝수입니다')
else:
  print(num,'은 홀수입니다')

