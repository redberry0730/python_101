list_numbers = [10, 20, 30]

try:
  idx, number = map(int, \
                    input('리스트 숫자 중 index를 입력하고 \n'\
                          '공백 후에 나누는 숫자를 입력하세요 : ').split())
  print(list_numbers[idx] / number)
except ZeroDivisionError:
  print('숫자를 0으로 나눌 수 없습니다')
except IndexError:
  print('index를 다시 입력해 주세요')

print('idx :',idx)

print('프로그램 종료')
