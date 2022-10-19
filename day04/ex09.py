num=0
'''
주민등록번호(-)를 입력받아서
남자인지 여자인지 출력하세요

[입력예] 950123-1625987

7 번째 자리수
9 : 1800 - 남자
0 : 1800 - 여자
1, 3 : 남자
2, 4 : 여자
5, 7 : 외국인 남자
6, 8 : 외국인 여자
'''
950123-1625987
pn = input("주민등록번호를 입력하세요 : ")
pn = pn.split("-")[1]
gender = ""
if pn[0] == "1" or pn[0] == "3":
  gender = "남자"
elif pn[0] == "2" or pn[0] == "4":
  gender = "여자"
elif pn[0] == "5" or pn[0] == "7":
  gender = "외국인남자"
elif pn[0] == "6" or pn[0] == "8":
  gender = "외국인여자"
else:
  gender = "?"

if gender != "?":
  print(f"당신은 {gender}입니다")
else:
  print("주민등록번호를 바르게 입력해 주세요")




