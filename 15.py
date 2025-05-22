class BankAccount:
    def _init_(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{self.owner} withdrew ₹{amount}. New balance: ₹{self.balance}")

    def show_balance(self):
        print(f"{self.owner}'s current balance: ₹{self.balance}")

acc = BankAccount("Rahul", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()