
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

'''
list 합치기
'''
list_result = list1 + list2
print(list_result)

'''
list 반복하기
'''
print(list1 * 5)

'''
list 길이 구하기
'''
print(len(list1))
print(len(list2))
print(len(list_result))

print(list2)
'''
hello 8
'''
# print("hello" + list2[2])
# TypeError: can only concatenate str (not "int") to str

print("hello " + str(list2[2]))

print(list1)
print(id(list1))

'''
 [1, 2, 3, 4, 5]
 4 -> 7
 [1, 2, 3, 7, 5]
 
 list : 원본이 바뀜(변형됨) <-- mutable
'''
list1[3] = 7
print(list1)
print(id(list1))
print("-------------------------")

str1 = "python"
print(str1)
'''
python -> pyshon
'''
'''
 str1[2] = "s"
TypeError: 'str' object does not support item assignment
  <-- immutable    ㄴ (class : type)
'''
str_result = str1[:2] + "s" + str1[3:]
print(str1[:2] + "s" + str1[3:]) # pyshon
print(str_result)

