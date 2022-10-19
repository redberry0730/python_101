num=0
'''
학생 성적이 저장된 list_scores 에서
60점 이상을 합격이라 할 때, (score >= 60)
합격생이 몇 명인지 출력하세요
'''
list_scores = [92,82,62,51,42,84,21]
result = ""
count = 0

#  (score >= 60) 참인 경우에만 count 를 1 증가시킴
for score in list_scores:
  if score >= 60:
    count += 1
print(f"{count} 명이 합격했습니다")

print("-------------------------------------")

'''
1 번째 학생 : 합격
....
4 번째 학생 : 불합격
'''
count = 0
for score in list_scores:
  if score >= 60:
    result = "합격"
  else:
    result = "불합격"
  count += 1
  print(f"{count} 번 학생 : {result}")




