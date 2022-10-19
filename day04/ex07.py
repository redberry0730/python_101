num = 0
'''
      통신사
011    SKT
016     KT
019   LGU+
010     ?

휴대전화번호를 입력받아서
어느 통신사인지 출력하세요

[입력예] 011-6539-9865
[출력예] SKT 사용자입니다 
[힌트] split() 사용

'''
phonenumber = input("전화번호를 입력하세요 : ")
p_number = phonenumber.split("-")[0]
company = "";

if p_number == "011":
  company = "SKT"
elif p_number == "016":
  company = "KT"
elif p_number == "019":
  company = "LGU+"
else:
  company = "?"

if company != "?":
  print(f"{company} 사용자입니다")
else:
  print("없는 통신사입니다")
