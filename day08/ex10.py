from abc import *

class Vehicle(metaclass=ABCMeta):
  @abstractmethod
  def move(self):
    pass
  @abstractmethod
  def stop(self):
    pass

class FireFighter(Vehicle):
  def move(self): #Overriding
    print('불을 끄러 출동합니다')
  def stop(self): #Overriding
    print('화재 현장에 도착했습니다')

class Ambulance(Vehicle):
  def move(self):  # Overriding
    print('환자를 이송하러 출동합니다')
  def stop(self):  # Overriding
    print('병원에 도착했습니다')

class PatrolCar(Vehicle):
  def move(self):  # Overriding
    print('순찰하러 출동합니다')
  def stop(self):  # Overriding
    print('본부에 도착했습니다')

list_vehicles = list()
list_vehicles.append(FireFighter())
list_vehicles.append(Ambulance())
list_vehicles.append(PatrolCar())

for car in list_vehicles:
  car.move()
print('--------------------------------')
for car in list_vehicles:
  car.stop()


