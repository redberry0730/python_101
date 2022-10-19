num=10

'''
제어문 (control statement)
  ㄴ 조건문(conditional), 반복문(loop)

 실행문
 실행문
 실행문

 if 조건(변수 or 수식):
   if의 조건이 True 인 경우 실행되는 code - 조건1
   실행문
   실행문
   실행문
 elif: - 조건2
   if의 조건2이 True 인 경우 실행되는 code - 조건2
 elif: - 조건3
   if의 조건3이 True 인 경우 실행되는 code - 조건3
 elif: - 조건4
   if의 조건4이 True 인 경우 실행되는 code - 조건4
 elif: - 조건5
   if의 조건5이 True 인 경우 실행되는 code - 조건5
 else:
   if의 조건이 False 인 경우 실행되는 code - 조건6

'''

money = False
if money:
  print("책을 삽니다")
else:
  print("책을 못 삽니다")

money = 3000
if money >= 5000:
  print("외식을 함")
else:
  print("집에서 먹음")

money = 2000
card = True
if money >= 10000 or card:
  print("여행을 감")
else:
  print("집에 있음")

list_num1 = [1, 2, 3]
print(2 in list_num1)
print(1 not in list_num1)

list_alphabet = ['a','b','c','d','e']
print('c' in list_alphabet)
print('C' in list_alphabet)

list_pocket = ['cash', 'card', 'phone']
if 'cash' in list_pocket:
  print("notebook 구입")
else:
  print("notebook 나중에 구입")

if 'money' in list_pocket:
  pass
else:
  print("card 사용")


if 'money' in list_pocket:
  print("memory 업그레이드");
else:
  if "card" in list_pocket:
    print("memory 업그레이드");
  else:
    print("memory 나중에 업그레이드");

if 'money' in list_pocket:
  print("memory 업그레이드");
elif "card" in list_pocket:
  print("memory 업그레이드");
else:
  print("memory 나중에 업그레이드");

if 'money' in list_pocket: print("memory 업그레이드");
elif "card" in list_pocket: print("memory 업그레이드");
else: print("memory 나중에 업그레이드");

'''
 성적이 60점 이상이면 success를 출력하고
 성적이 60점 미만이면 failure를 출력하세요
 score
'''
score = 73
message = "";
if score >= 60:
  message = "success"
else:
  message = "failure"

print("message")