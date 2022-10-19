class Book:
  def __init__(self, bookname):
    self.name = bookname
    print(f"책 이름이 {self.name}인 Book 객체가 생성됨")

book1 = Book("파이썬 입문")

'''
  생성자 :  메소드의 일종
            클래스를 생성할 때
            멤버변수를 초기화함  

 class 클래스이름:
   def __init__(self):
     statement....
     statement....

 생성자의 매개변수 : 필요한 만큼 지정할 수 있음
 객체를 생성할 때, 클래스이름 뒤의 소괄호 안에
 생성자(__init__)의 매개변수의 개수에 맞도록
 argument 를 넣어 주어야 함
 
 클래스이름()  <-- 해당 클래스의 생성자를 호출하는  code
               <-- 해당 클래스의 객체를 생성하는  code

'''
class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def introduce_myself(self):
    print(f"저의 이름은 {self.name}이고\n나이는 {self.age}입니다")

student1 = Student("유관순", 19)
student1.introduce_myself()

class Developer:
  def __init__(self, name, job):
    self.name = name
    self.job  = job
  def set_info(self, name, job):
    self.name = name
    self.job = job
  def get_info(self):
    return f"{self.name} -- {self.job}"
  def get_name(self):
    return self.name
  def get_job(self):
    return self.job
  def display_info(self):
    print(f"저는 {self.name}이고\n직업은 {self.job}입니다")

dev1 = Developer("더조은", "개발자")
dev1.display_info()
dev1.set_info("이순신", "장군")
dev1.display_info()
print(dev1.get_info())

print(dev1.get_name())
print(dev1.get_job())

dev2 = Developer("강감찬", "대장군")
print(dev2.get_name())
print(dev2.get_job())

print("----------------------------")

'''
생성자를 하나도 작성하지 않으면
해당 클래스의 객체를 생성할 때
자동으로 기본생성자가 호출됨
(기본생성자가 생략되어있음)
기본생성자 - 매개변수 없는 생성자
기본생성자를 [먼저] 작성하고
매개변수 있는 생성자를 [나중에] 작성하면
기본생성자를 사용해서 객체를 생성할 수 없고
매개변수 있는 생성자만 사용해서 객체를 생성할 수 있음
------------------------------------------
매개변수 있는 생성자를 [먼저] 작성하고
기본생성자를 [나중에] 작성하면
매개변수 있는 생성자를 사용해서 객체를 생성할 수 없고
기본생성자를 사용해서 객체만 생성할 수 있음
------------------------------------------
매개변수 있는 생성자만 작성하고
기본생성자는 작성하지 않은 경우에는
매개변수 있는 생성자만 사용해서 객체를 생성할 수 있음
'''
class Car:

  def __init__(self, color, door):
    self.color = color
    self.door = door

  def set_info(self, color, door):
    self.color = color
    self.door  = door
  def display_info(self):
    print(f"{self.color} -- {self.door}")

car1 = Car("white", 4)
# AttributeError: 'Car' object has no attribute 'color'
car1.set_info("blue", 6)
car1.display_info()




