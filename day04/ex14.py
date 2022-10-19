num = 0
'''

1번 이순신 학생 : 합격
2번 안중근 학생 : 합격
3번 이재명 학생 : 합격
4번 김유신 학생 : 불합격
5번 이율곡 학생 : 불합격

'''
dict_scores \
  = {"이순신":91,"안중근":76,"이재명":88,"김유신":69,"이율곡":52}

result = ''
count = 0

for score in dict_scores.values():
  if score >= 60:
    result = '합격'
  else:
    result = '불합격'
  print(f"{count+1} 번 {list(dict_scores.keys())[count]} 학생 : {result}")
  count += 1





 