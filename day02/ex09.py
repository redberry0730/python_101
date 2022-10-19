
# list 정렬하기
list1 = [7, 3, 5, 1, 0]
print("----list1.sort()--원본이 바뀜--------------------------------")
print("----return 값이 없음 : None--------------------------------")
print("list1 :",list1)
print("list1.sort() :",list1.sort()) # None
print("list1 :",list1)
print("----sorted(list2)--원본이 안 바뀜--------------------------------")
print("----원본(원 data)을 가지고 정렬 후 새로운 list 를 생성함--------------------------------")

list2 = [7, 3, 5, 1, 0]
print("list2 :",list2)
print("sorted(list2) :",sorted(list2))
print("list2 :",list2)
print("--------------------------------------")

'''
 list 뒤집기
 reverse()
 원본을 뒤집기만 하고 return 값이 없음
'''
list3 = [1, 2, 3, 4, 5]
print('list3 :',list3)
print('list3.reverse() :',list3.reverse()) # : None
print('list3 :',list3)

list4 = [9, 3, 8, 5, 6, 1]
print('list4 :',list4)
list4.reverse()
print('list4 :',list4)

list5 = [10, 4, 7, 6, 9, 2]
'''
 list5 를 내림차순으로 정렬한 후 출력하세요
 오름차순으로 정렬한 후 reverse() 함
'''
print("--sorted(list5).reverse()---------------------------------")
print('list5 :',list5)
list5_1 = sorted(list5)
print(list5_1.reverse()) # None
print(list5_1)
print("--list5.sort() & list5.reverse()---------------------------------")
list5.sort()
list5.reverse()
print('list5 :',list5)
print("--sorted(list6, reverse=True)---------------------------------")

list6 = [34, 21, 67, 1, 8, 0]
print('list6 :',list6)
list6_1 = sorted(list6, reverse=True) # 기본값 : reverse=False
print('list6_1 :',list6_1)
print("--list6.sort(reverse=True)---------------------------------")
list6.sort(reverse=True)
print('list6(내림차순) :',list6)

print("--list_str1.sort()---------------------------------")
list_str1 = ["python", "java", "Spring", "c/c++", "javascript"]
print('list_str1 :',list_str1)
list_str1.sort()
print('list_str1 :',list_str1)
print("----str9.split()---------------------------------")

str9 = "더조은 IT 아카데미"
list_str9 = str9.split()
print('list_str9 :',list_str9)
# list_str9 : ['더조은', 'IT', '아카데미']
print("----list_str9.sort(key=len)---------------------------------")

list_str9.sort(key=len)
print('list_str9 :',list_str9)

list_str9.sort(key=len, reverse=True)
print('list_str9 :',list_str9)

print("----reversed(list10)---------------------------------")
'''
list.reverse()
reversed(list)
'''
list10 = [5, 3, 8, 1, 11]
print('list10 :',list10)
print(reversed(list10))
print('list10 :',list10)
print('list(reversed(list10)) :',list(reversed(list10)))
print('list10 :',list10)




print("----index---------------------------------------")
list7 = [11, 22, 33, 44, 55]
print('list7.index(22) :',list7.index(22))

list8 = ["python", "programming", "language"]
print('list8.index("language") :',list8.index("language"))

