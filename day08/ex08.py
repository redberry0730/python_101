from abc import *

class Car(metaclass=ABCMeta):
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return f"자동차 이름 : {self.name}"
  def display_info(self):
    print(f"{self.name}(은)는 새로 나온 자동차입니다")
  @abstractmethod
  def fuel(self):
    pass

class ElectronicCar(Car):
  # Overriding
  def fuel(self):
    return 'Electronic'

elect = ElectronicCar('아이오닉5')
print(elect,', 사용연료 :',elect.fuel())

class HydrogenCar(Car):
  # Overriding
  def fuel(self):
    return 'Hydrogen'

hydrogen = HydrogenCar('넥쏘')
print(hydrogen,', 사용연료 :',hydrogen.fuel())