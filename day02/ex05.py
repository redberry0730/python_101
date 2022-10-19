num = 10

'''
리스트(list) 자료형 : index 가 있음
  data type 이 다른 여러 개의 data 를 저장할 수 있음
    ㄴ list 안에는 어떠한 data type 도 저장할 수 있음 
  비어있는 list 를 만들 수 있음
'''
list1 = []
list1_1 = list()
list2 = [1, 2, 3, 4, 5]
list3 = ['python', 'program', 'best', 'language']
list4 = [1, 2, 3, 'python', 'program', 'best']
list5 = [1, 2, 3, 'python', ['program', 'best']]


list2 = [1, 2, 3, 4, 5]
print(list2[3])

list3 = ['python', 'program', 'best', 'language']
print(list3[2])

list5 = [1, 2, 3, 'python', ['program', 'best']]
print(list5[4][0])
print(list5[4][1])
print(list5[4]) # ['program', 'best']
print(list5[-1]) # ['program', 'best']
print(list5[-1][1]) # best

list2 = [1, 2, 3, 4, 5]
print(list2[2] + list2[3])


list6 = [55, 77, ['python', 'program', ['best', 'language']]]
print(list6[2][2][1])
print(list6[-1][2][1])
print(list6[-1][-1][1])
print(list6[-1][-1][-1])
'''
python, program
'''
print(list6[2][0:2])

list7 = [11, 22, 33, ["python", "best", "language"], "a", "b", "c"]
'''
best, language
'''
print(list7[3][1:3])
print(list7[3][1:2])

