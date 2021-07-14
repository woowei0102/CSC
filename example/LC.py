class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance < amount:
            print('{}的存款不足.'.format(self.name))
        else:
            self.balance -= amount
    def show(self):
        print('{}餘額NT${}元'.format(self.name, self.balance))