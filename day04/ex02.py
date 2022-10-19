num=10
'''
성적을 입력받아서 (정수 or 실수)
학점을 출력하세요

A : 90 - 100
B : 80 - 99 
C : 70 - 89
D : 60 - 69
F : 59 이하
'''
score = float(input("성적을 입력하세요 : "))
grade = ''

if 90 <= score <= 100:
  grade = 'A'
elif 80 <= score < 90:
  grade = 'B'
elif 70 <= score < 80:
  grade = 'C'
elif 60 <= score < 70:
  grade = 'D'
else:
  grade = 'F'

print(f"당신의 학점은 {grade} 학점입니다")
