# practice for creating classes and function

# create a program that has a class, class attributes, two functions for debit and credit

class Account:
    balance = 100
    account_number = 12345

    def credit(self, amount):
        self.balance = self.balance + amount
        print(f"Added ${amount} to account {self.account_number}")
        print(f"Account {self.account_number} has new balance of ${self.balance}")

    def debit(self, amount):
        self.balance = self.balance - amount
        print(f"Used ${amount} from account {self.account_number}")
        print(f"Account {self.account_number} has new balance of ${self.balance}")

    

acc = Account()
acc.debit(100)
acc.credit(150)

# ask = int(input("Give me a number: "))
# print(ask)
# print(type(ask))

a =2
print(f"this is number {a}")