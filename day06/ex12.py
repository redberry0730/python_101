
class Child:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def set_name(self, name):
    self.name = name
  def set_age(self, age):
    self.age = age

ch1 = Child("더조은", 19)
print(ch1.name,'--',ch1.age)

ch1.name ="이순신"
ch1.age = 48
print(ch1.name,'--',ch1.age)