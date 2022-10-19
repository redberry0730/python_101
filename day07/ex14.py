class ProductInfo:
  def __init__(self, name):
    self.name = name
    self.price = 10
  def __str__(self):
    return self.name
  def package_price(self):
    return self.price * 10

class PencilInfo(ProductInfo):
  def __init__(self, name):
    ProductInfo.__init__(self,name)
    self.price = 100
  # Override
  def package_price(self):
    return self.price * 15

class EraserInfo(ProductInfo):
  def __init__(self, name):
    ProductInfo.__init__(self, name)
    self.price = 50
  # Override
  def package_price(self):
    return self.price * 15
  # Override
  def __str__(self):
    return ProductInfo.__str__(self) + "가격 : " + str(self.price) + " 원"

pencil = PencilInfo("연필")
eraser = EraserInfo("지우개")

print(pencil)
print(eraser)

print(pencil.package_price())
print(eraser.package_price())




