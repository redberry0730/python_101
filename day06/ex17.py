class Person:
  member_ages = []

  def info(self, name, age, address):
    self.name = name
    self.age = age
    self.address = address
    print(f"이름은 {self.name}이고 "
          f"\n나이는{self.age}세입니다"
          f"\n주소는{self.address}입니다")
    Person.member_ages.append(self.age)
    print('회원 나이 정보 :',Person.member_ages)

p1 = Person()
p2 = Person()

p1.info('이순신', 48, '서울')
p2.info('더조은', 30, '수원')
p2.info('유관순', 19, '인천')


