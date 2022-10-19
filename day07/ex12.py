
class Country:
  def __init__(self):
    self.name = "나라이름"
    self.population = "나라인구"
    self.capital = "나라수도"
  def display_info(self):
    print("나라 클래스입니다")

class Korea(Country):
  def __init__(self, name, population, capital):
    self.name = "나라이름"
    self.population = "나라인구"
    self.capital = "나라수도"
  def display_info(self):
    print(f" 나라 이름 : {self.name}\n",
          f"나라 인구 : {self.population}\n",
          f"나라 수도 : {self.capital}\n")

country = Country()
country.display_info()
print("--------------------------------")

korea = Korea("대한민국", "5000만", "서울")
korea.display_info()

'''
상속관계에 있는 두 클래스가 있을 때 
자식클래스에서 부모클래스에 있는 메소드를 Overriding한 상태에서,
Overriding된 자식클래스의 메소드를 호출하면
부모클래스에서 작성된 메소드의 body부분이 실행되지 않고
Overriding된 자식클래스의 메소드의 body부분이 실행됨

'''
