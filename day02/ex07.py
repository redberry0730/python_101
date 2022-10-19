
# list 의 item(요소) 삭제하기
# del (함수) 사용

list1 = [1, 2, 3, 4, 5]
print(list1)
# del list1[5]
# IndexError: list assignment index out of range
del list1[4]
print(list1)
print("------list1[1:4]----------------------------")

list1 = [1, 2, 3, 4, 5]
print(list1)
# del list1[5]
# IndexError: list assignment index out of range
del list1[1:4]
print(list1)
print("----------------------------------")


number = 100
print(number)
print(id(number))
del number
'''
print(number)
print(id(number))
NameError: name 'number' is not defined
'''
print("---------pop()-------------------------")

list1 = [1, 2, 3, 4, 5]
print(list1)
print(list1.pop())
print(list1)
print("--------pop(3)-------------------------")

list1 = [1, 2, 3, 4, 5]
print(list1)
print(list1.pop(3))
print(list1)
print("----------------------------------")

list1 = [1, 2, 3, 4, 5]
print(list1)
print(list1[-1])
print(list1)
print("----------------------------------")

list1 = [1, 2, 3, 4, 5]
print(list1)
print(list1[-1:len(list1)])
print(list1)
print("----------------------------------")

list1 = [1, 2, 3, 4, 5]
print(list1)
print(list1.remove(3)) # None
print(list1)
print("----------------------------------")