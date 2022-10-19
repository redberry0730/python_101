
# 동시에 두 변수에 같은 값 할당하기
num1 = num2 = 10
print(num1 + num2)
print(num1, num2)

'''
num3 의 값을 1 증가시켜서
num3 에 할당하기
변수 : 한 번에 값 하나만 저장하는 공간 
       값을 바꿔가면서 몇 번이고
       계속 할당할 수 있음
         ㄴ 맨 마지막에 할당 값이 남음
'''
num3 = 10
print('num3 :',num3)
num3 = 20
print('num3 :',num3)
num3 = 30
print('num3 :',num3)
num3 = 40
print('num3 :',num3)
num3 = 50
print('num3 :',num3)


'''
num3 의 값을 1 증가시켜서
num3 에 할당하기
'''
num3 = num3 + 1
print('num3 :',num3)
# num3 : 51

num3 += 1
print('num3 :',num3)
# num3 : 52

num3 = num3 - 1
print('num3 :',num3)
# num3 : 51

num3 -= 1
print('num3 :',num3)
# num3 : 50

