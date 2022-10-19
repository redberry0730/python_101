
class Calculator:
  def __init__(self):
    self.number1 = 0
    self.number2 = 0
    self.result = 0
  def setdata(self, num1, num2):
    self.number1 = num1
    self.number2 = num2
  def add(self):
    self.result += self.number1 + self.number2;
    return self.result

calc1 = Calculator()
calc2 = Calculator()

calc1.setdata(11, 22)
calc1.add()
print('calc1.result :',calc1.result)

calc2.setdata(33, 55)
calc2.add()
print('calc2.result :',calc2.result)
print("------------------------------------------")

calc1.setdata(10, 20)
calc1.add()
print('calc1.result :',calc1.result)
print("------------------------------------------")

calc2.setdata(10, 20)
calc2.add()
print('calc2.result :',calc2.result)
print("------------------------------------------")

print('calc1.result :',calc1.result)
print("------------------------------------------")

