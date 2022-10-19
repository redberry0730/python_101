
num = 10
'''
  상속 :  default    :  부모클래스 (Parent, Super)
          추상적        기반클래스 (base class)
         extension   :  자식클래스  (Child, Sub)
          구체적        파생클래스 (derived class)


                             생물

                    동물             식물

            척추동물  무척추동물      꽃식물  민꽃식물

  포유류/조류/파충류  절지동물 연체동물    속씨식물
   /양서류/어류                        쌍떡잎식물 외떡잎식물

'''
'''
오버라이딩 :
  상속관계에서 부모클래스에 정의되어있는 메소드를
  자식클래스에서 상속받아서 사용하는 경우,
  선언부는 부모클래스에 있는 메소드의 선언부과
  똑같이 작성하고 body(몸통-구현부)의 내용을
  자식클래스에 맞게 적당히 변형해서 작성하는 것
  
  super() : 상속관계에서
            자식객체에서 부모의 멤버를 사용할 때
            사용하는 키워드
'''
class Animal:
  def sound(self):
    print('소리를 냅니다')

class Dog(Animal):
  # 부모클래스에 정의되어있는 sound() 메소드와
  #  선언부는 똑같이 작성함
  def sound(self):
    super().sound()
    # Dog 클래스에 맞는 내용으로 변형함
    print('멍멍')

class Cat(Animal):
  # 부모클래스에 정의되어있는 sound() 메소드와
  #  선언부는 똑같이 작성함
  def sound(self):
    super().sound()
    #  Cat 클래스에 맞는 내용으로 변형함
    print('야옹')

ani1 = Animal()
ani1.sound()
d1 = Dog()
d1.sound()
c1 = Cat()
c1.sound()




