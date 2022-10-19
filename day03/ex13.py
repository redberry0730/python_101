
success = 80
score = int(input('성적을 입력하세요 : '))
# score = int(score)
print(f"당신의 성적은 {score}입니다")

'''
success 이상일 때 '합격'을 출력하세요
미만일 때는 '불합격'을 출력하세요
TypeError: 
  '>=' not supported 
       between instances of 'str' and 'int'
'''
if score >= success:
  print('합격')
else:
  print('불합격')
