
class Calc1:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
  def add(self):
    return self.num1 + self.num2
  def subtract(self):
    return self.num1 - self.num2
class Calc2:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
    # Calc1 클래스 타입의 변수를
    # Calc2 클래스의 멤버변수로 함
    self.calc1 = Calc1(self.num1, self.num2)
  def multiply(self):
    return self.num1 * self.num2
  def add(self):
    return self.calc1.add()
  def subtract(self):
    return self.calc1.subtract()

calc2 = Calc2(10, 8)
print('calc2.add() :',calc2.add())
print('calc2.subtract() :',calc2.subtract())
print('calc2.multiply() :',calc2.multiply())
