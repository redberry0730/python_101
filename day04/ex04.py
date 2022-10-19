a, b = 10, 5

print(a < 0 and (b / 1) == 0)
print(a & b and (b / 1) == 0)

'''

1 byte = 1 bit * 8

비트연산

    1   &  1    :   1
    1   &  0    :   0
    0   &  1    :   0
    0   &  0    :   0
    
    1   |  1    :   1
    1   |  0    :   1
    0   |  1    :   1
    0   |  0    :   0

10 : 1 0 1 0
 &
 5 : 0 1 0 1
---------------
     0 0 0 0 
     
     
10 : 1 0 1 0
 |
 5 : 0 1 0 1
---------------     
     1 1 1 1
'''
a, b = 10, 5

print(a & b) # 0
print(a | b) # 15

a, b = 10, 5

print(a < 0 and (b / 1) == 0)
print(a & b and (b / 1) == 0)

num1 = 1
num2 = 0

if num2 and 10 / num2:
  print(True)
else:
  print(False)

if num1 and 10 / num1:
  print(True)
else:
  print(False)

'''
비트 연산에서 0과 다른 수를 |(비트 or연산)연산을 하면
결과는 다른 수가 그대로 나오고
비트 연산에서 15와 다른 수를 &(비트 and연산)연산을 하면
결과는 다른 수가 그대로 나옴
'''
c, d = 15, 5

print(c & d)
print(c | d)

