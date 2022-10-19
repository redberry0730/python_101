class Employee1:
  def __init__(self):
    self.__age = 18
  @property  # getter
  def age(self):
    return self.__age
  @age.setter  # setter
  def age(self, age):
    if age >= 18:
      self.__age = age
      print("회원가입을 축하합니다")
    else:
      print(f"{self.__age}세 이상만 가입 가능합니다")

emp1 = Employee1()
emp1.age = 31
print(emp1.age)