num = 10
'''
 매개변수에 dictionary 전달받기
  kwargs (Keyword Arguments)
   | ㄴ arguments
  keyword
  
 def 함수이름(**params):
   statement ...
   statement ...
   
'''
def print_dict(**key_values):
  print(key_values)

print_dict(name="이순신")
print_dict(name="안중근", age=32)

def print_name(**name):
  print("성은,",name['first_name'],"이고, 이름은",name['last_name'],"입니다")
print_name(first_name="이", last_name="순신")


print("---------------------------------")

def operations(n1, n2):
  return n1+n2, n1-n2, n1*n2, n1/n2

result_add, result_subtract, result_multi, result_divide\
  = operations(10, 8)

print('result_add       :',result_add)
print('result_subtract  :',result_subtract)
print('result_multi     :',result_multi)
print('result_divide    :',result_divide)









