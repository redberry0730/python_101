num=0

'''
  구구단 : 이중(중첩) for 문 구조
  
   단수 X 곱하는수
    2     (1 ~ 9)
    3     (1 ~ 9)
    4     (1 ~ 9)
    5     (1 ~ 9)
    6     (1 ~ 9)
    7     (1 ~ 9)
    8     (1 ~ 9)
    9     (1 ~ 9)

'''

for i in range(2, 10):
  print(f"-- {i} 단 --")
  for j in range(1, 10):
    print(f"{i} X {j} = {i * j}")
  print()
print("-----------------------------------")

for i in range(2, 10):
  for j in range(1, 10):
    print(f"{i} X {j} = {i * j}")
  print()
print("-----------------------------------")

'''
각단에 홀수만 곱해서 출력하세요
각단에 짝수만 곱해서 출력하세요

홀수단만 출력하세요
짝수단만 출력하세요
'''

for i in range(2, 10):
  for j in range(1, 10, 2):
    print(f"{i} X {j} = {i * j}")
  print()
print("-----------------------------------")

for i in range(2, 10):
  for j in range(2, 10, 2):
    print(f"{i} X {j} = {i * j}")
  print()
print("-----------------------------------")

for i in range(2, 10):
  for j in range(1, 10):
    if j % 2 == 1:
      print(f"{i} X {j} = {i * j}")
  print()
print("-----------------------------------")

for i in range(2, 10):
  for j in range(1, 10):
    if j % 2 == 0:
      print(f"{i} X {j} = {i * j}")
  print()
print("-----------------------------------")

for i in range(2, 10, 2):
  for j in range(1, 10):
    print(f"{i} X {j} = {i * j}")
  print()
print("-----------------------------------")

for i in range(3, 10, 2):
  for j in range(1, 10):
    print(f"{i} X {j} = {i * j}")
  print()
print("-----------------------------------")

for i in range(2, 10):
  for j in range(1, 10):
    if i % 2 == 1:
      print(f"{i} X {j} = {i * j}")
  print()
print("-----------------------------------")

for i in range(2, 10):
  for j in range(1, 10):
    if i % 2 == 0:
      print(f"{i} X {j} = {i * j}")
  print()
print("-----------------------------------")

'''
짝수단에서는 짝수만 곱하고
홀수단에서는 홀수만 곱하는 
구구단을 출력하세요
'''

for i in range(2, 10, 2):
  for j in range(2, 10, 2):
    print(f"{i} X {j} = {i * j}")
  print()
print("-----------------------------------")

for i in range(3, 10, 2):
  for j in range(1, 10, 2):
    print(f"{i} X {j} = {i * j}")
  print()
print("-----------------------------------")


for i in range(2, 10):
  for j in range(1, 10):
    if i % 2 == 0 and j % 2 == 0:
      print(f"{i} X {j} = {i * j}")
    if i % 2 == 1 and j % 2 == 1:
      print(f"{i} X {j} = {i * j}")
  print()
print("-----------------------------------")

for i in range(2, 10):
  for j in range(1, 10):
    if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1) :
      print(f"{i} X {j} = {i * j}")
  print()
print("-----------------------------------")

for i in range(2, 10):
  for j in range(1, 10):
    if i % 2 == j % 2:
      print(f"{i} X {j} = {i * j}")
  print()
print("-----------------------------------")

