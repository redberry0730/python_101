
# list 복사 - mutable

list1 = [1, 2, 3, 4, 5]
list2 = list1[:]
'''
print(list1)
print(list1[:])
print(id(list1))     # 1679390823744
print(id(list1[:]))  # 1679391129152
'''
# 내용만 비교 : True
print('list1 == list2 :',list1 == list2)
# 주소를 비교 : False
print('list1 is list2 :',list1 is list2)

print('list1 :',list1)
print('list2 :',list2)

list1[2] = 11  # list2[2] = 11
print('list1 :',list1)
print('list2 :',list2)

print("---------------------------------------")

list3 = [[11, 22], [33, 44]]
list4 = list3[:]

print('list3 :',list3)
print('list4 :',list4)

print('list3 주소 :',id(list3))
print('list4 주소 :',id(list4))

print('list3[0] 주소 :',id(list3[0]))
print('list4[0] 주소 :',id(list4[0]))
print('list3[1] 주소 :',id(list3[1]))
print('list4[1] 주소 :',id(list4[1]))

print("---------------------------------------")

list3[0] = [55, 77]
print('list3 :',list3)
# list3 : [[55, 77], [33, 44]]
print('list4 :',list4)
# list4 : [[11, 22], [33, 44]]

print("---list3[1].append(55)------------------------------------")
list3[1].append(55)
print('list3 :',list3)
# list4[1].append(55)
print('list4 :',list4)


