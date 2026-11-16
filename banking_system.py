from abc import ABC, abstractmethod

# 1. Abstraction
class BankAccount(ABC):
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance          # 2. Encapsulation (Private)
        self.history = [f"Account opened with ₹{balance}"]

    def get_balance(self):
        return self.__balance

    def _set_balance(self, amount):
        self.__balance = amount

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.history.append(f"Deposited: +₹{amount}")
            print(f"Deposited ₹{amount}. Balance: ₹{self.__balance}")

    @abstractmethod
    def withdraw(self, amount):
        pass

    def show_history(self):
        print(f"\n--- History ({self.name}) ---")
        for h in self.history:
            print(h)

# 3. Inheritance & 4. Polymorphism
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.get_balance() - amount >= 500:   # Min ₹500 balance rule
            self._set_balance(self.get_balance() - amount)
            self.history.append(f"Withdrawn: -₹{amount}")
            print(f"Withdrawn ₹{amount}. Balance: ₹{self.get_balance()}")
        else:
            print("Error: Minimum ₹500 balance required!")

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if self.get_balance() - amount >= -2000: # ₹2000 overdraft limit
            self._set_balance(self.get_balance() - amount)
            self.history.append(f"Withdrawn: -₹{amount}")
            print(f"Withdrawn ₹{amount}. Balance: ₹{self.get_balance()}")
        else:
            print("Error: Overdraft limit exceeded!")

# Demo Run
if __name__ == "__main__":
    acc = SavingsAccount("101", "Loveleeta", 2000)
    acc.deposit(1000)
    acc.withdraw(800)
    acc.show_history()
  
