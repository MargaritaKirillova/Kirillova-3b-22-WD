class BankAccount:
    def __init__(self, owner, acc_number, balance):
        self.owner = owner
        self.acc_number = acc_number
        self.balance = balance

    def replenishment(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount


bankAccount1 = BankAccount("Абрамова Юлия", 13563865545, 800000)
print(bankAccount1.balance)

bankAccount1.replenishment(60000)
print(bankAccount1.balance)

bankAccount1.withdrawal(100000)
print(bankAccount1.balance)