class User:
    bank_name = "First National Dojo"
    def __init__(self, name):
        self.name = name
        self.accountBalance = 0

    def makeDepoit(self, amount):
        self.accountBalance += amount
        return self

    def makeWithdrawal(self, amount):
        self.accountBalance -= amount
        return self

    def displayUserBalance(self):
        print(f"{self.name}, Balance: ${self.accountBalance}")
        return self

    def transferMoney(self,amount,user):
        self.accountBalance -= amount
        user.accountBalance += amount
        self.displayUserBalance()
        user.displayUserBalance()
        return self

tom = User("Tom Cruise")
pete = User("Pete Mitchell")
ethan = User("Eathan Hunt")

tom.makeDepoit(50000).makeDepoit(100000).makeDepoit(150000).makeWithdrawal(25000).displayUserBalance()
pete.makeDepoit(150000).makeDepoit(200000).makeWithdrawal(50000).makeWithdrawal(150000).displayUserBalance()
ethan.makeDepoit(300000).makeWithdrawal(100000).makeWithdrawal(100000).makeWithdrawal(50000).displayUserBalance()
tom.transferMoney(75000, ethan)
