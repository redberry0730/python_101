
# __ : doulbe underline : dunder
# __init__(self) : 생성자 - constructor
# self.result : self. 이 앞에 붙어있는 변수는
#                 ㄴ 멤버변수 (instance variable)
class Calc:
  def __init__(self):
    self.result = 0
  def add(self, number):
    self.result += number
    return self.result

calc1 = Calc()
calc2 = Calc()

print('calc1.add(3) :',calc1.add(3))
print('calc1.add(5) :',calc1.add(5))
print('calc2.add(3) :',calc2.add(5))
print('calc2.add(5) :',calc2.add(7))











