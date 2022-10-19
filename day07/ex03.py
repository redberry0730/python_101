class Employee1:
  def __init__(self):
    self.__age = 28
  def set_age(self, age):
    self.__age = age
  def get_age(self):
    return self.__age

emp1 = Employee1()
print(emp1.get_age())
emp1.set_age(32)
print(emp1.get_age())
print("------------------")
emp1.__age = 12
print(emp1.__age)