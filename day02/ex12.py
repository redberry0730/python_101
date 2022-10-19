'''
list3 = [[11, 22], [33, 44]]
list4 = list3[:]

'''
# shallow copy - 얕은 복사

import copy
list3 = [[11, 22], [33, 44]]
list4 = copy.copy(list3)

'''
.  : access operator - 접근연산자
     dot operator    - 점연산자
'''
print('list3 :',list3)
print('list4 :',list4)

list3[0] = [55, 77]
print('list3 :',list3)
print('list4 :',list4)

list3[1].append(55)
print('list3 :',list3)
print('list4 :',list4)

