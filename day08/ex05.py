class Figure:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def display_info(self):
    print('Size :',self.width,', ',self.height)

class Rectangle(Figure):
  # Overriding
  def display_info(self):
    # print('Size :', self.width, self.height)
    # super().display_info()
    Figure.display_info(self)
    print('Area_rectangle :', self.width * self.height)

class Triangle(Figure):
  # Overriding
  def display_info(self):
    super().display_info()
    print('Area_triangle :',self.width * self.height * 0.5)

rect = Rectangle(3, 4)
rect.display_info()

tri = Triangle(6, 3)
tri.display_info()