class Person:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
  def introduce_myself(self):
    print(f"이름 : {self.name}\n"
          f"나이 : {self.age}\n"
          f"성별 : {self.gender}")

class Employee(Person):
  def __init__(self, name, age, gender, salary, hiredate):
    Person.__init__(self, name, age, gender)
    self.salary = salary
    self.hiredate = hiredate
  #Overriding
  def introduce_myself(self):
    Person.introduce_myself(self)
    print(f"급여   : {self.salary}\n"
          f"입사일 : {self.hiredate}")
  def work_hard(self):
    print(f"{self.name} 님은 열심히 일하십니다")

emp = Employee("이순신", 48, "남자", "70000000", "2021년 5월 15일")
emp.work_hard()
emp.introduce_myself()


class Student(Person):
  def __init__(self, name, age, gender, stdno, grade):
    Person.__init__(self, name, age, gender)
    self.stdno = stdno
    self.grade = grade
  #Override
  def introduce_myself(self):
    Person.introduce_myself(self)
    print(f"학번 : {self.name}\n"
          f"학년 : {self.grade}")

  def study_hard(self):
    print(f"{self.name}님은 공부를 열심히 합니다")

std = Student('더조은', 21, '여자', '19981015', '2')
std.study_hard()
std.introduce_myself()

std2 = Student('유관순', 19, '여자', '19000301', '4')
std2.study_hard()
std2.introduce_myself()
