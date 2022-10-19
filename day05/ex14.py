
from functools import reduce

students = \
[
  {'mail':'1@naver.com', 'name':'이순신', 'gender':'M', 'age':48},
  {'mail':'2@naver.com', 'name':'안중근', 'gender':'M', 'age':30},
  {'mail':'3@naver.com', 'name':'윤봉길', 'gender':'M', 'age':25},
  {'mail':'4@naver.com', 'name':'유관순', 'gender':'F', 'age':19},
  {'mail':'5@naver.com', 'name':'김유신', 'gender':'M', 'age':62},
]

result = reduce(lambda n1, n2 : n1 + n2['age'], students, 0)
print('나이의 합 :',result) # 184

result = reduce(lambda n1, n2 : n1 + [n2['mail']], students, [])
print('이메일 :',result)
# 이메일 : ['1@naver.com', '2@naver.com', '3@naver.com', '4@naver.com', '5@naver.com']

result = reduce(lambda n1, n2 : n1 + n2['mail'], students, "")
print('이메일 :',result)
# 이메일 : 1@naver.com2@naver.com3@naver.com4@naver.com5@naver.com

def group_gender(genders, students):
  gender = students['gender']
  if gender not in genders:
    genders[gender] = []
  genders[gender].append(students['name'])
  return genders

print(reduce(group_gender, students, {}))
# {'M': ['이순신', '안중근', '윤봉길', '김유신'], 'F': ['유관순']}