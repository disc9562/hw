class ATM:
	def __init__(self, account, password, money):
		self.account = account
		self.password = password
		self.money = money
	
	def withdraw(self, money):
		if(money < self.money):
			self.money = self.money - money
		else:
			return 'You are poor Q_Q'

	def getMoney(self):
		return self.money

account = input('請輸入帳號:')
password = input('請輸入密碼:')
money = input('金額:')

atm = ATM(account, password, int(money))
withdrawMoney = input('請輸入想領取的金額:')
atm.withdraw(int(withdrawMoney))
print(atm.getMoney())
withdrawMoney1 = input('請輸入想領取的金額:')
print(atm.withdraw(int(withdrawMoney1)))
#todo
#實作一個名為person的class其參數有身高、體重、姓名，並讓使用者可以輸入身高、體重、姓名
#person的class中有可以拿取bmi的method
