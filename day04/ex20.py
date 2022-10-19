num=0
'''
A 학급에 모두 10 명의 학생이 있습니다.
이 학생들의 중간고사 점수는
[70,60,55,75,95,90,80,80,85,100]
입니다
for 문을 사용해서 A 학급의 평균을 출력하세요
'''
list_scores = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in list_scores:
  total += score;
average = total / len(list_scores)
print(f'A 학급의 평균 : {average} 점')

'''
아래에 학생 12 명의 혈액형이 있습니다.
['A','A','A','O','O','O','B','O','AB','B','AB','A']
for 문을 사용해서 각 혈액형 별 학생 수를 출력하세요
1) count 를 이용하는 방법
2) dictionary 를 이용하는 방법
'''

list_bloods = ['A','A','A','O','O','O','B','O','AB','B','AB','A']

student_A = 0
student_B = 0
student_AB = 0
student_O = 0

for blood in list_bloods:
  if blood == 'A':
    student_A += 1
  elif blood == 'B':
    student_B += 1
  elif blood == 'O':
    student_O += 1
  elif blood == 'AB':
    student_AB += 1

print(f"A 형 학생 {student_A} 명")
print(f"B 형 학생 {student_B} 명")
print(f"O 형 학생 {student_O} 명")
print(f"AB 형 학생 {student_AB} 명")
print("---------------------------------------------")

dict_blood = {'A':0, 'B':0, 'O':0, 'AB':0}
list_bloods = ['A','A','A','O','O','O','B','O','AB','B','AB','A']

for blood in list_bloods:
  dict_blood[blood] += 1

print(f"A 형 학생 {dict_blood['A']} 명")
print(f"B 형 학생 {dict_blood['B']} 명")
print(f"O 형 학생 {dict_blood['O']} 명")
print(f"AB 형 학생 {dict_blood['AB']} 명")
print("---------------------------------------------")

dict_blood['A'] = 0
dict_blood['B'] = 0
dict_blood['O'] = 0
dict_blood['AB'] = 0

for blood in list_bloods:
  if blood == 'A':
    dict_blood['A'] += 1
  elif blood == 'B':
    dict_blood['B'] += 1
  elif blood == 'O':
    dict_blood['O'] += 1
  elif blood == 'AB':
    dict_blood['AB'] += 1

print(f"A 형 학생 {dict_blood['A']} 명")
print(f"B 형 학생 {dict_blood['B']} 명")
print(f"O 형 학생 {dict_blood['O']} 명")
print(f"AB 형 학생 {dict_blood['AB']} 명")
print("---------------------------------------------")
