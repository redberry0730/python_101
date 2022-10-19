class Person:
  def work(self):
    print("열심히 일합니다")

class Student1(Person):
  def work(self): #Overriding
    super().work()
    print("열심히 공부합니다")
  def part_time_work(self):
    print("아르바이트도 합니다")
  def doit(self):
    self.work()

class Student2(Person):
  def work(self): #Overriding
    # super().work()
    Person.work(self)
    print("열심히 공부합니다-2")
  def part_time_work(self):
    print("아르바이트도 합니다-2")
  def doit(self):
    self.work()

person = Person()

std1 = Student1()
std1.work()
std1.part_time_work()
std1.doit()
print("----------------------------")
std2 = Student2()
std2.work()
std2.part_time_work()
std2.doit()
print("----------------------------")

print(issubclass(Student1, Person))
print(issubclass(Student2, Person))
print(issubclass(Person, Student2))
print("----------------------------")

print(isinstance(std1, Student1))
print(isinstance(std1, Student2))
print(isinstance(std2, Student2))
print(isinstance(std2, Student1))
print(isinstance(std2, Student1))
print("----------------------------")
print(isinstance(person, Student1))
print(isinstance(person, Student2))
print("----------------------------")

print(isinstance(std1, Person))
print(isinstance(std2, Person))
