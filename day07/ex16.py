num=10
'''
다중상속
  ㄴ 하나의 자식 클래스가
     두 개 이상의 부모 클래스를 상속하는 것
'''
class Parent1:
  def display_myself(self):
    print("Parent1 입니다")

class Parent2:
  def display_myself(self):
    print("Parent2 입니다")

class Child(Parent1, Parent2):
  def display_child(self):
    print("Child 입니다")
    Parent1.display_myself(self)
    Parent2.display_myself(self)

chd = Child()
chd.display_child()
print("-------------------------------")
chd.display_myself()

