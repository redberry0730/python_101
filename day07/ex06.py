class Restaurant:
  list_type = ['한식', '양식', '중식']

  def __init__(self, name, restaurant_type, address):
    self.name = name
    self.__restaurant_type = restaurant_type
    self.address = address

  @property  # getter
  def restaurant_type(self):
    return self.__restaurant_type

  @restaurant_type.setter  # setter
  def restaurant_type(self, restaurant_type):
    if restaurant_type in Restaurant.list_type:
      self.__restaurant_type = restaurant_type
      print("식당 종류를 변경했습니다")
    else:
      print("{} 중 하나를 선택하세요".format(','.join(Restaurant.list_type)))

  def display_info(self):
    return (f'식당 이름 : {self.name}\n'
            f'식당 종류 : {self.restaurant_type}\n'
            f'식당 주소 : {self.address}')


rest1 = Restaurant('더조은 식당', '한식', '신촌')
print(rest1.display_info())

rest1.restaurant_type = '분식'
print(rest1.display_info())

rest1.restaurant_type = '양식'
print(rest1.display_info())