num=10
'''
입력한 문자가 대문자이면 소문자로
소문자이면 대문자로 변환해서 출력하세요

upper()
lower()

isupper()
islower()
'''
char1 = input("문자 하나를 입력하세요 : ")

if char1.islower():
  print(char1.upper())
elif char1.isupper():
  print(char1.lower())
'''  
else:
  print(char1.lower())
'''



