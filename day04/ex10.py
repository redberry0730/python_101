num=0
'''
주민등록번호를 입력받아서
어느 지역 출신인지 출력하세요

주민등록번호 8~9 번째 자리수

서울특별시 : 00~08
부산광역시 : 09~12
인천광역시 : 13~15
경기도 내 주요 도시 16~18
경기도 내 기타 지역 19~25
강원도 : 26~34
충청북도 : 35~39
대전광역시 : 40~41
충청남도 : 42~43, 45~47
세종특별자치시 : 44, 96[29]
전라북도 : 48~54
전라남도 : 55~64
광주광역시 : (구)55, 56 (신)65, 66
대구광역시 : 67~70
경상북도 : 71~81
경상남도 : 82~84, 86~91
울산광역시 : 85, 90[30]
제주특별자치도 : 92~95

# 910216-2079845

서울특별시 : 00~08
부산광역시 : 09~12
광주광역시 : (구)55, 56 (신)65, 66
'''

pn =  input("주민등록번호를 입력하세요 : ")
pn = pn.split("-")[1]
loc_number = int(pn[1:3])
location = ""

seoul = list(range(9))
pusan = list(range(9, 13))
kwangju = [55,56,65,66]
loc = ["서울","부산","광주"]

if loc_number in seoul:
  location = loc[0]
elif loc_number in pusan:
  location = loc[1]
elif loc_number in kwangju:
  location = loc[2]
else:
  location = "?"

if location != "?":
  print(f"당신은 {location} 에 거주하고 있습니다")
else:
  print("주민등록번호를 바르게 입력해 주세요")





