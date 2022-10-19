
# deepcopy - 깊은 복사

import copy

list5 = [[111, 222], [333, 444]]
list6 = copy.deepcopy(list5)

print('list5 :',list5)
print('list6 :',list6)
print("------------------------------------")

list5[1].append(555)
print('list5 :',list5)
print('list6 :',list6)
