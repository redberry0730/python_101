num=10

'''
Lambda 함수
 ㄴ lambda 키워드를 사용함
    함수를 간결하게 표기함
'''

def add(n1, n2):
  return n1 + n2

result = add(11, 22)
print('result :',result)

sum = lambda n1, n2 : n1 + n2
'''
def sum(n1, n2):
  return n1 + n2
'''
print('sum(33, 55) :',sum(33, 55))
print((lambda n1, n2 : n1 + n2)(33, 55))
print((lambda n1, n2 : 7777)(33, 55))
print((lambda n1, n2=11 : n1 + n2)(33, 55))
print((lambda n1, n2=11 : n1 + n2)(33))

number = 22
print((lambda n1 : n1 + number)(33))

def add_ten(num1):
  return num1 + 10
print(add_ten(56))

print((lambda num1 : num1 + 10)(56))

'''
map(함수, 리스트)

'''
list_numbers = [1, 2, 3, 4, 5]

list_result \
  = list(map(lambda n1 : n1 + 1, list_numbers))

print('list_result :',list_result)

list_result2 \
  = list(filter(lambda n1 : n1 % 2 == 0, list_numbers))

print('list_result2 :',list_result2)
















