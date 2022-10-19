class Employee1:
  def __init__(self, age):
    self.__age = age
  def get_age(self):
    return self.__age
  def set_age(self, age):
    self.__age = age

'''
맴버변수(self.~~~) 이름 앞에 
__(double underscore : dunder) 를 붙이면
해당 클래스 외부에서는 접근할 수 없는 
private 멤버변수가 됨
해당 클래스 내부에서는 접근이 가능함
 ㄴ 같은 클래스의 메소드에서는 접근(사용)이 가능함
'''

emp1 = Employee1(32)
# AttributeError: 'Employee1' object has no attribute '__age'
# print(emp1.__age)
print(emp1.get_age())
emp1.set_age(10)
print(emp1.get_age())
