
result1 = 0
result2 = 0

def add1(num):
  global result1
  result1 += num
  return result1

def add2(num):
  global result2
  result2 += num
  return result2

print(add1(3))
print(add2(5))
print(add1(6))
print(add2(2))
print("-------------------------")

print(result1)
print(result2)


