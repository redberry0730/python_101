num = 10

'''
클래스 상속 (inheritance)
  ㄴ 확장( extension ) __ extends 키워드 사용 (in java)
'''
class Calc4:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
  def set_data(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
  def add(self):
    self.result = self.num1 + self.num2
    return self.result
  def subtract(self):
    self.result = self.num1 - self.num2
    return self.result
  def multiply(self):
    self.result = self.num1 * self.num2
    return self.result
  def divide(self):
    self.result = self.num1 / self.num2
    return self.result

class Calc_further(Calc4):
  def pow(self):
    self.result = self.num1 ** self.num2
    return self.result

cf1 = Calc_further(10, 8)
print(cf1.add())
print(cf1.subtract())
print(cf1.multiply())
print(cf1.divide())
print(cf1.pow())