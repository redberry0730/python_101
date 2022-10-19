
list_numbers = [1, 2, 3, 4, 5]
list_result  = []

def add_one(num1):
  return num1 + 1

for number in list_numbers:
  list_result.append(add_one(number))
print('result :',list_result)

list_result  = list(map(add_one, list_numbers))
print('result :',list_result)

list_result  = list(map(lambda num1: num1 + 2, list_numbers))
print('result :',list_result)
print("-----------------------------------")

list_real_numbers = [1.2, 2.5, 3.6, 4.2]
list_integer_numbers = []
print(list_real_numbers)

for idx in range(len(list_real_numbers)):
  list_integer_numbers.append(int(list_real_numbers[idx]))
print(list_integer_numbers)

list_integer_numbers = list(map(int, list_real_numbers))
print(list_integer_numbers)

print(list(range(1, 11)))
print(list(map(str, range(1, 11))))

