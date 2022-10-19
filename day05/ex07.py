
# 전역변수 : global variable
num = 1

# 지역변수 : local variable
def test(num):
  print("test(num) 호출됨")
  num = num + 1
  return

test(num)
print('num :',num)