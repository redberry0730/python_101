class CalcParent:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
  def add(self):
    print(self.num1 + self.num2)

class CalcChild(CalcParent):
  def subtract(self):
    print(self.num1 - self.num2)
  def mulitply(self):
    print(self.num1 * self.num2)

chd1 = CalcChild(10, 8)
chd1.add()
chd1.subtract()
chd1.mulitply()
print("------------------------------")

class CalcGrandChild(CalcChild):
  def divide(self):
    print(self.num1 / self.num2)
  def mulitply(self):
    self.result = self.num1 * self.num2
    print(f"계산결과는  {self.result } 입니다")
  def add(self):
    self.result = self.num1 + self.num2
    print(f"계산결과는  {self.result} 입니다")

gchd1 = CalcGrandChild(8, 5)
gchd1.add()
gchd1.subtract()
gchd1.mulitply()
gchd1.divide()