num=0
'''
주민등록번호 유효성 검사

  9 5 0 2 1 6 - 2 0 9 6 5 3 5
X 2 3 4 5 6 7   8 9 2 3 4 5

total % 11 : 11로 나눈 나머지

11 - 11로 나눈 나머지  <-- 마지막 번호
'''
pn = input("주민등록번호를 입력하세요 : ")

total =  int(pn[0]) * 2 + int(pn[1]) * 3 + int(pn[2]) * 4\
       + int(pn[3])* 5 + int(pn[4]) * 6 + int(pn[5]) * 7\
       + int(pn[7]) * 8 + int(pn[8]) * 9 + int(pn[9]) * 2\
       + int(pn[10]) * 3 + int(pn[11]) * 4 + int(pn[12]) * 5

result = 11 - (total % 11)

if int(pn[-1]) == result:
  print("유효한 주민등록번호입니다")
else:
  print("유효하지 않은 주민등록번호입니다")
