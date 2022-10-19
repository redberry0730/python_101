from abc import *

class Person(metaclass=ABCMeta):
  @abstractmethod
  def eat(self):
    pass
  @abstractmethod
  def sleep(self):
    pass
class Student(Person):
  # Overriding
  def eat(self):
    print('밥먹기')
  # Overriding
  def sleep(self):
    print('잠자기')
  def study(self):
    print('공부하기')
  def go_to_school(self):
    print('학교 가기')
class Worker(Person):
  # Overriding
  def eat(self):
    print('밥먹기')
  # Overriding
  def sleep(self):
    print('잠자기')
  def work(self):
    print('근무하기')
  def go_to_work(self):
    print('출근하기')

std = Student()
std.eat()
std.sleep()
std.study()
std.go_to_school()

worker = Worker()
worker.eat()
worker.sleep()
worker.work()
worker.go_to_work()