
# 짝수인지 홀수인지 판별하기
def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False
print(is_even(15))  # False

print((lambda num : num % 2 == 0)(14)) # True

def is_even2(num):
  return True if num % 2 == 0 else False
print(is_even2(15))  # False

list_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_result = []

for number in list_nums:
  if is_even2(number):
    list_result.append(number)
print('list_result :',list_result)
# list_result : [2, 4, 6, 8, 10]

list_result = list(filter(is_even2, list_nums))
print('list_result :',list_result)
# list_result : [2, 4, 6, 8, 10]

print(list(filter(lambda num : num % 2 == 0,list_nums)))
# [2, 4, 6, 8, 10]

list_result = \
   list(filter(lambda num : num % 2 == 0,list_nums))
print('list_result :',list_result)
# list_result : [2, 4, 6, 8, 10]



