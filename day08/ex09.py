num=10
'''
다형성 :  polymorphism
          ㄴ 같은 모양의 code를 실행할 때
             여러가지 결과가 나오는 것 
'''
'''
객체지향 프로그래밍의 4 대 특성

 1) 추상화(abstraction)
 2) 캡슐화(encapsulation) : self.__변수이름
 3) 상속-(code 의 재사용) : inheritance <-- extension
 4) 다형성 - polymorphism
'''

class Musician:
  def introduce(self):
    print('안녕하세요~')
  def play(self):
    print('연주합니다')

class Pianist(Musician):
  def introduce(self): # Overriding
    print('안녕하세요~ 피아니스트입니다')
  def play(self): # Overriding
    print('딩동댕')
  def tuning(self):
    print('도레미')
  def __str__(self):
    return 'Pianist'

class Violinist(Musician):
  def introduce(self):
    print('안녕하세요~ 바이올리니스트입니다')
  def play(self):
    print('낑깽')
  def __str__(self):
    return 'Violinist'

class Vocalist(Musician):
  def introduce(self):
    print('안녕하세요~ 성악가입니다')
  def play(self):
    print('아에이오우')
  def __str__(self):
    return 'Vocalist'

# 연주자 리스트
list_musician = list()
pianist = Pianist()
violinist = Violinist()
vocalist = Vocalist()

list_musician.append(pianist)
list_musician.append(violinist)
list_musician.append(vocalist)

print('===== 연주자 인사 =====')
for musician in list_musician:
  musician.introduce()

print('===== 연주 =====')
for musician in list_musician:
  musician.play()

'''
list_musician = [Pianist(), Violinist(), Vocalist()]

list_musician <-- [pianist, violinist, vocalist]

print(Pianist())
print(Violinist())
print(Vocalist())
'''

