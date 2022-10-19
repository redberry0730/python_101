class Java:
  version = "1.8"
  def __init__(self):
    self.version = "version : " + self.version
  @staticmethod
  def static_version():
    return Java()
  @classmethod
  def class_version(cls):
    return cls()
  # instance 메소드
  def display_version(self):
    print(self.version)

class Csharp1(Java):
  version = "7.1"
class Csharp2(Java):
  version = "7.2"

'''
자식클래스에서는 부모로부터 상속받은 
모든 code를 실행시킬 수 있음
부모클래스의 클래스변수이름과
자식클래스의 클래스변수이름이 같은 경우
상속받은 스태틱메소드에서는
부모클래스에서 설정된 클래스변수값을 사용하고
상속받은 클래스메소드에서는
자식(자신)클래스에서 설정된 클래스변수값을 사용함

'''


print("--------Csharp1----------------")

c1_static = Csharp1.static_version()
c1_static.display_version()
c1_class = Csharp1.class_version()
c1_class.display_version()
print("--------Csharp2----------------")

c2_static = Csharp2.static_version()
c2_static.display_version()
c2_class = Csharp2.class_version()
c2_class.display_version()