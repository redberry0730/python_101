number = 10

'''
Car class 작성하기 (Parent)
attribute(멤버변수) :  생성자에 self.name 선언
method              :  def info(self)

(Child1)
ElectronicCar class
attribute(멤버변수) :  생성자에 self.name 선언
method              :  def info(self) Override
                       이름, 사용연료(electronic) 출력
(Child2)
GasolineCar class
attribute(멤버변수) :  생성자에 self.name 선언
method              :  def info(self) Override
                       이름, 사용연료(gasoline) 출력
'''
class Car:
  def __init__(self, name):
    self.name = name
  def get_info(self):
    print(self.name)

class ElectronicCar(Car):
  '''
  def __init__(self, name):
    self.name = name
    super().__init__(name)
  '''
  def get_info(self):
    print(self.name,'사용연료 : electronic')

class GasolineCar(Car):
  '''
  def __init__(self, name):
    self.name = name
    super().__init__(name)
  '''
  def get_info(self):
    print(self.name, '사용연료 : gasoline')

elec = ElectronicCar("전기차")
gasol = GasolineCar("가솔린차")
elec.get_info()
gasol.get_info()