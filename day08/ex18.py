
# 외부 함수 (outer function)
def say_hello():
  hello1 = 'Hello, Python !!'
  hello2 = 'Hello, Programming !!'
  # 내부 함수 (inner function)
  def say_greeting1():
    print(hello1)
  def say_greeting2():
    print(hello2)
  say_greeting1()
  say_greeting2()

say_hello()
print('-------------------------')

def outerfunc():
  num = 11
  def innerfunc():
    num = 22
  innerfunc()
  print(num)

outerfunc()
print('-------------------------')


def outerfunc2():
  num2 = 11
  def innerfunc2():
    nonlocal num2
    num2 = 22
  innerfunc2()
  print(num2)

outerfunc2()