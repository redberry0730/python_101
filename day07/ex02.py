class Employee1:
  def __init__(self):
    self.age = 28
  def set_age(self, age):
    self.age = age
  def get_age(self):
    return self.age

emp1 = Employee1()
print(emp1.get_age())
emp1.set_age(32)
print(emp1.get_age())
print("------------------")
emp1.age = 12
print(emp1.age)

'''
class Employee2:
  def __init__(self, age):
    self.age = age
  def set_age(self, age):
    self.age = age
  def get_age(self):
    return self.age
'''