
class Figure:
  def __init__(self, name, color):
    self.name = name
    self.color = color

class Quardangle(Figure):
  def set_area(self, width, height):
    self.width = width
    self.height = height
  def get_info(self):
    print(self.name, self.color, self.width * self.height)

class Quardangle_child(Quardangle):
  def set_diagonal(self, diagonal):
    self.diagonal = diagonal


figure = Figure('유관순', ' red')

quardangle = Quardangle('이순신', 'blue')
quardangle.set_area(3, 4)
quardangle.get_info()

print(quardangle.name)
print(quardangle.color)

'''
issubclass()
Quardangle 클래스가 Figure클래스의
자식클래스인지 알아보기
'''
print(issubclass(Quardangle, Figure))

quardangle_child = Quardangle_child('안중근','green')

print(issubclass(Quardangle_child, Quardangle))
print(issubclass(Quardangle_child, Figure))

print('--------------------------------------------')

print('isinstance(figure, Figure) :',isinstance(figure, Figure))
print('isinstance(quardangle, Quardangle) :',isinstance(quardangle, Quardangle))
print('isinstance(Quardangle_child, Quardangle_child)) :',isinstance(Quardangle_child, Quardangle_child))

print('--------------------------------------------')

print('isinstance(quardangle, Figure) :',isinstance(quardangle, Figure))
print('isinstance(qch, Figure) :',isinstance(quardangle_child, Figure))
print('isinstance(quardangle_child, Quardangle) :',isinstance(quardangle_child, Quardangle))
print('isinstance(quardangle_child, Quardangle_child) :',isinstance(quardangle_child, Quardangle_child))

print('--------------------------------------------')

print('isinstance(figure, Figure) :',isinstance(figure, Figure))
print('isinstance(figure, Quardangle) :',isinstance(figure, Quardangle))
print('isinstance(quardangle, Figure) :',isinstance(quardangle, Figure))
print('isinstance(quardangle_child, Quardangle) :',isinstance(quardangle_child, Quardangle))
print('isinstance(quardangle, Figure) :',isinstance(quardangle, Figure))