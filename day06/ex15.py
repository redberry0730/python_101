num = 10

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
 생성자의 매개변수의 개수에 맞도록
 argument 를 넣어 주어야 함
 클래스이름()  <-- 해당 클래스의 생성자를 호출하는  code
'''
class Book:
  def __init__(self, bookname):
    self.name = bookname
    print(f"책 이름이 {self.name}인 객체가 생성됨0")

book1 = Book("파이썬 프로그래밍")

class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def introduce_myself(self):
    print(f"저의 이름은 {self.name}이고\n나이는 {self.age} 살입니다")

std1 = Student("유관순", 19)
std1.introduce_myself()
print("-----------------------------")

'''
 __del__(self) : destroy 소멸자
                 객체를 메모리 상에서 삭제함 
  
'''
class Developer:
  def __init__(self, name, job):
    self.name = name
    self.job = job
  def self_info(self, name, job):
    self.name = name
    self.job = job
  def display_info(self):
    print(f"저는 {self.name}이고, \n직업은 {self.job} 입니다")
  def __del__(self):
    print("객체가 소멸되었습니다")

dev1 = Developer("윤봉길","독립운동가")
dev1.display_info()

del Developer









