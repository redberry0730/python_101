
def add_many(*params):  # *args
  result = 0
  for i in params:
    result = result + i
  return result

result = add_many(1)
print('result :',result)
result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('result :',result)


def add_multi(operator, *numbers):
  result = 1
  if operator == "add":
    for i in numbers:
      result += i
  if operator == "subtract":
    for i in numbers:
      result -= i
  if operator == "multiply":
    print(numbers)
    for i in numbers:
      result *= i
  if operator == "divide":
    for i in numbers:
      result /= i
  return result

return_value = add_multi("add", 1, 2, 3, 4, 5)
print('return_value :',return_value)
return_value = add_multi("subtract", 1, 2, 3, 4, 5)
print('return_value :',return_value)
return_value = add_multi("multiply", 1, 2, 3, 4, 5)
print('return_value :',return_value)
return_value = add_multi("divide", 1, 2, 3, 4, 5)
print('return_value :',return_value)

print("-------------------------------")

def children(*kids):
  print("우리집 아이들은",kids,"입니다")
children("더조은","파이썬","자바")

def children(*kids):
  child = ""
  for kid in kids:
    if kid == kids[len(kids)-1]:
      child += kid
    else:
      child += kid + ", "
  print("우리집 아이들은",child,"입니다")
children("더조은","파이썬","자바")