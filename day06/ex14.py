class Account:
  def __init__(self):
    self.__balance = 0
  def open_account(self, money):
    if money > 0:
      self.__balance += money
      print("계좌 개설을 축하드립니다 !!!")
    self.display_account()

  def deposit(self, money):
    if money > 0:
      self.__balance += money
    else:
      print('입금하시는 금액을 확인해 주세요')
    self.display_account()

  def withdraw(self, money):
    if money <= self.__balance:
      self.__balance -= money
    else:
      print("잔액이 부족합니다")
    self.display_account()

  def display_account(self):
    print("현재 잔액 :",self.__balance,"원")

acc1 = Account()
acc1.open_account(10000)

acc1.deposit(30000)
acc1.deposit(15000)

acc1.withdraw(30000)
acc1.withdraw(30000)

