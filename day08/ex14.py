num=10

'''
예외 메세지 받아오기

try:
  예외가 발생할만한 code
catch 예외이름 as 변수:
  예외 처리 부분  
'''

list_numbers = [10, 20, 30]

try:
  idx, number = map(int, input('리스트 숫자 중 index 번호를 입력하고\n' \
                               '공백 후에 나누는 숫자를 입력하세요 : ').split())
  print(list_numbers[idx] / number)
#   ZeroDivisionError  인 경우
except ZeroDivisionError as e:
  print('숫자를 0으로 나눌 수 없습니다', e)
#    IndexError 인 경우
except IndexError as e:
  print('잘못된 index 번호입니다', e)





