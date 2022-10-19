num=10
'''
추상클래스 : abstract class
  ㄴ 완성되지 않은 클래스
       ㄴ 완성되지 않은 메소드를 가지고 있음
            ㄴ 선언부만 있고 body(몸통:구현부)가 없음
                 ㄴ 추상메소드   
                 
추상클래스 작성 방법
1) abc 모듈을 import 함

2) 추상클래스의 이름 옆에 
   (metaclass=ABCMeta) 를 명시함
   
3) 추상메소드 작성
    ㄴ 메소드 이름 위에
       @abstractmethod 라는 데코레이터를 작성함
       
from abc import *
class AbstractTest(metaclass=ABCMeta):
  @abstractmethod
  def test(self):
    pass       
    
추상클래스는 추상메소드를 가지고 있기 때문에
              ㄴ 선언부만 있고 body(몸통:구현부)가 없음    
객체를 생성할 수 없음
추상클래스에 작성되어있는 추상메소드를 사용하려면
추상클래스를 상속받는 자식클래스에서
조상인 추상클래스의 추상메소드를 Overriding 해서
일반메소드를 만들어서 사용함

-- 추상클래스 작성 목적 --

추상클래스를 상속받은 자식클래스에서
추상클래스에 있는 추상메소드를
강제적으로 Overriding 하게 함

추상클래스를 상속받은 자식클래스에서
기본적으로 어떤 메소드를 작성해야 하는지
안내해 주는 안내서 역할을 함
   
'''
from abc import *

class Character(metaclass=ABCMeta):
  @abstractmethod
  def attack(self):
    pass
  @abstractmethod
  def move(self):
    pass
class Elf1(Character):
  def say_hello(self):
    print('안녕하세요')
class Elf1_Child(Elf1):
  # Overriding
  def attack(self):
    print("엘프 공격")
  # Overriding
  def move(self):
    print("엘프 이동")

'''
Character()
TypeError: Can't instantiate abstract class Character 
           with abstract methods attack, move
Elf1()           
TypeError: Can't instantiate abstract class Elf1 
           with abstract methods attack, move
'''


class Elf2(Character):
  def say_hello(self):
    print('안녕하세요')
  # Overriding
  def attack(self):
    print("엘프 공격")
  # Overriding
  def move(self):
    print("엘프 이동")

elf2 = Elf2()
elf2.attack()
elf2.move()
elf2.say_hello()


class Human(Character):
  # Overriding
  def attack(self):
    print("사람이 공격함")
  # Overriding
  def move(self):
    print("사람이 이동함")

human = Human()
human.attack()
human.move()