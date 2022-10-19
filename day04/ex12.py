num=0
'''
 반복문 : for, while
 
 형식
          iterate (순회)  iterable type
               sequential type (index) 
 for 변수 in (list, tuple, str, range()):
   statement 1 .....
   statement 2 .....
   statement 3 .....
'''

list_numbers = [1, 2, 3, 4, 5, 6, 7]

for number in list_numbers:
  print(number, end=" ")
print()

n1, n2 = 1, 2
print(n1, n2)

list_nums = [(1, 2), (3, 4), (5, 6)]
for (a, b) in list_nums:
  print(a + b)
print("--------------------------------------")

for (a, b) in list_nums:
  print(a * b)
print("--------------------------------------")







