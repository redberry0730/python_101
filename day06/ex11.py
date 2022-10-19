class Calculator:
  def __init__(self, num1, num2):
    self.number1 = num1
    self.number2 = num2
    self.result = 0
  def setdata(self, num1, num2):
    self.number1 = num1
    self.number2 = num2
  def add(self):
    self.result = self.number1 + self.number2
    return self.result
  def sub(self):
    self.result = self.number1 - self.number2
    return self.result
  def multi(self):
    self.result = self.number1 * self.number2
    return self.result
  def divide(self):
    self.result = self.number1 // self.number2
    return self.result

c1 = Calculator(10, 8)
print(c1.number1)
print(c1.number2)
print(c1.add())
print(c1.sub())
print(c1.multi())
print(c1.divide())

'''
Child 클래스를 작성하고
'더조은' 과 '김철수' 의
이름과 나이를 출력하세요
'''
# 생성자 : 객체가 생성될 때
#          멤버변수를 초기화하는 메소드
class Child:
  def __init__(self):
    self.name = ""
    self.age = 0
  def set_name(self, name):
    self.name = name
  def set_age(self, age):
    self.age = age

child1 = Child()
child2 = Child()

child1.set_name("더조은")
child2.set_name("김철수")

child1.set_age(19)
child2.set_age(23)

print("child1의 이름 :",child1.name)
print("child1의 나이 :",child1.age)
print("child2의 이름 :",child2.name)
print("child2의 나이 :",child2.age)
