
# 전역변수 : global variable
num = 1

def test():
  print("test() 호출됨")
  global num
  num = num + 1
  return

test()
print('num :',num)