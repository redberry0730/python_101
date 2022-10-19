import random

'''
  random.random()
    0 부터 1 미만의 실수를 발생시킴
    0.0 ~ 0.9999999999999999.........
'''
print('random.random() :',random.random())

'''
 1부터 10까지의 임의의 정수 발생시키기
'''
print('random.randint(1, 10) :',random.randint(1, 10))
print("----------------------------------------")

list_numbers = []
for i in range(10):
  list_numbers.append(random.randint(1, 10))
  print(list_numbers)
print("----------------------------------------")
print('list_numbers :',list_numbers)

print("----------------------------------------")
for i in range(10):
  print(list_numbers[i] * 3.14 * 2)
print("----------------------------------------")





