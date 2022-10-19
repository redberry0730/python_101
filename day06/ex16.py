class Account:
  # 클래스 멤버변수
  # 개설한 계좌 수
  num_accounts = 0
  # 공용 계좌의 잔액
  common_balance = 0

  # self : instance member variable
  def __init__(self, name):
    self.name = name
    # 개인 계좌의 잔액
    self.balance = 100
    Account.num_accounts += 1

  def deposit(self, money):
    self.balance += money
  def deposit_common(self, money):
    Account.common_balance += money

  def display_account(self):
    print(f"{self.name} 님의 현재 잔액은 {self.balance} 원입니다")
    print(f"공용 계좌의 현재 잔액은 {Account.common_balance} 원입니다")
    print("------------------------------\n")


acc1 = Account("이순신")
print(Account.num_accounts," 번 째 계좌")
print(acc1.balance,'원')
acc2 = Account("유관순")
print(Account.num_accounts," 번 째 계좌")
print(acc2.balance,'원')
acc3 = Account("사임당")
print(Account.num_accounts," 번 째 계좌")
print(acc3.balance,'원')

# 이순신
acc1.deposit(200)
acc1.deposit_common(100)
acc1.display_account()
# 유관순
acc2.deposit(300)
acc2.deposit_common(200)
acc2.display_account()
# 사임당
acc3.deposit(500)
acc3.deposit_common(600)
acc3.display_account()