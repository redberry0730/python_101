num = 10
'''
클래스 메소드
@classmathod (데코레이터) 를 사용함

class 클래스이름:
  @classmethod
  def 메소드이름(cls, 매개변수, ...):
    statement....
'''
class Robot:
  count_robot = 0
  def __init__(self):
    Robot.count_robot += 1

  # 클래스 메소드
  @classmethod
  def display_count_robot_class(cls):
    print(f"클래스 메소드 : 로보트가 {cls.count_robot} 대 제작되었습니다")

  # 인스턴스 메소드
  def display_count_robot_instance(self):
    print(f"인스턴스 메소드 : 로보트가 {Robot.count_robot} 대 제작되었습니다")


Robot.display_count_robot_class()

r1 = Robot()
Robot.display_count_robot_class()
r1.display_count_robot_instance()
'''
r1.display_count_robot_class()
각각의 instance(object)에서도 클래스메소드에
접근이 가능하지만, 클래스이름으로 접근하는 것은 권장함 
'''
r2 = Robot()
Robot.display_count_robot_class()
r2.display_count_robot_instance()
r3 = Robot()
Robot.display_count_robot_class()
r3.display_count_robot_instance()


