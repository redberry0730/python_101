num = 10
'''
정적 메소드 : static method
@staticmethod 사용함
매개변수부에 self키워드를 사용하지 않음
              ㄴ 기본적으로 생성자의 호출과 관계없이 동작함
                            (객체의 생성과)
class 클래스이름:
  @staticmethod 
  def 메소드이름(매개변수...):
    statement....
'''
class Calc:
  @staticmethod
  def add(num1, num2):
    return num1 + num2
  @staticmethod
  def multi(num1, num2):
    return num1 * num2

result1 = Calc.add(11,22)
print(result1)
result2 = Calc.multi(3, 6)
print(result2)


