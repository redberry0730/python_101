num = 0
'''
세 수를 입력 받아서  <-- input()
가장 큰 수를 출력하세요

if 문

가장 작은 수를 출력하세요

'''

max = 0
min = 0

num1 = int(input('첫 번째 수를 입력하세요 : '))
num2 = int(input('두 번째 수를 입력하세요 : '))
num3 = int(input('세 번째 수를 입력하세요 : '))

if num1 >= num2 and num1 >= num3:
  max = num1
elif num2 >= num1 and num2 >= num3:
  max = num2
else:
  max = num3

print(f"가장 큰 수는 {max} 입니다")

if num1 <= num2 and num1 <= num3:
  min = num1
elif num2 <= num1 and num2 <= num3:
  min = num2
else:
  min = num3

print(f"가장 작은 수는 {min} 입니다")

'''
삼항 연산자 1) if 를 사용한 ...
            2) and, or 를 사용한...  
'''
max2, min2 = 0, 0
max2 = num1 if num1 >= num2 and num1 >= num3 else num2 if num2 >= num3 else num3
min2 = num1 if num1 <= num2 and num1 <= num3 else num2 if num2 <= num3 else num3

print(f"가장 큰 수는 {max2} 입니다")
print(f"가장 작은 수는 {min2} 입니다")

max3 = (num1 >= num2 and num1 >= num3) and num1 or (num2 >= num3) and num2 or num3
min3 = (num1 <= num2 and num1 <= num3) and num1 or (num2 <= num3) and num2 or num3

print(f"가장 큰 수는 {max3} 입니다")
print(f"가장 작은 수는 {min3} 입니다")
