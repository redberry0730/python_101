class Child:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
  def get_name(self):
    return self.__name
  def get_age(self):
    return self.__age
  def set_name(self, name):
    self.__name = name
  def set_age(self, age):
    self.__age = age

ch1 = Child("이순신", 48)
ch2 = Child("강감찬", 72)

# print(ch1.name,"--",ch1.age)
print(ch1.get_name())
print(ch1.get_age())

ch1.name = "안중근" # 재할당 안 된
print(ch1.get_name())

ch1.set_name("안중근") # 재할당 됨
print(ch1.get_name())

